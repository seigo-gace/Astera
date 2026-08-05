# Astera

> **問いを星図に変える。**

Asteraは、質問・相談・計画・AIの回答を、**人が判断するために必要な材料へ整理する仕組み**です。

答えを急いで作るのではなく、目的、足りない前提、確認できる事実、危険、反対視点、比較案を先に整理します。その結果を利用者自身が判断に使うか、ChatGPT、Claude、Gemini、自作AIなどへ渡して最終成果物へ仕上げます。

## まず知りたいこと

| 知りたいこと | 読むPage |
|---|---|
| Asteraで何ができるか | このREADME |
| 追加Optionの違い | [追加Option](docs/options.md) |
| Plan・料金・Credit | [Plan・料金・Credit](docs/plans-and-credits.md) |
| APIやDeveloper Mode | [Developer Mode](docs/developer-mode.md) |
| 現在どこまで公開されているか | [現在の公開状態](docs/current-status.md) |
| 実際の入力と結果 | [公開Sample](examples/README.md) |
| すべての説明 | [Documentation](docs/README.md) |

---

## Asteraが整理する8つの判断材料

| 番号 | 判断材料 | 分かること |
|---:|---|---|
| 01 | 本当の目的 | 表面的な依頼の奥で本当に達成したいこと |
| 02 | 前提不足 | 判断前に確認する条件 |
| 03 | 事実確認 | 事実、未確認情報、意見、推測の区別 |
| 04 | 危機察知 | 失敗、損失、安全、信用、運用上の危険 |
| 05 | 反対視点 | 見落としている反論や別の立場 |
| 06 | 比較案 | 二択に限らない複数の選択肢 |
| 07 | 推奨判断 | 現時点の方向、成立条件、停止条件 |
| 08 | 主役AIへの再指示 | 最終成果物を作るための具体的な依頼文 |

Asteraは一つの結論を押しつけません。**なぜその判断になるのか、何が変われば判断も変わるのか**を見える形にします。

---

## どんな場面で使うのか

### 日常の判断

- 商品、Service、住居、旅行先を比較する
- 転職、進路、独立を検討する
- 人間関係で事実と推測を分ける

### 仕事・事業

- 企画、提案、事業計画の抜けを確認する
- 契約や発注条件を整理する
- 新Service公開や料金変更のRiskを確認する

### 開発・運用

- 技術案を同じ条件で比較する
- 障害原因を決めつけず確認順を作る
- 実装計画の依存関係、停止条件、Rollbackを整理する

### AI回答の確認

- 根拠のない断定を見つける
- 最新確認が必要な箇所を分ける
- 反対意見や重大Riskの抜けを確認する
- より具体的な再質問・再指示を作る

---

## Astera Appで選べるもの

### 目的

自動、Review、比較、検証、改善、調査、計画、検討、判断、原因分析から、今回行いたいことを選びます。

### 追加Option

| Option | 内容 |
|---|---|
| 高精度翻訳 | 見出し、表、Code、URL、情報量を維持し、本文だけを翻訳する |
| エージェントモード | Low・Medium・Highの複数Stepで調査や処理を進める |
| 書類作成 | 公式・個別Templateへ内容を反映し、書式崩れを検査する |
| 外部Storage転送 | 完成した結果を利用者管理のStorageへ一方向転送する |

Private Mode、暗号化、Astera Storage、Developer Modeは、実行ごとに追加するOptionではなく独立機能です。

詳しくは[追加Option](docs/options.md)をご覧ください。

---

## Planと料金

| Plan | 税込月額 | 月次Credit | 主な範囲 |
|---|---:|---:|---|
| Free | 0円 | 初回20,000／以後10,000 | 基本処理 |
| Basic | 980円 | 180,000 | 翻訳、外部転送、Private Mode、Storage |
| Pro | 2,980円 | 640,000 | 書類Template、Developer Mode・API |
| Business | 9,980円 | 2,200,000 | 上位利用枠、最大500GB Storage |
| Enterprise | 29,800円 | 6,600,000 | 最大利用枠、最大1TB Storage |

未登録では合計7,500 Credit、最大5回、1回最大1,500 Creditの試用範囲を設ける設計です。

追加Credit Pack、自由購入、Credit計算式、Storageの月次Creditは[Plan・料金・Credit](docs/plans-and-credits.md)にまとめています。

> 現在はCatalog内容の公開段階です。Astera Appの料金Pageと決済接続が公開されるまで、契約・購入可能とは案内していません。

---

## Developer Mode

Developer ModeはPro以上を対象とし、AsteraをApplicationや業務Systemから利用するための管理画面です。

主な対象：

- 判断材料生成API
- 根拠検索API
- 判定API
- Astera統合API
- Webhook Gateway接続

API Keyの発行、Rotate、Pause、Resume、削除、Usage、Credit、Rate、Quota、停止理由、Sandbox Explorerを一つの画面で管理する設計です。

現在は仕様と画面構成の公開段階で、実API Keyと公開Endpointは準備中です。詳しくは[Developer Mode](docs/developer-mode.md)をご覧ください。

---

## 基本Flow

```text
質問・相談・計画・AI回答を入力
  ↓
目的、Option、Template、保存方法を選ぶ
  ↓
予定Creditを確認
  ↓
Astera v8が8つの判断材料へ整理
  ↓
利用者が判断する
または
主役AIへ渡して文章・計画・Codeへ仕上げる
```

Astera v8は自由な文章生成を主目的にした生成AIではなく、決められた工程で判断材料を整理する中核Runtimeです。

---

## 現在の公開状態

現在このRepositoryで確認できるもの：

- Asteraの目的と8つの判断材料
- Astera v8の処理構造
- Astera Appの画面・操作・Option・Plan・Developer Mode仕様
- 公開Sample
- Support、Security、Contribution情報

現在、利用可能とは案内していないもの：

- Astera AppのProduction提供
- Account・認証の実運用
- Plan契約、Credit購入、決済
- File内容解析、Storage、Share
- Developer APIの実Endpoint
- Android／iOS Store版

詳細は[現在の公開状態](docs/current-status.md)をご覧ください。

---

## Documentation

- [Documentation案内](docs/README.md)
- [追加Option](docs/options.md)
- [Plan・料金・Credit](docs/plans-and-credits.md)
- [Developer Mode](docs/developer-mode.md)
- [Astera App Guide](docs/app-guide.md)
- [Asteraの仕組み](docs/how-it-works.md)
- [活用例](docs/use-cases.md)
- [FAQ](docs/faq.md)
- [現在の公開状態](docs/current-status.md)

---

## 開発者

Asteraは、**Seigo (`seigo-gace`) が個人で構想・設計・開発しているProject**です。

既存の生成AIを作り直すのではなく、人とAIが答えを出す前の「判断」を支える仕組みとして開発しています。

---

## English overview

**Astera structures questions, plans, and AI responses into decision material before a person or a primary AI produces a final answer.**

It organizes the real objective, missing assumptions, facts, risks, opposing views, comparable options, a recommended decision, and a refined instruction for a primary AI.

- [Options](docs/options.md)
- [Plans, pricing and credits](docs/plans-and-credits.md)
- [Developer Mode](docs/developer-mode.md)
- [Current status](docs/current-status.md)
