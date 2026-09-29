# /// script
# requires-python = ">=3.10"
# dependencies = ["fonttools[woff]==4.60.1", "brotli==1.1.0", "uharfbuzz==0.52.0"]
# ///
"""Verify font semantics and Tibetan shaping, independently of compression bytes."""

from io import BytesIO
from pathlib import Path

from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.ttLib import TTFont
import uharfbuzz as hb

ROOT = Path(__file__).resolve().parents[1]


def shape(font, text):
    buffer = hb.Buffer()
    buffer.add_str(text)
    buffer.guess_segment_properties()
    buffer.language = "bo"
    hb.shape(font, buffer)
    return [
        (info.codepoint, info.cluster, pos.x_advance, pos.y_advance, pos.x_offset, pos.y_offset)
        for info, pos in zip(buffer.glyph_infos, buffer.glyph_positions)
    ]


def harfbuzz_font(font):
    # HarfBuzz consumes SFNT; expand WOFF2 before passing it to the shaper.
    stream = BytesIO()
    font.flavor = None
    font.save(stream)
    return hb.Font(hb.Face(stream.getvalue()))


def main():
    with TTFont(ROOT / "Paramita.ttf", recalcTimestamp=False) as source, TTFont(
        ROOT / "web/Paramita.woff2", recalcTimestamp=False
    ) as web:
        assert source.getGlyphOrder() == web.getGlyphOrder(), "Glyph order changed"
        assert source.getBestCmap() == web.getBestCmap(), "Character coverage changed"
        assert set(source.keys()) - {"DSIG"} == set(web.keys()), "Unexpected table change"
        # WOFF2 transforms these tables; compare outlines separately below.
        for tag in set(web.keys()) - {"GlyphOrder", "head", "glyf", "loca"}:
            assert source.getTableData(tag) == web.getTableData(tag), f"{tag} changed"
        for key, value in vars(source["head"]).items():
            if key not in {"checkSumAdjustment", "flags"}:
                assert value == getattr(web["head"], key), f"head.{key} changed"
        assert (source["head"].flags ^ web["head"].flags) & ~(1 << 11) == 0
        source_glyphs, web_glyphs = source.getGlyphSet(), web.getGlyphSet()
        for name in source.getGlyphOrder():
            pens = [DecomposingRecordingPen(glyphs) for glyphs in (source_glyphs, web_glyphs)]
            source_glyphs[name].draw(pens[0])
            web_glyphs[name].draw(pens[1])
            assert pens[0].value == pens[1].value, f"Outline changed: {name}"
            programs = [getattr(font["glyf"][name], "program", None) for font in (source, web)]
            instructions = [program.getBytecode() if program is not None else b"" for program in programs]
            assert instructions[0] == instructions[1], f"Hint instructions changed: {name}"

        fonts = [harfbuzz_font(font) for font in (source, web)]
        samples = [
            "བོད་ཡིག", "སངས་རྒྱས།", "བསྒྲུབས།", "ཧཱུྃ།",
            "ཨོཾ་མ་ཎི་པདྨེ་ཧཱུྃ།", "༢༠༢༦", "中文 ཤེས་རབ། wisdom",
        ]
        samples += [chr(cp) for cp in source.getBestCmap() if 0x0F00 <= cp <= 0x0FFF]
        # Exercise base/subjoined/vowel combinations beyond a fixed page corpus.
        samples += [
            chr(base) + chr(subjoined) + chr(vowel)
            for base in range(0x0F40, 0x0F6D)
            for subjoined in range(0x0F90, 0x0FBD)
            for vowel in (0x0F71, 0x0F72, 0x0F74, 0x0F7A, 0x0F7C, 0x0F80)
            if all(cp in source.getBestCmap() for cp in (base, subjoined, vowel))
        ]
        for text in samples:
            assert shape(fonts[0], text) == shape(fonts[1], text), f"Shaping changed: {text!r}"
        print(f"Verified {len(source.getGlyphOrder()):,} outlines, all metadata/layout/hint tables, "
              f"and {len(samples):,} HarfBuzz shaping samples.")


if __name__ == "__main__":
    main()
