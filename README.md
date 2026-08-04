# Astera

> **問いを星図に変える。**

Asteraは、質問・相談・資料・計画・AIの回答を、**人が判断するために必要な材料へ整理する仕組み**です。

すぐに答えを作るのではなく、最初に「本当に達成したいこと」「足りない前提」「確認できる事実」「失敗した場合の危険」「反対側から見た問題」「比較できる別案」を整理します。

その上で、利用者自身が判断するか、ChatGPT、Claude、Gemini、自作AIなどの主役AIへ渡して、説明・計画・文章・Codeなどの最終成果物へ仕上げます。

[現在の公開状態](docs/current-status.md) ｜ [Documentation](docs/README.md) ｜ [公開Sample](examples/README.md) ｜ [公式Site](https://asterav8.jp)

---

## 現在このRepositoryで公開している範囲

このPublic Repositoryは、**Asteraの構想だけを置いた予告Pageではありません**。

現在完成している説明、処理構造、App Sourceの実装範囲、公開Sample、Support・Security情報を、外部から確認できる形で公開しています。

| 領域 | 現在の公開状態 |
|---|---|
| Asteraの目的と役割 | 公開済み |
| 8つの判断材料 | 公開済み |
| Astera v8の処理構造 | 公開説明済み |
| Use Caseと入出力Sample | 公開済み |
| Appの43 Route PatternとFrontend Source構成 | Source実装範囲として公開説明済み |
| Documentation、Support、Security、Contribution情報 | 公開済み |
| Production Web、Backend、Account、決済、Native実機 | 確認完了まで利用可能機能としては案内しない |

仕様があること、Sourceへ実装されていること、Productionで利用できることは同じではありません。

詳細は[現在の公開状態](docs/current-status.md)にまとめています。

---

## Asteraを一言でいうと

**答えを急ぐ前に、判断の土台を作る仕組みです。**

たとえば、次の相談があるとします。

> 新しいServiceを来月までに公開したい。すぐ作り始めるべきか？

一般的な回答は、開発手順やおすすめの進め方から始まりがちです。

Asteraは、その前に次を確認します。

- 公開そのものが目的なのか、利用者を増やすことが目的なのか
- 来月でなければならない理由はあるか
- 誰が使うのか
- どの状態を「公開できる完成」と呼ぶのか
- 問い合わせ、障害、返金、個人情報への対応は準備されているか
- 全機能を一度に出さず、範囲を限定して試せないか
- どの条件になったら延期・中止・切り戻しを行うか

これにより、勢いや思い込みだけで進めるのではなく、**何を確認し、どの案を比べ、どの条件で決めるのか**が見えるようになります。

---

## Asteraが整理する8つの判断材料

| 番号 | 判断材料 | 何が分かるか |
|---:|---|---|
| 01 | 本当の目的 | 表面的な質問の奥で、本当に達成したいこと |
| 02 | 前提不足 | 判断する前に確認しなければならない条件 |
| 03 | 事実確認 | 分かっていること、未確認のこと、推測 |
| 04 | 危機察知 | 失敗、損失、安全、信用、運用上の危険 |
| 05 | 反対視点 | 見落としている反論、別の立場、逆の可能性 |
| 06 | 比較案 | 同じ条件で比べられる複数の選択肢 |
| 07 | 推奨判断 | 現時点で妥当な方向と、成立条件・停止条件 |
| 08 | 主役AIへの再指示 | AIへ渡す、具体的で抜けの少ない依頼文 |

Asteraは、一つの結論を押しつけるものではありません。

**なぜその判断になるのか、何が変われば判断も変わるのか**を、利用者が理解できる形にします。

---

## Asteraを構成する2つのProduct

```text
利用者
  ↓
Astera App
入力・目的選択・Result表示・Workspace操作
  ↓
Astera v8
問いを分解し、複数の視点と案を比較する
  ↓
8つの判断材料
  ↓
利用者 または 主役AI
最終判断・説明・計画・成果物
```

### Astera App

Astera Appは、Asteraを利用するためのFrontendです。

現在のSource実装には、次が含まれます。

- 新しい実行画面
- 自動、Review、比較、検証、改善、調査、計画、検討、判断、原因分析の目的選択
- Templateと追加Optionの選択UI
- 処理段階の表示
- 8つの判断材料へのResult Mapping
- Turn移動
- Section単位とResult全体のCopy
- Markdown Download
- 端末共有
- Project、History、Settings、Account、Security、Plan、Credit、Developer、Share、Legal、Status、Supportを含む43 Route Pattern
- Desktop、Smartphone、Tablet向けResponsive Shell
- Android／iOS Native Shell用の設定とWorkflow

ただし、Routeや画面がSourceへ存在することを、Backend・認証・決済・Storage・実機を含む本番稼働済みとは表記しません。

File機能も、現在のFrontend Sourceでは名称・Size・TypeなどのMetadataをPayloadへ含める段階であり、File本体のUploadと内容解析は現在の公開実績に含めません。

詳しくは[Astera App Guide](docs/app-guide.md)と[現在の公開状態](docs/current-status.md)をご覧ください。

### Astera v8

Astera v8は、入力された内容を決められた工程で分解・比較し、8つの判断材料へ組み立てる中核Runtimeです。

Astera v8は、自由に文章を作る生成AIそのものではありません。

- 入力の目的と構造を確認する
- 内容に合う視点を選ぶ
- 事実、未確認情報、推測を分ける
- 危険と失敗条件を調べる
- 賛成側、慎重側、前提を疑う側から見直す
- 二択以外の案を作る
- 同じ条件で案を比較する
- 判断材料と主役AIへの再指示へまとめる

詳しくは[Asteraの仕組み](docs/how-it-works.md)をご覧ください。

---

## 現在のApp Sourceで確認できる基本Flow

1. 新しい実行画面で内容を入力する
2. 必要に応じて目的、Template、Optionを選択する
3. Frontendから実行Payloadを作る
4. 処理段階を表示する
5. Responseを8つの判断材料へ割り当てる
6. Turnを移動する
7. ResultのSectionまたは全体をCopyする
8. Markdownとして保存する
9. 端末の共有機能へ渡す

Backend EndpointとResponse Schemaを含むProduction動作は、実接続確認が終わるまで現在利用可能とは案内しません。

---

## どんな場面で使うのか

Asteraは、正解をすぐに決めにくい場面ほど役立ちます。

### 日常の判断

- 商品、Service、住居、旅行先を比較する
- 転職、進路、独立などの選択肢を考える
- 人間関係で、事実と自分の推測を分ける
- 家族へ説明するために、自分の考えを整理する

### 仕事・事業

- 企画、事業計画、提案書をReviewする
- 契約や発注条件の確認項目を整理する
- 新規公開、料金変更、業務変更の危険を確認する
- 複数部署・複数人の意見を同じ条件で比較する

### 開発・運用

- 技術選択やArchitecture案を比較する
- 障害原因を一つに決めつけず、確認順を作る
- 実装計画の依存関係、失敗条件、切り戻し条件を整理する
- AIが作ったCodeや改善案の前提を確認する

### AI回答の品質確認

- AI回答の中に、根拠のない断定がないかを見る
- 最新情報を調べる必要がある箇所を見つける
- 反対意見や重大Riskが抜けていないか確認する
- より良い再質問・再指示を作る

詳しい例は[活用例](docs/use-cases.md)と[公開Sample](examples/README.md)をご覧ください。

---

## Documentation

| Document | 内容 |
|---|---|
| [現在の公開状態](docs/current-status.md) | 公開済み、Source実装、実稼働未確認の区分 |
| [Documentation案内](docs/README.md) | 目的別の読み順 |
| [Asteraのはじめかた](docs/getting-started.md) | 現在のSourceに沿った操作Flow |
| [Astera App Guide](docs/app-guide.md) | 画面、機能、Navigation、現在の接続状態 |
| [Astera AppとAstera v8](docs/app-and-runtime.md) | App・Runtime・主役AIの役割分担 |
| [Asteraの仕組み](docs/how-it-works.md) | 入力から8つの判断材料までの工程 |
| [Workspace・結果管理](docs/workspace-and-results.md) | Project、History、Turn、Result、Shareの設計 |
| [Account・Security・Plan・Credit](docs/account-security-and-billing.md) | Account関連画面と現在の実装状態 |
| [Mobile・Tablet・Accessibility](docs/mobile-and-accessibility.md) | Source対応と実機確認状態 |
| [活用例](docs/use-cases.md) | 日常、仕事、事業、開発での使い方 |
| [連携の考え方](docs/integrations.md) | 主役AI、File、Storage、APIとの関係 |
| [よくある質問](docs/faq.md) | AsteraとAppに関するFAQ |
| [Press Kit](docs/press-kit.md) | 紹介・記事・資料向けの基本情報 |

---

## 開発者

Asteraは、**Seigo (`seigo-gace`) が個人で構想・設計・開発しているProject**です。

既存の生成AIを作り直すのではなく、人とAIが答えを出す前の「判断」を支える仕組みとして開発しています。

---

## English overview

**Astera turns questions, plans, documents, and AI responses into structured decision material before a person or a primary AI produces a final answer.**

It organizes the real objective, missing assumptions, known and unknown facts, risks, opposing views, comparable options, a recommended decision, and a refined instruction for a primary AI.

This public repository currently publishes the product concept, the eight-part decision structure, architecture documentation, public examples, and the verified scope of the Astera App frontend source.

Frontend routes or screens are not presented as production-ready services until backend, authentication, billing, storage, deployment, and device verification are complete.

- [Current public status](docs/current-status.md)
- [Documentation](docs/README.md)
- [Public examples](examples/README.md)
