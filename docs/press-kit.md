# Astera Press Kit

Asteraを記事、紹介資料、発表、SNS、動画、事業説明で紹介する際に使える基本情報です。

**現在紹介できる範囲は、Asteraの目的、8つの判断材料、Astera v8の処理構造、公開Sample、Astera AppのSource実装範囲です。**

Astera Appを本番利用可能な完成Productとして紹介しないでください。

最新の公開判定は[現在の公開状態](current-status.md)を確認してください。

---

## 正式名称

- Product全体：**Astera**
- 利用者向けFrontend：**Astera App**
- 中核Runtime：**Astera v8**

---

## Tagline

> **問いを星図に変える。**

---

## 一文説明

Asteraは、質問、相談、計画、AI回答を、目的、前提、事実、危険、反対視点、比較案、推奨判断、主役AIへの再指示へ整理する判断材料生成Systemです。

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

本当の目的、前提不足、事実確認、危機察知、反対視点、比較案、推奨判断、主役AIへの再指示という8つの判断材料へ整理し、利用者自身または主役AIが、より安全で具体的な回答を作れる状態を目指します。

---

## 現在公開している実績

- Asteraの目的と生成AIとの役割分担
- 8つの判断材料
- Astera v8の処理構造
- 日常、事業、開発、AI回答確認等のUse Case
- 具体的なInput・Output Sample
- Astera Appの43 Route Pattern
- 入力、目的選択、Result Mapping、Turn、Copy、Markdown Download等のFrontend Source実装
- Desktop、Smartphone、Tablet向けResponsive Source
- Android／iOS Native Shell用の設定とWorkflow
- Public Documentation、Support、Security、Contribution情報

---

## 現在利用可能とは紹介しないもの

- Astera AppのProduction稼働
- Backend EndpointとSchemaの実接続
- File本体Uploadと内容解析
- Project、History、ShareのServer保存
- Account登録、Login、Passkey、二段階認証
- Plan、Credit、Checkout、Billing
- 外部Storage
- Developer API
- Android／iOS実機
- Google Play／App Store公開

画面やRouteがSourceにあることを、利用可能機能として紹介しないでください。

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

Asteraを利用するためのFrontendです。

現在のSource実装には次が含まれます。

- 新しい実行画面
- 10種類の目的選択
- Template・追加Option
- File Metadata
- 処理段階表示
- 8つの判断材料へのResult Mapping
- Turn
- Copy・Markdown Download・端末共有
- Project、History、Settings、Account、Security、Plan、Credit、Developer、Share等の43 Route Pattern
- Desktop、Smartphone、Tablet向けResponsive Shell
- Android／iOS Native Shell用設定

Backend、認証、決済、Storage、実機等を含む本番動作は現在の公開実績に含めません。

### Astera v8

入力を決められた処理順で分解・比較し、8つの判断材料へ組み立てる中核Runtimeです。

Astera v8は生成AIそのものではありません。

### 主役AI

Asteraの判断材料を使い、説明、計画、文章、Code等の最終成果物を作ります。

現在公開できる利用Flowは、AsteraのResultをCopyし、ChatGPT、Claude、Gemini、自作AI等へ渡す方法です。

Developer APIによる自動接続は現在の公開実績に含めません。

---

## 基本の流れ

```text
質問・相談・計画・AI回答
  ↓
Astera App Frontend
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

## 紹介時に使えるSample

### AI回答の確認

AIが「全面的に作り直せば解決する」と提案した場合、Asteraは、原因が確認されているか、局所改善や段階移行が可能か、TestやRollbackがあるかを整理します。

### 日常の判断

転職や独立について、本人の希望だけでなく、生活費、収入、健康、家族、段階的な案、延期条件を比較します。

### 事業・開発

新Service公開について、機能完成だけでなく、Account、決済、規約、Support、障害、Mobile対応等の確認項目を整理します。

具体的なInput・Outputは[公開Sample](../examples/README.md)にあります。

---

## 開発者

Asteraは、**Seigo（GitHub: `seigo-gace`）が個人で構想・設計・開発しているProject**です。

既存の生成AIを作り直すのではなく、人とAIが答えを出す前の「判断」を支える独立した仕組みとして開発しています。

---

## 公式情報

- 公式Site：[asterav8.jp](https://asterav8.jp)
- GitHub：[seigo-gace/Astera](https://github.com/seigo-gace/Astera)
- 現在の公開状態：[Current Status](current-status.md)
- App Source説明：[Astera App Guide](app-guide.md)
- Sample：[公開Sample](../examples/README.md)

Astera AppのURLを、動作確認完了前に利用可能なApplicationとして案内しないでください。

---

## 表記

- 正式表記：`Astera`
- Runtime：`Astera v8`
- Frontend：`Astera App`
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

### 「Appが本番公開済み」

現在はFrontend Source実装範囲を公開しています。Production、Backend、Account、決済、Native App等の本番利用は未確認です。

---

## English description

**Astera is a decision-material system that structures questions, plans, and AI responses before a person or a primary AI produces a final answer.**

It organizes the real objective, missing assumptions, known and unknown facts, risks, opposing views, comparable options, a recommended decision, and a refined instruction for a primary AI.

The current public release covers the Astera concept, the eight-part decision structure, architecture documentation, public examples, and the implemented scope of the Astera App frontend source.

It does not claim that production deployment, backend services, authentication, billing, storage, developer APIs, or native applications are currently available.

---

## 問い合わせ

取材、掲載、連携、支援に関する問い合わせは、公式Siteの問い合わせ窓口をご利用ください。
