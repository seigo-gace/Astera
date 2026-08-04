# Account・Security・Plan・Credit

このDocumentは、Astera App Sourceに存在するAccount、Security、Plan、Credit、Billingの**画面構成と現在の接続状態**を説明します。

現在、これらを本番利用可能な機能として案内しているわけではありません。

最新の判定は[現在の公開状態](current-status.md)を正本とします。

---

## 現在の状態

| 領域 | Source状態 | 公開上の扱い |
|---|---|---|
| Account関連Route | Source実装済み | 画面構成として公開可能 |
| Login・登録画面 | Source実装済み | 認証Backend接続は未確認 |
| Password再設定 | Route・画面あり | Email送信・Token処理は未確認 |
| Passkey | 画面・設計あり | 登録・Login実動作は未確認 |
| 二段階認証 | Challenge Route・設計あり | 認証App連携は未確認 |
| Backup Code | 管理設計あり | 発行・消費・再生成は未確認 |
| Plan・Subscription | Route・画面あり | 契約Data連携は未確認 |
| Credit | Route・画面あり | Ledger・残高反映は未確認 |
| Checkout・Billing | Route・画面あり | 外部決済・反映処理は未確認 |

---

## 1. Account Route

現在のSourceには、次のRoute Patternがあります。

```text
/login
/register
/verify-email
/forgot-password
/reset-password
/account/password/setup
/auth/2fa
/account
/account/security
/account/subscription
/account/credit
/account/checkout
/account/billing/status
```

RouteがあることはSource実装として確認できます。

それぞれが実Data、Email、認証Provider、決済Providerと接続し、本番で利用できることは別の確認対象です。

---

## 2. 認証境界

Frontend Sourceは、認証が必要なRouteでAccount APIを確認し、未認証時にLoginへ移動する構成です。

設計上の方針：

- Cookieを含むSession確認
- Same Originの相対PathだけをReturn先として扱う
- MutationでCSRF情報を送る
- 必要な処理でIdempotency Keyを使う
- API Base未設定時は安全停止する
- API Errorを成功表示へ置き換えない

これらはFrontend側の境界実装です。

Session発行、Cookie属性、CSRF検証、Account API Response等のBackend実動作は未確認です。

---

## 3. EmailとPassword

Source上には、EmailとPasswordを使う次のFlowがあります。

1. Account登録
2. Email確認
3. Login
4. Password再設定
5. 必要に応じたAstera用Password設定

外部Loginを使う場合でも、GoogleやGitHubのPasswordをAsteraが取得・流用しない方針です。

現在公開できるのは、このFlowのRoute・画面・Frontend境界です。

Email配信、確認Token、Password Hash、Reset Token、Rate Limit等を含む本番認証は、接続確認後に公開判定します。

---

## 4. Passkey・二段階認証・Backup Code

Security画面の設計には次が含まれます。

- Passkey登録・削除
- 二段階認証設定
- Login時の二段階認証Challenge
- Backup Code
- 接続Login方法
- Session確認

現在は、これらの画面構成とRouteをSource実装範囲として公開します。

端末Authenticator、WebAuthn、TOTP、Backup Code発行・消費、Recovery Flowの実動作は、現在の公開実績には含めません。

---

## 5. Plan・Subscription

Plan・Subscription画面は、設計上次を扱います。

- 現在のPlan
- 契約期間
- 更新状態
- 利用範囲
- Storage容量
- Option
- Developer API範囲
- Plan変更
- 解約状態

現在はRoute・画面構成がSourceにあります。

実際のCatalog、契約Data、変更日、解約処理、Storage反映等は、Backend・決済接続確認前です。

---

## 6. Credit

Credit画面は、設計上次を扱います。

- 現在残高
- 購入候補
- 購入履歴
- 使用履歴
- 予約中Credit
- 返金・補填
- 低残高通知
- 実行停止状態

現在はRoute・画面構成をSource実装範囲として公開します。

Credit Ledger、原子的な増減、重複反映防止、返金・補填、枯渇時停止、補給後復帰等の実動作は、現在の公開実績には含めません。

---

## 7. Checkout・Billing Status

CheckoutとBilling StatusのRouteはSourceへ実装されています。

設計上のFlowは次のとおりです。

```text
購入内容確認
  ↓
外部決済
  ↓
Asteraへ戻る
  ↓
Billing Status確認
  ↓
PlanまたはCredit反映
```

Billing Statusでは、完了、反映待ち、失敗、Cancel、確認必要等を分ける設計です。

Square等の外部決済、Webhook、署名検証、Accountへの反映、重複防止、返金等は実接続確認前です。

そのため、現在は「決済画面がある」「購入できる」とは案内しません。

---

## 8. Data・Privacy

Data・Privacy画面のRoute・設計には、次の確認項目が含まれます。

- 入力・Result・File・Historyの保存
- 保存先
- 保存期間
- Share状態
- 外部Storage
- Data Download
- 削除
- Account退会時の扱い

現在、保存Backendや削除処理が本番で成立しているとは表記しません。

Privacy Policy、実Storage構成、保持期間、削除保証が確定・接続確認された後に、利用者向けの実運用手順へ更新します。

---

## 9. 現在公開できる説明

現在、外部へ正しく説明できる内容は次です。

- Account、Security、Plan、Credit、BillingのRouteと画面構成がSourceにある
- 認証必須RouteをFail-Closedで扱うFrontend方針がある
- Google／GitHubのProvider Passwordを取得・流用しない
- Account、決済、Credit等を別画面で確認できる構成を設計している
- API未接続・不整合時に成功扱いへ置き換えない

現在、外部へ利用可能機能として説明しない内容は次です。

- Account登録・Loginの本番稼働
- Passkey・二段階認証の本番稼働
- Plan契約・変更・解約
- Credit購入・利用・返金
- Checkout・Billing反映
- 外部決済・Webhook

---

## 関連Document

- [現在の公開状態](current-status.md)
- [Astera App Guide](app-guide.md)
- [App画面一覧](app-screen-map.md)
- [連携の考え方](integrations.md)
- [Security Policy](../SECURITY.md)
