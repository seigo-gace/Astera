# Account・Security・Plan・Credit

Astera Appでは、Account情報、Login方法、Security、Plan、Credit、決済状態を分けて管理します。

料金とCreditの具体値は[Plan・料金・Credit](plans-and-credits.md)、現在の提供状態は[現在の公開状態](current-status.md)をご覧ください。

---

## Account画面

Account概要では次を確認する構成です。

- Profile
- Email確認状態
- Account状態
- Current Plan
- 利用可能Creditと予約中Credit
- Security設定
- Login方法
- Billing状態
- Developer API利用資格

問題がある場合は、実行画面で原因不明のErrorにせず、Account側で理由と必要なActionを確認します。

---

## LoginとAccount登録

対応するLogin方法の設計：

- Email＋Password
- Google
- GitHub
- Passkey

GoogleやGitHubで登録した場合でも、ProviderのPasswordをAsteraが取得・流用することはありません。必要に応じてAstera専用Passwordを設定します。

### 基本Flow

```text
Account登録
↓
Email確認
↓
Login
↓
必要に応じてPassword・Passkey・2FAを設定
```

Loginが必要な画面を開いた場合は、認証後に元の画面へ戻る構成です。

---

## Password

- 12〜128文字
- Password変更
- Passwordを忘れた場合の再設定
- 外部Login後のAstera専用Password設定

重要な操作では、一定時間以内の再認証を要求する設計です。

---

## Passkey

Passkeyは任意で利用します。

- 複数端末へ登録
- 分かりやすい名称を付ける
- 最終利用を確認
- 個別に削除

端末を失った場合に備え、別のLogin方法も確保します。

---

## 二段階認証とBackup Code

二段階認証はAuthenticator Appを使う設計です。

設定時にBackup Codeを発行し、安全な場所へ保存します。

- 認証CodeやBackup Codeを他人へ送らない
- 使用後や紛失時は再生成する
- Public Issueへ書かない

SMS、電話、Email OTPは初期範囲に含めません。

---

## Sessionと接続Account

Security画面では次を管理します。

- Login中の端末・Session
- Google／GitHub等の接続方法
- 不明なSessionの終了
- Password、Passkey、2FAの状態

接続Accountを解除する前に、別のLogin方法が残っていることを確認します。

---

## Plan・Subscription

Plan画面では次を確認します。

- Current Plan
- 税込月額
- 月次Credit
- 利用可能なOptionと機能
- Astera Storage上限
- Developer Mode利用資格
- 更新・変更・解約状態

現在のPlan：

| Plan | 税込月額 | 月次Credit |
|---|---:|---:|
| Free | 0円 | 初回20,000／以後10,000 |
| Basic | 980円 | 180,000 |
| Pro | 2,980円 | 640,000 |
| Business | 9,980円 | 2,200,000 |
| Enterprise | 29,800円 | 6,600,000 |

Planごとの詳しい機能は[Plan・料金・Credit](plans-and-credits.md)をご覧ください。

---

## Credit画面

Credit画面では次を確認する構成です。

- 利用可能残高
- 実行のための予約残高
- 概算の残り実行回数
- 固定Packと自由購入
- 使用・購入・返却・補填の履歴
- 低残高・不足・反映待ち等の状態
- 通知設定
- Credit不足で停止しているDeveloper API Key

### Creditが不足した場合

処理開始前に不足を判定した場合、その実行は開始せずCreditも消費しません。

表示する内容：

- 現在残高
- 予定Credit
- 正確な不足量
- Creditを追加
- 元の入力へ戻る
- Optionや入力を減らす

購入後も元の実行を自動開始しません。再見積り後に利用者が実行します。

---

## CheckoutとBilling Status

```text
購入内容を確認
↓
外部決済
↓
Asteraへ戻る
↓
Billing Statusを確認
↓
PlanまたはCreditへ反映
```

決済画面から戻っただけでは反映済みとしません。

- 支払確認中
- Credit／Plan反映待ち
- 完了
- 失敗・取消
- 確認が必要

を分けて表示します。

---

## 通知

### 重要通知

- Credit不足による実行停止
- 支払い失敗
- Security設定の変更
- 不審なLogin
- Account状態の変更
- Developer APIの停止・再開

### 任意通知

- Credit低下予告
- 利用状況
- 更新案内
- Email／Push

App内の重要表示を、EmailやPushだけに依存させません。

---

## Data・Privacy

Data・Privacy画面では次を確認します。

- 何を保存するか
- 保存先と期間
- HistoryとShare
- Astera Storageと外部Storage
- Data Downloadと削除
- Account退会時の扱い
- Private Mode

Private Modeでは、通常のHistoryやAstera Storageへ本文・File・結果を保存しない設計です。

---

## 困ったとき

| 状況 | 確認する場所 |
|---|---|
| Loginできない | Email確認、Password再設定、2FA、Backup Code |
| Planが違う | Plan・Subscription、Billing Status |
| Creditが反映されない | Billing Status、Credit履歴 |
| 実行が停止した | Credit残高、予定Credit、Account状態 |
| APIが停止した | Developer Modeの停止理由 |
| 不審なLoginがある | Security、Session、Password、Passkey |

秘密情報や決済情報はPublic Issueへ書かず、[Support](../SUPPORT.md)を利用してください。

---

## 関連Document

- [Plan・料金・Credit](plans-and-credits.md)
- [追加Option](options.md)
- [Developer Mode](developer-mode.md)
- [Astera App Guide](app-guide.md)
- [Security Policy](../SECURITY.md)
- [現在の公開状態](current-status.md)
