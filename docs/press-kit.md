# Astera Press Kit

Asteraを記事、紹介資料、発表、SNS、動画、事業説明で紹介する際に使える基本情報です。

---

## 正式名称

- Product全体：**Astera**
- 利用者向けApplication：**Astera App**
- 中核Runtime：**Astera v8**

---

## タグライン

> **問いを星図に変える。**

---

## 一文説明

Asteraは、質問、相談、資料、計画、AI回答を、目的、前提、事実、危険、反対視点、比較案、推奨判断、主役AIへの再指示へ整理する判断材料生成Systemです。

---

## 30文字前後の説明

**人やAIが答えを出す前に、判断材料を整理するSystem。**

---

## 短い紹介文

Asteraは、人やAIが答えを出す前に、見落としや思い込みを減らすための判断材料を作ります。

入力を8つの項目へ分解し、分かっていること、足りない情報、失敗の危険、反対意見、比較できる案を見える形にします。

---

## 標準紹介文

生成AIは、文章、説明、要約、提案、Codeを作ることに優れています。一方で、入力に含まれる前提不足、未確認情報、思い込み、重大Risk、一案への偏りまで、常に十分に整理できるとは限りません。

Asteraは、最終回答を作る前に判断の骨組みを作ります。

本当の目的、前提不足、事実確認、危機察知、反対視点、比較案、推奨判断、主役AIへの再指示という8つの判断材料へ整理し、利用者自身または主役AIが、より安全で具体的な回答を作れる状態へ導きます。

---

## Asteraが解決しようとしている問題

AIや人が早く答えを出そうとすると、次の問題が起きることがあります。

- 手段が目的に変わる
- 足りない前提を一般論で埋める
- 推測を事実として扱う
- 一つの案だけで進める
- 失敗時の影響を後回しにする
- 文章は自然だが、実行条件がない
- 結論が変わる条件を説明できない

Asteraは、答えの文章を長くするのではなく、答えを作る前に必要な判断材料を明確にします。

---

## Product構成

### Astera App

Asteraを利用するためのApplicationです。

- 新しい実行
- 目的選択
- File・Project情報
- Template・Option
- 8つの判断材料
- Turn
- Project
- History
- Result詳細
- Copy・Download・Share
- Settings
- Account・Security
- Plan・Credit・Billing
- Developer Mode

Web Browser、Smartphone、Tabletで同じ情報と操作を扱う共通Applicationとして設計されています。

### Astera v8

入力を決められた処理順で分解・比較し、8つの判断材料へ組み立てる中核Runtimeです。

Astera v8は生成AIそのものではありません。

### 主役AI

Asteraの判断材料を使い、説明、計画、文章、Codeなどの最終成果物を作ります。

主役AIには、ChatGPT、Claude、Gemini、自作AI、自社AIなどを利用できます。

---

## 基本の流れ

```text
質問・相談・資料・AI回答
  ↓
Astera App
  ↓
Astera v8
  ↓
8つの判断材料
  ↓
利用者 または 主役AI
  ↓
最終判断・計画・成果物
```

---

## 8つの判断材料

1. **本当の目的** — 表面的な依頼の奥で達成したいこと
2. **前提不足** — 判断する前に確認する条件
3. **事実確認** — 事実、未確認情報、意見、推測
4. **危機察知** — 失敗、損失、安全、信用、運用Risk
5. **反対視点** — 慎重な立場、別の立場、前提への反論
6. **比較案** — 二択以外を含む複数の選択肢
7. **推奨判断** — 現時点の方向、成立条件、停止条件
8. **主役AIへの再指示** — 最終成果物を作るための具体的な依頼

---

## 主な利用分野

- 商品・Service比較
- 企画・事業計画
- 契約・提案確認
- 開発・技術選択
- 障害原因分析
- AI回答Review
- 転職・独立・進路
- 人間関係
- Team Decision
- 調査設計
- 説明・文章作成前の論点整理

---

## 紹介時に使える例

### AI回答の確認

AIが「全面的に作り直せば解決する」と提案した場合、Asteraは、原因が確認されているか、局所改善や段階移行が可能か、TestやRollbackがあるかを整理します。

### 日常の判断

転職や独立について、本人の希望だけでなく、生活費、収入、健康、家族、段階的な案、延期条件を比較します。

### 事業・開発

新サービス公開について、機能完成だけでなく、Account、決済、規約、Support、障害、Mobile対応まで確認します。

---

## Astera Appの特徴

- 入力とResultだけでなく、ProjectとHistoryを扱う
- Resultを8つの固定項目で確認できる
- 項目単位でCopyできる
- Markdown DownloadやShareへ再利用できる
- 設定、Account、Security、Plan、Creditを同じApplicationで管理する
- PC、Smartphone、Tabletの画面幅と向きへ追従する
- Developer Modeから外部Applicationとの接続を管理する

---

## 開発者

Asteraは、**Seigo（GitHub: `seigo-gace`）が個人で構想・設計・開発しているProject**です。

既存の生成AIを作り直すのではなく、人とAIが答えを出す前の「判断」を支える独立した仕組みとして開発しています。

---

## 公式情報

- 公式Site：[asterav8.jp](https://asterav8.jp)
- Astera App：[app.asterav8.jp](https://app.asterav8.jp)
- GitHub：[seigo-gace/Astera](https://github.com/seigo-gace/Astera)
- App Guide：[Astera App完全ガイド](app-guide.md)
- Samples：[公開サンプル](../examples/README.md)

---

## 表記

- 正式表記：`Astera`
- Runtime：`Astera v8`
- Application：`Astera App`
- 開発者：`Seigo` または `seigo-gace`
- Tagline：`問いを星図に変える。`

Asteraを生成AIそのものとしてではなく、**人やAIが回答を作る前の判断材料生成System**として説明してください。

---

## 紹介時に避ける誤解

### 「別のChat AI」

Asteraは、会話文を自由生成するAIを主目的にしていません。

### 「AIの答えを自動的に正解へする」

Asteraは見落としを減らす判断材料を作りますが、すべての事実を自動的に保証するものではありません。

### 「人間の判断を不要にする」

利用者が理由と条件を理解して決められる状態を作ることが目的です。

---

## English description

**Astera is a decision-material system that structures questions, plans, documents, and AI responses before a person or a primary AI produces a final answer.**

It organizes the real objective, missing assumptions, known and unknown facts, risks, opposing views, comparable options, a recommended decision, and a refined instruction for a primary AI.

Astera consists of the user-facing **Astera App** and the deterministic **Astera v8** runtime.

---

## 問い合わせ

取材、掲載、連携、支援に関する問い合わせは、公式Siteの問い合わせ窓口をご利用ください。
