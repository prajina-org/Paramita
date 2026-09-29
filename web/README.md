# Paramita for the web

**[中文版](#中文版) | [English](#english)**

## 中文版

### 直接接入

將 `Paramita.woff2`、`paramita.css`、`ATTRIBUTION.txt` 和根目錄的 `OFL.txt` 複製到 app 的公開靜態目錄（例如 `public/fonts/paramita/`），依照[主 README](../README.md#在-web-app-使用)載入 CSS 並設定字體清單。這適用於一般 HTML、React、Vue、Next.js 等能提供靜態檔案的 web app，無需字體載入套件。若 app 部署在子路徑，請調整 `<link>` 的 URL；CSS 內的字體 URL 相對於 CSS 本身解析。

`paramita.css` 只宣告 `@font-face`，讓 app 自己決定哪些元件使用 Paramita。放在原有字體清單最前面即可保留其他語言的字體，例如 `"Paramita", "Lora", Georgia, serif`。輸入框與按鈕請另設 `font: inherit`，避免瀏覽器預設樣式覆蓋字體。

### 效率與正確性

- **完整 WOFF2，沒有 subset。** 保留原始 3,202 個字形與 2,752 個 Unicode 對應，以及藏文 shaping、字距、輪廓、hinting 和內嵌授權資料。只移除原始二進位的 `DSIG` 簽章。
- **`unicode-range: U+0F00-0FFF`** 只將藏文交給 Paramita，中文與 Latin 使用 fallback。沒有匹配文字時不下載；首次匹配時下載整份字體。這不是檔案裁切，也不會分段下載。若有舊式 PUA 編碼內容，這份 CSS 不涵蓋它；請先轉成 Unicode 藏文，或針對已知編碼另行設定。
- **`font-display: swap`** 先顯示系統 fallback，下載完成再換成 Paramita。不同 fallback 的字形尺寸可能造成版面位移；請在目標裝置測試。
- 這是 **Regular 400** 字體，並無真正的粗體／斜體版本。瀏覽器可能合成粗體與斜體；若要維持原始字形，可對藏文元素設定 `font-synthesis: none`。
- 藏文段落可從 `line-height: 2` 開始調整；保留 `letter-spacing: normal`。請檢查高堆疊、上／下母音符號、換行、縮放，以及容器的固定高度或 `overflow: hidden` 是否裁切文字。
- 保留預設 OpenType shaping。不要停用 `ccmp`、`calt`、`abvs`、`blws`，也不要將同一音節中的基字、下加字與母音拆成不同字體或個別元件。

藏文堆疊會依賴沒有直接 Unicode 對應的字形。若未來真的需要 subset，請使用能保留 OpenType layout closure 的工具，並以實際內容與 shaping 測試驗證；不要只依照頁面上的字元刪除字形。

### 可選預載與部署

只有確定首屏有藏文、需要盡早載入的頁面，才在 `<head>` 加上：

```html
<link rel="preload" href="/fonts/paramita/Paramita.woff2"
      as="font" type="font/woff2" crossorigin>
```

URL 必須與 CSS 最終解析的 URL 一致，即使同源也加 `crossorigin`。預載會強制下載，沒有藏文的頁面請省略；也避免框架字體工具與手動 `<link>` 重複管理同一字體。

自行託管，不要把 GitHub 的檔案預覽 URL 當作字體 CDN。回應字體時使用 `Content-Type: font/woff2`；若放在不同來源，設定允許 app 來源的 `Access-Control-Allow-Origin`。確認部署後沒有 404、CORS 或字體解析錯誤。可為**含版本或內容雜湊的 URL** 使用 `Cache-Control: public, max-age=31536000, immutable`；內容改版時換 URL。沒有版本的固定 URL 請使用會重新驗證的快取策略，避免使用者長期拿到舊字體。

### 檔案大小

此 repo 使用下方固定版本的轉檔流程，將原始 TTF 的 1,341,084 bytes 壓縮為 WOFF2 的 359,456 bytes，減少約 **73.2%**。這是完整字體的容器壓縮，保留原始時間戳，沒有刪除字形。

### 預覽與維護

在 repo 根目錄執行 `python3 -m http.server 8000`，開啟 `http://localhost:8000/web/demo.html`。示例包含藏文堆疊、梵文轉寫、混合語言及輸入框。

使用 [uv](https://docs.astral.sh/uv/) 重建及驗證（依賴版本已在腳本中固定，app 不需要 Python）：

```sh
uv run scripts/build_webfont.py
uv run scripts/build_webfont.py --check
uv run tests/verify_webfont.py
```

`--check` 比較產物是否與重建一致。驗證腳本比較全部字形輪廓、字碼、metrics、layout 與 hinting 資料，並比較原始 TTF 和解壓後 WOFF2 的 HarfBuzz shaping。CI 會執行這兩項檢查。瀏覽器仍需確認：純中文／英文頁面不請求 WOFF2、動態插入藏文時成功載入、高堆疊不被裁切。

隨字體散布 `OFL.txt` 和 `ATTRIBUTION.txt`。OFL 1.1 是原始 Paramita README 與字體內嵌資料宣告的授權版本；原始 copyright 與內部字體名稱 `Paramita_v1` 均保留。CSS 中的 `Paramita` 是 web family 別名。

## English

### Integration

Copy `Paramita.woff2`, `paramita.css`, `ATTRIBUTION.txt`, and the root `OFL.txt` into your app's public static directory, such as `public/fonts/paramita/`. Follow the [main README](../README.md#use-in-a-web-app) to load the CSS and apply the font stack. This works with plain HTML and frameworks that serve static assets, including React, Vue, and Next.js; no font loader package is required. Adjust the stylesheet URL for apps deployed under a subpath. The font URL resolves relative to the stylesheet.

The stylesheet only declares `@font-face`; your app chooses the elements that use it. Put Paramita first in your existing font stack, e.g. `"Paramita", "Lora", Georgia, serif`. Set `font: inherit` on form controls when needed.

### Performance and shaping

- **Full WOFF2, without subsetting.** All 3,202 glyphs, 2,752 Unicode mappings, shaping data, metrics, outlines, hinting, and name/license records are retained. Only the original binary's `DSIG` signature is removed.
- **`unicode-range: U+0F00-0FFF`** restricts font selection to Tibetan. Chinese and Latin use your fallback fonts. Without matching text, no font download is needed; the first match downloads the whole file. This does not subset the binary or download individual glyphs. Legacy PUA-encoded text is outside this CSS range: convert it to Unicode Tibetan or define a separate range for the known encoding.
- **`font-display: swap`** shows fallback text while the font loads. Different fallback metrics can cause layout shifts; test your target devices.
- Only **Regular 400** is supplied. Browsers may synthesize bold/italic; use `font-synthesis: none` on Tibetan elements to retain the original shapes if desired.
- Start Tibetan paragraphs with `line-height: 2` and `letter-spacing: normal`. Check tall stacks, upper/lower vowel marks, wrapping, zoom, fixed heights, and clipping containers.
- Keep default OpenType shaping, including `ccmp`, `calt`, `abvs`, and `blws`. Keep each syllable's base, subjoined consonants, and vowels in the same font run; do not split them across individual components.

Tibetan stacks depend on glyphs without direct Unicode mappings. If you later subset, use a tool that retains OpenType layout closure and validate real text and shaping results. Removing glyphs based only on visible page characters can break stacks.

### Optional preload and hosting

Preload only on pages where Tibetan is visible immediately and earlier loading matters:

```html
<link rel="preload" href="/fonts/paramita/Paramita.woff2"
      as="font" type="font/woff2" crossorigin>
```

Match the resolved CSS font URL exactly and include `crossorigin` even for same-origin fonts. Preloading forces a download; omit it on pages without Tibetan. Avoid managing the same font through both a framework loader and manual links.

Self-host the files; GitHub preview URLs are not font CDN URLs. Serve WOFF2 with `Content-Type: font/woff2`. For cross-origin hosting, allow the app's origin via `Access-Control-Allow-Origin`. Check for 404, CORS, and font decoding errors after deployment. Use `Cache-Control: public, max-age=31536000, immutable` for **versioned or content-hashed URLs**, changing the URL when the font changes. Use revalidation for an unversioned fixed URL.

### File size

This repository's pinned build compresses the original 1,341,084-byte TTF to a 359,456-byte WOFF2 (**73.2% smaller**). This is full-font container compression; it preserves the source timestamp and does not remove glyphs.

### Preview and maintenance

From the repository root, run `python3 -m http.server 8000` and visit `http://localhost:8000/web/demo.html`. The demo includes Tibetan stacks, Sanskrit transliteration, mixed scripts, and an editable field.

Rebuild and verify with [uv](https://docs.astral.sh/uv/); dependencies are pinned in the scripts. Apps consuming the font do not need Python:

```sh
uv run scripts/build_webfont.py
uv run scripts/build_webfont.py --check
uv run tests/verify_webfont.py
```

`--check` compares the committed artifact to a fresh build. Verification compares every outline, character mapping, metrics, layout, and hinting tables, then compares HarfBuzz shaping of the TTF and expanded WOFF2. CI runs both checks. In browsers, also check that Chinese/English-only pages do not request WOFF2, dynamically added Tibetan loads it successfully, and tall stacks are not clipped.

Redistribute `OFL.txt` and `ATTRIBUTION.txt` with the font. OFL 1.1 is the version declared by Paramita's existing README and embedded font metadata. The original copyright and internal family name `Paramita_v1` are retained; `Paramita` is the CSS family alias.

## References

- [FontTools WOFF2 conversion](https://fonttools.readthedocs.io/en/stable/ttLib/woff2.html)
- [FontTools subsetting and layout closure](https://fonttools.readthedocs.io/en/stable/subset/)
- [MDN: unicode-range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
- [MDN: font-display](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
- [MDN: preloading fonts](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload)
