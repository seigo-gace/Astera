# Astera Press Kit

Asteraを記事、SNS、動画、発表、事業説明で紹介する際の基本情報です。

---

## 正式名称

- Product：**Astera**
- Application：**Astera App**
- 中核Runtime：**Astera v8**
- 開発者：**Seigo (`seigo-gace`)**

## Tagline

> **問いを星図に変える。**

## 一文説明

**Asteraは、人やAIが答えを出す前に、目的、前提、事実、危険、反対視点、比較案を8つの判断材料へ整理する仕組みです。**

---

## 短い紹介文

Asteraは、質問、相談、計画、AI回答を、判断に必要な8つの項目へ整理します。

文章をすぐ生成するのではなく、本当の目的、足りない情報、事実と推測、失敗の危険、反対意見、比較案を先に見える形にします。

利用者自身が判断に使うことも、ChatGPT、Claude、Gemini、自作AIなどへ渡して文章・計画・Codeへ仕上げることもできます。

---

## 8つの判断材料

1. 本当の目的
2. 前提不足
3. 事実確認
4. 危機察知
5. 反対視点
6. 比較案
7. 推奨判断
8. 主役AIへの再指示

---

## Asteraの特徴

- 生成AIそのものではなく、回答前の判断材料を整理する
- 一つの結論だけでなく成立条件・停止条件・別案を示す
- 日常、事業、契約、開発、AI回答確認へ使える
- 目的に応じてReview、比較、検証、計画などを選べる
- Resultを固定8項目で読み比べられる
- 追加Option、Plan、Credit、Developer Modeを一つのAppで扱う設計

---

## 追加Option

| Option | 内容 |
|---|---|
| 高精度翻訳 | 文書構造と情報量を維持して翻訳だけを行う |
| エージェントモード | Low・Medium・Highの複数Stepで調査・処理を進める |
| 書類作成 | 公式・個別Templateへ内容を反映する |
| 外部Storage転送 | 完成結果を利用者管理のStorageへ一方向転送する |

Private Mode、暗号化、Astera Storage、Developer Modeは独立機能です。

---

## Plan

| Plan | 税込月額 | 月次Credit |
|---|---:|---:|
| Free | 0円 | 初回20,000／以後10,000 |
| Basic | 980円 | 180,000 |
| Pro | 2,980円 | 640,000 |
| Business | 9,980円 | 2,200,000 |
| Enterprise | 29,800円 | 6,600,000 |

- Basic：高精度翻訳、外部Storage転送、Private Mode、Astera Storage
- Pro：書類Template、Developer Mode・API
- Business／Enterprise：より大きな月次CreditとStorage上限

料金の詳細は[Plan・料金・Credit](plans-and-credits.md)をご覧ください。

> 現在はCatalog内容の公開段階です。契約・購入はAstera Appの料金Pageと決済接続の公開後に開始します。

---

## Developer Mode

Developer ModeはPro以上を対象に、次のAPIをApplicationや業務Systemへ組み込むための管理画面です。

- 判断材料生成
- 根拠検索
- 判定
- Astera統合
- Webhook Gateway接続

API Key、Sandbox／Production、Scope、Usage、Credit、Rate、Quota、停止状態を管理する設計です。

現在は仕様公開段階で、実EndpointとAPI Key発行は準備中です。

---

## 主なUse Case

### AI回答の確認

AIが全面移行を提案した場合、原因が確認されているか、局所改善や段階移行が可能か、TestやRollbackがあるかを整理します。

### 事業・企画

新Service公開について、機能だけでなく、利用者、料金、規約、Support、障害、停止条件まで確認します。

### 日常の判断

転職、独立、購入などについて、希望だけでなく、費用、期限、家族、代替案、延期条件を比較します。

### 開発・運用

技術案、障害原因、実装順、依存関係、失敗条件を整理します。

公開Sampleは[examples](../examples/README.md)にあります。

---

## Product構成

```text
利用者
↓
Astera App
入力・目的・Option・Result・Project・Credit
↓
Astera v8
8つの判断材料へ整理
↓
利用者 または 主役AI
最終判断・文章・計画・Code
```

Astera AppはWeb、Smartphone、Tablet、Android、iOSを共通Sourceで扱う構成です。

---

## 現在の公開状態

現在公開しているもの：

- Asteraの目的と処理構造
- 8つの判断材料
- Option、Plan、料金、Credit
- Developer Mode仕様
- Appの画面・利用Flow
- 入出力Sample

現在、利用可能とは案内していないもの：

- Production版Astera App
- Account・決済の本番運用
- File内容解析・Storage・Share
- Developer APIの実Endpoint
- Android／iOS Store版

最新情報は[現在の公開状態](current-status.md)をご覧ください。

---

## 表記

- `Astera`
- `Astera App`
- `Astera v8`
- `Seigo` または `seigo-gace`
- `問いを星図に変える。`

Asteraを「別のChat AI」ではなく、**人やAIが答えを出す前の判断材料を整理する仕組み**として紹介してください。

---

## English description

**Astera structures questions, plans, and AI responses into eight categories of decision material before a person or a primary AI produces a final answer.**

It identifies the real objective, missing assumptions, facts, risks, opposing views, comparable options, a recommended decision, and a refined instruction for a primary AI.

---

## 公式情報

- 公式Site：[asterav8.jp](https://asterav8.jp)
- GitHub：[seigo-gace/Astera](https://github.com/seigo-gace/Astera)
- [追加Option](options.md)
- [Plan・料金・Credit](plans-and-credits.md)
- [Developer Mode](developer-mode.md)
- [現在の公開状態](current-status.md)
- [公開Sample](../examples/README.md)
