# Astera AppとAstera v8

Asteraは、一つの大きなAIや一枚のChat画面ではありません。

利用者が操作する**Astera App**、判断材料を組み立てる**Astera v8**、最終成果物を作る**主役AI**を分けています。

この分離によって、「操作」「判断」「生成」を同じ処理へ混ぜず、それぞれの役割を明確にします。

---

## 全体像

```text
利用者
  ↓
Astera App
入力・目的・資料・Project・History・Result・Account
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

## 1. Astera Appの役割

Astera Appは、利用者がAsteraを継続して使うためのProductです。

単にTextを送信するだけではなく、判断に関係する情報をまとめ、結果を保存し、後から見直す場所として機能します。

### 入力と実行

- 質問、相談、資料の説明、AI回答を入力する
- 自動、レビュー、比較、検証、改善、調査、計画、検討、判断、原因分析から目的を選ぶ
- File、Project情報、Template、Optionを追加する
- 実行中の状態を確認する
- 必要な場合は処理を停止する

### Result

- 8つの判断材料を決まった順番で表示する
- 項目単位でコピーする
- Result全体をコピーする
- MarkdownとしてDownloadする
- 端末の共有機能を使う
- Result詳細で入力と条件を確認する

### Workspace

- Projectへ同じ目的の作業をまとめる
- Historyから過去の実行を探す
- Turnごとの判断変化を確認する
- Shareを作成・停止・管理する

### Settings

- Option
- 表示・言語
- 個別Template
- 外部Storage
- Astera Storage
- Data・Privacy
- 通知・Credit警告

### Account

- Profile
- Password、Passkey、二段階認証、Backup Code
- Plan・Subscription
- Credit購入と利用履歴
- CheckoutとBilling Status
- Developer Mode

詳しい画面説明は[Astera App完全ガイド](app-guide.md)をご覧ください。

---

## 2. Astera Appの画面構成

Astera Appでは、役割ごとに画面を分けます。

```text
Public
├─ 料金・Plan
├─ 公開Share
├─ 規約・Privacy
├─ System Status
└─ Support

認証
├─ Login
├─ Account登録
├─ Email確認
├─ Password再設定
├─ Astera用Password設定
└─ 二段階認証

利用画面
├─ 新しい実行
├─ Result詳細
├─ Project
├─ History
├─ Asteraについて
├─ Settings
└─ Share管理

Account
├─ Account概要
├─ Security
├─ Plan・Subscription
├─ Credit
├─ Checkout
└─ Billing Status

Developer
└─ Developer Mode
```

利用者は内部URLを覚える必要はありません。PCではSidebar、スマートフォンではDrawerから移動します。

---

## 3. Astera v8の役割

Astera v8は、入力を判断材料へ変換する中核Runtimeです。

自由な会話文を作ることよりも、**判断に必要な順番、分類、比較、再現性**を重視します。

### 目的を確認する

表面的な依頼と、本当に達成したい状態を分けます。

例：

```text
表面的な依頼：新しいSystemを導入したい
本当の目的：予約ミスを減らし、スタッフの作業時間を短くしたい
```

System導入そのものが目的ではない場合、現行Systemの改善や運用変更も比較案になります。

### 内容に合う視点を選ぶ

契約、健康、事業、開発、人間関係など、対象によって確認すべきRiskや前提は異なります。

Astera v8は、内容に合う視点を選び、共通の判断工程へ加えます。

### 事実と未確認情報を分ける

- 入力から確認できる事実
- 外部確認が必要な情報
- 利用者の意見
- 第三者の意見
- 推測

これらを混ぜずに扱います。

### Riskを確認する

成功方法だけでなく、失敗時の影響を確認します。

- 費用
- 時間
- 安全
- 信用
- 法令・契約
- 運用停止
- 戻しにくさ
- 関係者への影響

### 反対側から見直す

現在の案に賛成する材料だけではなく、慎重な立場、利用者と異なる立場、前提そのものを疑う立場から見直します。

### 別案を作る

「実行する・中止する」の二択に固定せず、次のような案を作ります。

- 条件を満たしてから進める
- 小さく試す
- 対象を限定する
- 一部だけ先に実行する
- 期限を変える
- 現行方法を改善する
- 失敗時に戻せる形で試す

### 同じ条件で比較する

候補ごとに別の基準を使わず、対象に合った共通条件で比較します。

例：

- 費用
- 効果
- 導入時間
- 操作性
- Security
- Support
- 失敗時の影響
- 元へ戻せるか

### 8つの判断材料へまとめる

途中で見つかった内容を、利用者と主役AIが読みやすい8項目へまとめます。

---

## 4. 主役AIの役割

主役AIは、Asteraの判断材料を使って最終成果物を作ります。

例：

- 分かりやすい説明
- 提案書
- 実行手順
- Project計画
- 会話文
- Email
- Code
- 調査報告
- 契約相手へ確認する質問

Astera v8が判断の骨組みを作り、主役AIは表現と具体化へ集中します。

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

```text
入力
  ↓
判断の品質を整える
  ↓
表現と成果物を作る
```

---

## 6. AppとRuntimeの情報の流れ

### 入力時

Astera Appから、入力、目的、File情報、Template、OptionなどをAstera v8へ渡します。

### 処理時

Astera v8は、目的、事実、不足、Risk、反対視点、比較案を組み立てます。

### Result時

Astera Appは、受け取った内容を8つのSectionとして表示します。

### 保存時

利用者は、ResultをProject、History、Download、Share、主役AIへの再利用へつなげます。

---

## 7. 具体例

利用者が次のように入力したとします。

> 現在の仕事を辞めて独立した方がよいですか？

### Astera App

- 相談を入力する
- 「検討」と「判断」を選ぶ
- 必要なら収支表や事業計画を追加する
- ResultをProjectへ残す

### Astera v8

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

Asteraの判断材料を使い、月ごとの準備計画、確認表、家族への説明文、顧客獲得手順などへ仕上げます。

---

## 8. Web・Mobile・Tabletとの関係

Astera Appは、端末ごとに別の判断処理を使いません。

画面配置は変わっても、入力、Project、History、Result、Accountの意味は共通です。

- PC：Sidebarと広いResult表示
- Smartphone：Header、Drawer、Touch操作
- Tablet：画面幅、向き、分割表示へ追従
- Native App：OS共有、Deep Link、Keyboard、Back操作と連携

詳しくは[Mobile・Tablet・Accessibility](mobile-and-accessibility.md)をご覧ください。

---

## 9. 役割のまとめ

| 要素 | 主な役割 | 行わないこと |
|---|---|---|
| 利用者 | 目的、希望、事実提供、最終決定 | 判断を完全に他者へ渡すこと |
| Astera App | 入力、Workspace、Result、Accountの操作 | 判断Algorithmそのもの |
| Astera v8 | 判断材料の分解、確認、比較、構造化 | 自由な最終文章の生成を主目的にすること |
| 主役AI | 説明、計画、文章、Codeへの具体化 | 不足前提を確認せず勝手に確定すること |

Asteraが目指すのは、主役AIを弱く制限することではありません。

**主役AIが具体化へ集中できるように、判断の土台を先に整えること**です。

---

## 関連Document

- [Astera App完全ガイド](app-guide.md)
- [Asteraの仕組み](how-it-works.md)
- [Workspace・結果管理](workspace-and-results.md)
- [連携の考え方](integrations.md)
