# Astera AppとAstera v8

Asteraは、一つの大きなAIや一枚のChat画面ではありません。

利用者が操作する**Astera App**、判断材料を組み立てる**Astera v8**、最終成果物を作る**主役AI**を分けています。

このDocumentでは、役割分担と現在の公開状態を説明します。

最新の実装・接続判定は[現在の公開状態](current-status.md)を正本とします。

---

## 全体像

```text
利用者
  ↓
Astera App
入力・目的・Result表示・Workspace操作
  ↓
Astera v8
問いを分解し、事実・Risk・反対視点・比較案を整理
  ↓
8つの判断材料
  ↓
利用者 または 主役AI
判断・説明・計画・文章・Code・成果物
```

Asteraの中心にいるのは利用者です。

Astera v8も主役AIも、利用者の目的、条件、最終決定を置き換えるものではありません。

---

## 現在の公開状態

| 要素 | 現在公開できる内容 | 現在の公開実績に含めない内容 |
|---|---|---|
| Astera App | Route、画面構成、Frontend処理、Responsive Source | Production、Backend、認証、決済、Storage、実機 |
| Astera v8 | 役割、8つの判断材料、処理構造、Use Case、Sample | 未確認の実環境接続を完成扱いすること |
| 主役AI連携 | ResultをCopyして別AIへ渡す利用方法 | Developer APIによる自動連携 |

---

## 1. Astera Appの役割

Astera Appは、Asteraを利用するためのFrontendです。

現在のSource実装には次が含まれます。

### Inputと実行UI

- 質問、相談、資料の説明、AI回答を入力する
- 10種類の目的を選ぶ
- File Metadata、Project情報UI、Template、追加Optionを設定する
- 処理段階を表示する
- Responseを8 SectionへMappingする

Backend EndpointとResponse Schemaを含むProduction実行は確認前です。

### Result

- 8つの判断材料をSection表示する
- Section単位でCopyする
- Result全体をCopyする
- Markdownを生成する
- 端末共有へ渡す
- Turn間を移動する

これらはFrontend Source実装範囲です。

### Workspace

- Project Route
- History Route
- Result詳細Route
- Public／Private Share Route
- Share管理Route

画面経路はSourceへ実装されています。Server保存、検索、同期、Share Token、認可等は接続確認前です。

### Settings

- Option
- 表示・言語
- Template
- 外部Storage
- Astera Storage
- Data・Privacy
- 通知・Credit警告

Theme等のFrontend設定と、Storage・通知・Credit等の外部接続を同一扱いしません。

### Account

- Login・登録・Email確認・Password再設定
- Account概要・Security
- Plan・Subscription
- Credit
- Checkout・Billing Status
- Developer Mode

Routeと画面構成はSource実装済みです。認証、決済、Credit、API提供の実動作は確認前です。

詳しくは[Astera App Guide](app-guide.md)をご覧ください。

---

## 2. Astera Appの43 Route Pattern

現在のSourceでは、次の領域を43 Route Patternへ分けています。

```text
Public
├─ Pricing
├─ Public Share
├─ Legal
├─ Status
├─ Offline
├─ Maintenance
└─ Support

Auth
├─ Login
├─ Register
├─ Email Verification
├─ Password Reset
├─ Astera Password Setup
└─ 2FA Challenge

App
├─ New Run
├─ Result Detail
├─ Projects
├─ History
├─ Settings
├─ Developer Mode
└─ Share Management

Account
├─ Account Overview
├─ Security
├─ Subscription
├─ Credit
├─ Checkout
└─ Billing Status
```

Route一覧と状態は[App画面・Route一覧](app-screen-map.md)にあります。

---

## 3. Astera v8の役割

Astera v8は、入力を判断材料へ変換する中核Runtimeです。

自由な会話文を作ることよりも、**判断に必要な順番、分類、比較、再現性**を重視します。

### 目的を確認する

表面的な依頼と、本当に達成したい状態を分けます。

```text
表面的な依頼：新しいSystemを導入したい
本当の目的：予約ミスを減らし、Staffの作業時間を短くしたい
```

### 内容に合う視点を選ぶ

契約、健康、事業、開発、人間関係等、対象によって確認すべきRiskや前提は異なります。

### 事実と未確認情報を分ける

- 入力から確認できる事実
- 外部確認が必要な情報
- 利用者の意見
- 第三者の意見
- 推測

### Riskを確認する

- 費用
- 時間
- 安全
- 信用
- 法令・契約
- 運用停止
- 戻しにくさ
- 関係者への影響

### 反対側から見直す

賛成材料だけでなく、慎重な立場、異なる立場、前提を疑う立場から見直します。

### 別案を作る

「実行する・中止する」の二択だけでなく、条件付き実行、小規模試験、対象限定、延期、現行改善等を比較します。

### 同じ条件で比較する

候補ごとに別の基準を使わず、共通条件で比較します。

### 8つの判断材料へまとめる

1. 本当の目的
2. 前提不足
3. 事実確認
4. 危機察知
5. 反対視点
6. 比較案
7. 推奨判断
8. 主役AIへの再指示

詳しくは[Asteraの仕組み](how-it-works.md)をご覧ください。

---

## 4. 主役AIの役割

主役AIは、Asteraの判断材料を使って最終成果物を作ります。

例：

- 分かりやすい説明
- 提案書
- 実行手順
- Project計画
- Email
- Code
- 調査報告
- 契約相手へ確認する質問

Astera v8が判断の骨組みを作り、主役AIは表現と具体化へ集中します。

現在公開できる連携方法は、ResultをCopyし、必要なSectionと再指示を主役AIへ渡すFlowです。

APIによる自動連携は現在の公開実績に含めません。

---

## 5. なぜ役割を分けるのか

判断と文章生成を一度に行うと、文章の自然さが優先され、次の問題が見えにくくなる場合があります。

- 入力に必要な前提がない
- 利用者の希望を事実として扱う
- 一案だけで進める
- 根拠がない部分を一般論で埋める
- Riskや停止条件が後回しになる
- 読みやすいが実行できない回答になる

Asteraは先に判断の骨組みを作り、主役AIが後から成果物へ仕上げます。

---

## 6. AppとRuntimeの情報Flow

### Frontend Sourceで確認できるFlow

```text
Input・Purpose・Template・Option・File Metadata
  ↓
API Payload作成
  ↓
Processing表示
  ↓
Response受領
  ↓
8 SectionへMapping
  ↓
Turn・Copy・Markdown・端末共有
```

### 現在確認前のFlow

- Production Backendへの実接続
- File本体Upload・解析
- Project・History保存
- Share発行
- Account・認証
- Plan・Credit・決済
- Developer API

---

## 7. 具体例

利用者が次のように入力したとします。

> 現在の仕事を辞めて独立した方がよいですか？

### Astera App Source上の操作

- 相談を入力する
- 「検討」と「判断」を選ぶ
- Resultを8 Sectionへ表示する
- 必要なSectionをCopyする

### Astera v8が整理する判断材料

- 独立したい本当の理由
- 現在の収入と必要生活費
- 顧客と売上見込み
- 健康、家族、契約への影響
- 今すぐ退職する案
- 副業から始める案
- 期限を決めて準備する案
- 売上や貯蓄の開始条件
- 中止・延期条件

### 主役AI

Asteraの判断材料を使い、月ごとの準備計画、確認表、家族への説明文、顧客獲得手順等へ仕上げます。

具体的なSampleは[公開Sample](../examples/README.md)にあります。

---

## 8. Web・Mobile・Tablet

共通Frontend Sourceには、Desktop、Smartphone、Tablet向けのResponsive Shellがあります。

- Desktop：Sidebarと広いResult表示
- Smartphone：Header、Drawer、Touch対応
- Tablet：画面幅、向き、分割表示を想定
- Native Shell：Android／iOS設定とWorkflow

実端末・Native Build・Store公開は現在の公開実績に含めません。

詳細は[Mobile・Tablet・Accessibility](mobile-and-accessibility.md)をご覧ください。

---

## 9. 役割のまとめ

| 要素 | 主な役割 | 現在公開できる状態 |
|---|---|---|
| 利用者 | 目的、希望、事実提供、最終決定 | Conceptとして公開済み |
| Astera App | Input、Result、Workspace、AccountのFrontend | Source実装範囲を公開 |
| Astera v8 | 判断材料の分解、確認、比較、構造化 | 処理構造・Sampleを公開 |
| 主役AI | 説明、計画、文章、Codeへの具体化 | Copy利用Flowを公開 |

Asteraが目指すのは、主役AIを弱く制限することではありません。

**主役AIが具体化へ集中できるように、判断の土台を先に整えること**です。
