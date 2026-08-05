# Astera Appの画面案内

このページでは、やりたいことから開く画面を探せます。

現在の提供状態は[現在の公開状態](current-status.md)をご覧ください。

---

## よく使う画面

| やりたいこと | 画面 | Path |
|---|---|---|
| 新しい相談・比較・検証を始める | 新しい実行 | `/app/new` |
| 前回のResultを見る | Result詳細 | `/app/results/:id` |
| 同じテーマをまとめる | Project | `/app/projects` |
| 過去の実行を探す | History | `/app/history` |
| Optionを表示・非表示にする | Option設定 | `/app/settings/options` |
| 表示言語やThemeを変える | 表示・言語 | `/app/settings/language` |
| Templateを管理する | 個別Template | `/app/settings/templates` |
| Storage接続を管理する | 外部Storage接続 | `/app/settings/storage-destinations` |
| Astera Storageを確認する | Astera Storage | `/app/settings/astera-storage` |
| 通知とCredit警告を設定する | 通知・Credit警告 | `/app/settings/notifications` |
| Planを確認・変更する | Plan・Subscription | `/account/subscription` |
| Credit残高・履歴を見る | Credit | `/account/credit` |
| PasswordやPasskeyを管理する | Account Security | `/account/security` |
| API Keyを管理する | Developer Mode | `/app/developer` |
| Resultを共有する | Share管理 | `/app/shares` |
| 障害情報を見る | System Status | `/status` |

---

## 新しい実行

`/app/new`はAstera Appの中心画面です。

ここで次を行います。

- 入力
- 目的選択
- 4つの追加Option
- Template
- File
- Private Mode
- 保存・転送先
- 予定Credit確認
- 実行
- 8つの判断材料の確認
- Turn移動
- Copy・Markdown Download・端末共有

追加Optionは[追加Option](options.md)、操作順は[はじめかた](getting-started.md)をご覧ください。

---

## Result・Project・History

### Result詳細 `/app/results/:id`

元の入力、選択した目的・Option・Template、8つの判断材料、関連Project、Share状態を確認します。

### Project `/app/projects`

同じ目的の実行、File、Result、判断変更をまとめます。

### History `/app/history`

過去の実行を日時、目的、Project、状態などから探します。

詳細は[Workspace・結果管理](workspace-and-results.md)をご覧ください。

---

## Settings

### Settings入口 `/app/settings`

利用できる設定とLocked理由を一覧で確認します。

### Option設定 `/app/settings/options`

Composerに表示するOption候補を管理します。

- 高精度翻訳
- エージェントモード
- 書類作成
- 外部Storage転送

ToggleをONにしただけでは実行・課金されません。

### 表示・言語 `/app/settings/language`

- 表示言語
- Light／Dark／System
- 全画面入力
- Reduced Motion

### 個別Template `/app/settings/templates`

書類作成などで繰り返し使うTemplateを作成・編集・Preview・複製・無効化します。

### 外部Storage接続 `/app/settings/storage-destinations`

利用者が管理するStorage Account、保存先Folder、接続状態を管理します。

### Astera Storage `/app/settings/astera-storage`

契約容量、使用量、残量、保存File、次回Credit減算を確認します。

### Data・Privacy `/app/settings/data-privacy`

保存、History、Share、外部接続、Private Mode、Data Download・削除を確認します。

### 通知・Credit警告 `/app/settings/notifications`

低残高、Credit不足、支払い、Security、API停止・再開などの通知を管理します。

---

## Account・Security・料金

### Account概要 `/account`

Profile、Current Plan、Credit、Security状態、Billing状態をまとめて確認します。

### Account Security `/account/security`

Password、Passkey、二段階認証、Backup Code、接続Account、Sessionを管理します。

### Plan・Subscription `/account/subscription`

Current Plan、月額、月次Credit、機能、Storage上限、更新・変更・解約状態を確認します。

### Credit `/account/credit`

利用可能・予約中Credit、概算残り回数、Pack、自由購入、Ledger、通知、API停止状態を確認します。

### Checkout `/account/checkout`

購入対象、金額、付与Credit、適用先、契約条件を確認して外部決済へ進みます。

### Billing Status `/account/billing/status`

支払確認中、反映待ち、完了、失敗、取消などを確認します。

料金とCreditは[Plan・料金・Credit](plans-and-credits.md)をご覧ください。

---

## Developer Mode `/app/developer`

Pro以上を対象とした開発者向け画面です。

- API一覧
- Sandbox／Production Key
- Scope
- Rotate、Pause、Resume、削除
- Usage、Credit、Rate、Quota
- 停止理由と履歴
- OpenAPIとSample
- Sandbox Explorer

詳しくは[Developer Mode](developer-mode.md)をご覧ください。

---

## Share

### Public Share `/s/:token`

共有URLから公開可能なResultを表示します。

### Private Share `/share/:id`

指定されたAstera AccountだけがResultを確認します。

### Share管理 `/app/shares`

Shareの種類、期限、Download、Password、公開状態、停止を管理します。

Private Modeの本文はShareできません。

---

## Login・Account登録

| 画面 | Path |
|---|---|
| Login | `/login` |
| Account登録 | `/register` |
| Email確認 | `/verify-email` |
| Password再設定要求 | `/forgot-password` |
| Password再設定 | `/reset-password` |
| Astera用Password設定 | `/account/password/setup` |
| 二段階認証 | `/auth/2fa` |

Loginが必要な画面を先に開いた場合は、Login後に元の画面へ戻る構成です。

---

## 公開情報・Support

| 画面 | Path |
|---|---|
| 料金・Plan | `/pricing` |
| Asteraについて | `/app/about` |
| 利用規約・Privacy等 | `/legal/*` |
| System Status | `/status` |
| Offline案内 | `/offline` |
| Maintenance | `/maintenance` |
| Support | `/support` |

---

## 迷ったとき

- 何を入力すればよいか → [はじめかた](getting-started.md)
- Optionを選べない → [追加Option](options.md)
- PlanとCreditを知りたい → [Plan・料金・Credit](plans-and-credits.md)
- APIを使いたい → [Developer Mode](developer-mode.md)
- App全体を知りたい → [Astera App Guide](app-guide.md)
- 現在使える範囲を知りたい → [現在の公開状態](current-status.md)
