# Astera App画面一覧

Astera Appには、実行画面だけでなく、Project、History、Settings、Account、Security、Plan、Credit、Share、Developer Modeなどの専用画面があります。

このDocumentでは、**どの画面で何を行うのか**を一覧で確認できます。

利用者はURLを覚える必要はありません。PCではSidebar、SmartphoneではHeader MenuとDrawerから移動します。

---

## 画面構成

```text
Astera App
├─ 入口・公開情報
├─ Login・Account登録
├─ 実行・Result・Workspace
├─ Settings
├─ Account・Security・Billing
├─ Developer・Share
└─ System・Support
```

---

## 1. 入口・公開情報

| 画面 | Path | 役割 |
|---|---|---|
| Astera App入口 | `/` | Astera Appの入口。利用状態に応じて新しい実行やLoginへ進む |
| 料金・Plan | `/pricing` | Plan、料金、利用範囲を確認する |
| 公開Share | `/s/:token` | 共有用URLから公開されたResultを見る |
| 規約・法務入口 | `/legal` | 利用規約、Privacy、商取引表記、API規約への入口 |
| 利用規約 | `/legal/terms` | Astera利用条件を確認する |
| Privacy Policy | `/legal/privacy` | Dataと個人情報の扱いを確認する |
| 特定商取引法表記 | `/legal/commercial` | 販売者、料金、支払い、解約などの法定情報を確認する |
| API Terms | `/legal/api-terms` | Developer API利用条件を確認する |

---

## 2. Login・Account登録

| 画面 | Path | 役割 |
|---|---|---|
| Login | `/login` | Email／Password、外部ProviderなどでLoginする |
| Account登録 | `/register` | 新しいAstera Accountを登録する |
| Email確認 | `/verify-email` | 登録Emailの確認を完了する |
| Passwordを忘れた場合 | `/forgot-password` | Password再設定用の案内を受け取る |
| Password再設定 | `/reset-password` | 新しいPasswordを設定する |
| Astera用Password設定 | `/account/password/setup` | Google／GitHub等から登録した後にAstera専用Passwordを設定する |
| 二段階認証Challenge | `/auth/2fa` | Login時に認証Codeまたは復旧方法を確認する |

### Login後に元の画面へ戻る

Loginが必要な画面を開いた場合は、認証後に元の操作へ戻れるようにします。

例：

```text
Share管理を開く
  ↓
Loginが必要
  ↓
Login完了
  ↓
Share管理へ戻る
```

---

## 3. 実行・Result・Workspace

| 画面 | Path | 役割 |
|---|---|---|
| Astera App | `/app` | 利用者向けWorkspaceの入口 |
| 新しい実行 | `/app/new` | 入力、目的、File、Template、Optionを設定して実行する |
| Result詳細 | `/app/results/:id` | 入力条件と8つの判断材料を詳しく確認する |
| Project | `/app/projects` | 同じ目的の実行、資料、Resultをまとめる |
| History | `/app/history` | 過去の実行とResultを探す |
| Asteraについて | `/app/about` | Astera AppとAstera v8の役割を確認する |

### 新しい実行で行うこと

- 質問、相談、資料説明、AI回答を入力する
- 目的を選ぶ
- Fileを追加する
- Project情報を使う
- TemplateやOptionを選ぶ
- 実行する
- 処理を停止する
- 8つの判断材料を読む
- SectionまたはResult全体をコピーする
- Turn間を移動する

詳しくは[Astera App完全ガイド](app-guide.md)をご覧ください。

### Result詳細で確認すること

- 元の入力
- 選択した目的
- 使用したFile、Template、Option
- 実行日時
- Result状態
- 8つの判断材料
- Projectとの関係
- Share状態

### ProjectとHistoryの違い

- **Project**：同じ目的に関係する作業をまとめる
- **History**：過去の実行を時系列や条件で探す

詳しくは[Workspace・結果管理](workspace-and-results.md)をご覧ください。

---

## 4. Settings

| 画面 | Path | 役割 |
|---|---|---|
| Settings入口 | `/app/settings` | 各設定項目と現在状態を確認する |
| Option設定 | `/app/settings/options` | 追加機能と利用する選択肢を管理する |
| 表示・言語 | `/app/settings/language` | Theme、表示言語、表示方法を管理する |
| 個別Template管理 | `/app/settings/templates` | 繰り返し使う入力Templateを管理する |
| 外部Storage接続 | `/app/settings/storage-destinations` | 外部保存先の接続状態を管理する |
| Astera Storage | `/app/settings/astera-storage` | 容量、使用量、保存Fileを確認する |
| Data・Privacy | `/app/settings/data-privacy` | 保存、履歴、共有、外部接続のData設定を確認する |
| 通知・Credit警告 | `/app/settings/notifications` | 重要通知、低残高警告、任意通知を管理する |

### Settings入口

Settings入口では、利用可能な設定、現在の状態、Planによる利用範囲を確認します。

### 表示・言語

主な設定：

- 日本語／対応言語
- Light／Dark／System連動
- 全画面入力
- 動きを抑える設定

### Storage

外部StorageとAstera Storageは別の画面で管理します。

- 外部Storage接続：接続先と権限
- Astera Storage：Astera内の容量、File、残量

---

## 5. Account・Security・Billing

| 画面 | Path | 役割 |
|---|---|---|
| Account概要 | `/account` | Profile、Plan、Credit、Security状態をまとめて見る |
| Account Security | `/account/security` | Password、Passkey、2FA、Backup Code、接続Accountを管理する |
| Plan・Subscription | `/account/subscription` | 現在Plan、契約、更新、変更、解約を確認する |
| Credit購入・Ledger | `/account/credit` | Credit残高、購入、使用履歴、補填、通知を確認する |
| Checkout確認 | `/account/checkout` | 購入対象、金額、適用先を確認して決済へ進む |
| Billing Status | `/account/billing/status` | 決済完了、反映待ち、失敗、Cancel等を確認する |

### Account概要

最初に確認する場所です。

- Profile
- Email確認
- 現在のPlan
- Credit残高
- Security設定
- Billing状態

### Account Security

- Password変更
- Astera用Password設定
- Passkey登録・削除
- 二段階認証
- Backup Code
- Google／GitHub等の接続状態
- Session確認

### PlanとCredit

Planは利用可能な機能と契約範囲、Creditは実行やOption等の利用量を管理します。

詳しくは[Account・Security・Plan・Credit](account-security-and-billing.md)をご覧ください。

---

## 6. Developer Mode・Share

| 画面 | Path | 役割 |
|---|---|---|
| Developer Mode | `/app/developer` | API Key、使用量、Credit、停止状態、外部接続を管理する |
| Private Share | `/share/:id` | Loginや権限が必要な共有Resultを見る |
| Share管理 | `/app/shares` | 作成済みShare、期限、公開状態、停止を管理する |

### Developer Mode

Asteraを外部Applicationや業務Systemから利用するための管理画面です。

- API利用状態
- API Key
- 接続先
- 使用量
- Credit
- Error・停止理由
- API Terms

### Share管理

Public ShareとPrivate Shareを一覧で確認し、不要な共有を停止します。

共有前には、個人情報、契約情報、顧客情報、API Key、非公開File名が含まれていないか確認します。

---

## 7. System・Support

| 画面 | Path | 役割 |
|---|---|---|
| System Status | `/status` | Asteraの稼働状態と障害案内を確認する |
| Offline | `/offline` | Networkへ接続できない場合の案内を見る |
| Maintenance | `/maintenance` | Maintenance中の状態と案内を見る |
| Support | `/support` | 問い合わせ方法と自己確認項目を見る |
| Page Not Found | その他 | 存在しない画面で、正しい入口へ戻る |

### 実行できない場合

次の順で確認します。

1. Network
2. System Status
3. Account状態
4. Plan
5. Credit
6. 入力内容
7. Error Message
8. Support

---

## 利用目的から画面を探す

| やりたいこと | 開く画面 |
|---|---|
| 新しい相談を整理する | 新しい実行 |
| 前回のResultを見る | HistoryまたはResult詳細 |
| 同じテーマを続ける | Project |
| Resultを共有する | Share管理 |
| 言語やThemeを変える | 表示・言語 |
| Templateを作る | 個別Template管理 |
| File容量を確認する | Astera Storage |
| PasswordやPasskeyを変える | Account Security |
| Planを確認する | Plan・Subscription |
| Creditを購入する | Credit購入・Ledger |
| 決済反映を確認する | Billing Status |
| APIを管理する | Developer Mode |
| 障害を確認する | System Status |
| 問い合わせる | Support |

---

## 関連Document

- [Astera App完全ガイド](app-guide.md)
- [はじめかた](getting-started.md)
- [Workspace・結果管理](workspace-and-results.md)
- [Account・Security・Plan・Credit](account-security-and-billing.md)
- [Mobile・Tablet・Accessibility](mobile-and-accessibility.md)
