# Paramita Tibetan Font (彼岸藏文字體)

[![License: OFL 1.1](https://img.shields.io/badge/License-OFL%201.1-lightgreen.svg)](http://scripts.sil.org/OFL)

---

**[English](#english-version) | [中文版](#中文版)**

---

## 中文版

### 介紹

Paramita (彼岸) 藏文字體是由般若文化研究學會 (Prajina Cultural Research Association) 發起的一項開源字體專案。般若文化研究學會是由一群來自台灣的頂尖藏文翻譯、AI工程師所組成的專業團隊，致力於運用最新科技來保存和推廣藏傳文化，並與南印度三大寺的六家圖書館等機構合作。

此專案開源 Paramita 藏文字體，希望能為需要使用藏文的信眾、研究者、設計師及所有藏人提供一個美觀且自由使用的選擇，讓藏傳文化的智慧與慈悲透過清晰優美的文字傳播得更遠，讓智慧不再遙不可及。

### 字體來源

Paramita 字體是基於 [Jomolhari-Regular](https://fonts.google.com/specimen/Jomolhari) 字體進行修改與優化的衍生作品。Jomolhari 字體本身也是基於 SIL Open Font License, Version 1.1 授權發布的。我們感謝 Jomolhari 字體原始開發者的貢獻。

### 設計與發行

*   **設計師 (Designer):** Evian Tien
*   **發行單位 (Publisher):** [般若文化研究學會 (Prajina Cultural Research Association)](https://Prajina.org)

### 願景

讓智慧不再遙不可及，為面對生活煩惱的人帶來內心的寧靜。透過開源工具與資源，支持藏傳文化的保存、研究與傳播。

### 授權條款 (License)

Paramita 字體根據 **SIL Open Font License, Version 1.1 (OFL 1.1)** 授權發行。

*   [本 repo 的授權條款全文](OFL.txt)

### 在 Web App 使用

建議使用完整字形的 **WOFF2** 網頁版，搭配只套用藏文的 CSS：

1. 將 [`web/Paramita.woff2`](web/Paramita.woff2)、[`web/paramita.css`](web/paramita.css)、[`web/ATTRIBUTION.txt`](web/ATTRIBUTION.txt) 與 [`OFL.txt`](OFL.txt) 放到 app 的公開靜態目錄，例如 `public/fonts/paramita/`。CSS 與 WOFF2 請放在同一層。
2. 載入 CSS，將 Paramita 放在字體清單最前面：

```html
<link rel="stylesheet" href="/fonts/paramita/paramita.css">
<style>
  body { font-family: "Paramita", system-ui, sans-serif; }
  input, textarea, button { font: inherit; }
  [lang="bo"] { line-height: 2; letter-spacing: normal; }
</style>
<p lang="bo">སངས་རྒྱས། བསྒྲུབས།</p>
```

沒有藏文的頁面不需要下載字體；藏文出現時才下載完整 WOFF2。中文和英文仍使用後面的字體。原始 TTF 保留給桌面安裝。

接入細節、可選預載、快取、藏文排版注意事項及可重建流程，請見 [Web 使用指南](web/README.md#中文版)。

### 支持我們

如果您認同我們的理念，並希望支持藏傳文化的保存與推廣，歡迎訪問 [般若文化研究學會網站](https://Prajina.org) 了解更多信息或參與支持專案。

---

## English Version

### Introduction

Paramita (彼岸) Tibetan Font is an open-source font project initiated by the Prajina Cultural Research Association. The Association comprises a professional team of top Tibetan translators and AI engineers from Taiwan, dedicated to preserving and promoting Tibetan culture using the latest technology, in collaboration with institutions like the six libraries of the three great monasteries in South India.

This project open-sources the Paramita Tibetan font, aiming to provide a beautiful and freely usable option for devotees, researchers, designers, and anyone needing to use the Tibetan script. We hope that the wisdom and compassion of Tibetan culture can spread further through clear and elegant text, making wisdom accessible.

### Font Origin

The Paramita font is a derivative work modified and optimized based on the [Jomolhari-Regular](https://fonts.google.com/specimen/Jomolhari) font. The Jomolhari font itself is also released under the SIL Open Font License, Version 1.1. We appreciate the contributions of the original developers of the Jomolhari font.

### Design and Publishing

*   **Designer:** Evian Tien
*   **Publisher:** [Prajina Cultural Research Association (般若文化研究學會)](https://Prajina.org)

### Vision

To make wisdom accessible and bring inner peace to those facing life's challenges. To support the preservation, study, and dissemination of Tibetan culture through open-source tools and resources.

### License

The Paramita font is licensed under the **SIL Open Font License, Version 1.1 (OFL 1.1)**.

*   [Full license text in this repository](OFL.txt)

### Use in a Web App

Use the full **WOFF2** web font with Tibetan-scoped CSS:

1. Copy [`web/Paramita.woff2`](web/Paramita.woff2), [`web/paramita.css`](web/paramita.css), [`web/ATTRIBUTION.txt`](web/ATTRIBUTION.txt), and [`OFL.txt`](OFL.txt) to a public static directory such as `public/fonts/paramita/`. Keep the CSS and WOFF2 together.
2. Load the stylesheet and put Paramita first in your font stack:

```html
<link rel="stylesheet" href="/fonts/paramita/paramita.css">
<style>
  body { font-family: "Paramita", system-ui, sans-serif; }
  input, textarea, button { font: inherit; }
  [lang="bo"] { line-height: 2; letter-spacing: normal; }
</style>
<p lang="bo">སངས་རྒྱས། བསྒྲུབས།</p>
```

Pages without Tibetan do not need to download the font. Tibetan text triggers the full WOFF2 download; Chinese and Latin use your fallback fonts. The original TTF remains available for desktop installation.

See the [web integration guide](web/README.md#english) for optional preload, caching, Tibetan shaping, and reproducible builds.

### Support Us

If you resonate with our mission and wish to support the preservation and promotion of Tibetan culture, please visit the [Prajina Cultural Research Association website](https://Prajina.org) for more information or to participate in supporting our projects.

