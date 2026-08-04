# Astera

> **問いを星図に変える。**

Asteraは、質問・相談・資料・計画・AIの回答を、**人が判断するために必要な材料へ整理する仕組み**です。

すぐに答えを作るのではなく、最初に「本当に達成したいこと」「足りない前提」「確認できる事実」「失敗した場合の危険」「反対側から見た問題」「比較できる別案」を整理します。

その上で、利用者自身が判断するか、ChatGPT、Claude、Gemini、自作AIなどの主役AIへ渡して、説明・計画・文章・コードなどの最終成果物へ仕上げます。

[公式サイト](https://asterav8.jp) ｜ [Astera App](https://app.asterav8.jp) ｜ [はじめかた](docs/getting-started.md) ｜ [Astera App完全ガイド](docs/app-guide.md) ｜ [公開サンプル](examples/README.md)

---

## Asteraを一言でいうと

**答えを急ぐ前に、判断の土台を作る仕組みです。**

たとえば、次の相談があるとします。

> 新しいサービスを来月までに公開したい。すぐ作り始めるべきか？

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
入力・目的選択・資料・Project・History・結果管理
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

Astera Appは、Asteraを日常的に利用するための操作画面です。

主な機能は次のとおりです。

- **新しい実行**：質問、相談、資料、AI回答などを入力する
- **目的選択**：自動、レビュー、比較、検証、改善、調査、計画、検討、判断、原因分析から選ぶ
- **資料と情報源**：FileやProjectに関連する情報を実行へ加える
- **Template**：レビュー、比較、計画、Risk確認などの入力補助を使う
- **結果表示**：8つの判断材料を決まった順番で読む
- **Turn管理**：一つの作業内で複数回の実行を移動して確認する
- **コピー・保存・共有**：項目単位または結果全体を再利用する
- **Project**：同じ目的の作業、資料、結果をまとめる
- **History**：過去の実行や結果を探し、再利用する
- **Settings**：表示、言語、Option、Template、Storage、Privacy、通知を管理する
- **Account**：Profile、Security、Plan、Credit、支払い状況を確認する
- **Developer Mode**：Asteraを外部Applicationや業務へ接続するための管理画面

詳しい画面構成と操作は[Astera App完全ガイド](docs/app-guide.md)をご覧ください。

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

## Astera Appでの基本的な流れ

1. **新しい実行を開く**
2. 質問、相談、資料の説明、確認したいAI回答などを入力する
3. 必要に応じて目的、File、Project情報、Template、Optionを追加する
4. 実行する
5. 8つの判断材料を読む
6. 不足情報を追加入力して、もう一度実行する
7. 結果をProjectやHistoryへ残す
8. 必要な項目をコピー、Download、共有する
9. 最終成果物が必要な場合は「主役AIへの再指示」を利用する

入力の書き方と画面操作は[はじめかた](docs/getting-started.md)、結果の読み方と管理は[Workspace・結果管理](docs/workspace-and-results.md)にまとめています。

---

## どんな場面で使えるのか

Asteraは、正解をすぐに決めにくい場面ほど役立ちます。

### 日常の判断

- 商品、サービス、住居、旅行先を比較する
- 転職、進路、独立などの選択肢を考える
- 人間関係で、事実と自分の推測を分ける
- 家族へ説明するために、自分の考えを整理する

### 仕事・事業

- 企画、事業計画、提案書をレビューする
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

詳しい例は[活用例](docs/use-cases.md)と[公開サンプル](examples/README.md)をご覧ください。

---

## Web・スマートフォン・Tablet

Astera Appは、同じ操作と情報をWeb Browser、スマートフォン、Tabletで扱える共通Applicationとして設計されています。

- PCではSidebarと広い結果表示を使う
- スマートフォンではHeaderとDrawerで画面を広く使う
- Tabletでは画面幅と向きに応じて配置を変える
- 縦向き・横向き、画面分割、Window Size変更へ追従する
- Touch操作では押しやすいButton Sizeと、入力中のKeyboard表示を考慮する
- Light／Dark、表示言語、動きを抑える設定を扱う

端末での考え方は[Mobile・Tablet・Accessibility](docs/mobile-and-accessibility.md)をご覧ください。

---

## Account・Security・Plan・Credit

Astera Appでは、実行画面だけでなく、継続利用に必要なAccount機能を一つの画面体系で扱います。

- Email登録とLogin
- Password再設定
- Google／GitHub Login後のAstera用Password設定
- Passkey
- 二段階認証
- Backup Code
- Login状態と接続Accountの確認
- PlanとSubscription
- Credit残高、購入、利用履歴
- 支払い処理後の状態確認
- Credit低下・停止に関する通知
- DataとPrivacyの設定

詳しくは[Account・Security・Plan・Credit](docs/account-security-and-billing.md)をご覧ください。

---

## Documentation

| Document | 内容 |
|---|---|
| [はじめかた](docs/getting-started.md) | 初回利用から結果の再利用まで |
| [Astera App完全ガイド](docs/app-guide.md) | 画面、機能、Navigation、操作 |
| [Astera AppとAstera v8](docs/app-and-runtime.md) | App・Runtime・主役AIの役割分担 |
| [Asteraの仕組み](docs/how-it-works.md) | 入力から8つの判断材料までの工程 |
| [Workspace・結果管理](docs/workspace-and-results.md) | Project、History、Turn、結果、共有 |
| [Account・Security・Plan・Credit](docs/account-security-and-billing.md) | Login、Security、契約、Credit |
| [Mobile・Tablet・Accessibility](docs/mobile-and-accessibility.md) | 端末、画面向き、操作性 |
| [活用例](docs/use-cases.md) | 日常、仕事、事業、開発での使い方 |
| [連携の考え方](docs/integrations.md) | 主役AI、外部Storage、APIとの関係 |
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

Astera consists of two main products:

- **Astera App** — the user-facing workspace for input, projects, history, results, sharing, account, security, plans, credits, and developer access
- **Astera v8** — the deterministic runtime that analyzes and structures decision material

Website: [asterav8.jp](https://asterav8.jp)