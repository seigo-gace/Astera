# Account・Security・Plan・Credit

Astera Appは、実行画面だけでなく、継続利用に必要なAccount、Security、Plan、Credit、Billingを一つの画面体系で扱います。

このDocumentでは、それぞれの役割を利用者向けに説明します。

---

## 1. Account概要

Account画面では、現在の利用状態をまとめて確認します。

主な確認項目：

- Profile
- Email確認状態
- Account状態
- 現在のPlan
- Credit残高
- Security設定
- 接続中のLogin方法
- Billing状態
- 利用可能な機能

Account情報に問題がある場合は、実行画面で原因不明のErrorとして扱わず、Account側で状態を確認できるようにします。

---

## 2. Loginと登録

Astera Appでは、EmailとPasswordによる登録・Loginを基本とし、GoogleやGitHubなどの外部Loginも利用できる構成です。

### Email登録

一般的な流れ：

1. EmailとPasswordを登録する
2. 確認Emailを受け取る
3. Email確認を完了する
4. Astera AppへLoginする

### Google／GitHub Login

外部Providerで本人確認を行った後も、Astera内のSecurity管理はAstera Accountとして扱います。

外部ProviderのPasswordをAsteraが受け取ったり、そのまま流用したりすることはありません。

必要な場合は、初回Login後にAstera専用Passwordを設定します。

### Passwordを忘れた場合

Password再設定画面から、登録Emailを使って再設定します。

---

## 3. Login状態

Astera Appでは、継続利用中のSessionを利用し、毎回すべてを入力し直さずに使えるようにします。

Security上の理由で再確認が必要な場合は、次の操作が求められることがあります。

- Password再入力
- Passkey
- 二段階認証
- Backup Code
- Email確認

共有端末では、利用後にLogoutします。

---

## 4. Account Security

Security画面では、LoginとAccount保護に関する設定を管理します。

### Password

- 現在のPasswordを変更する
- 外部Loginから登録した場合にAstera用Passwordを設定する
- Password再設定履歴を確認する

### Passkey

対応端末では、端末の生体認証や画面Lockを使ってLoginできます。

管理画面では、登録済みPasskeyの名称、登録端末、最終利用、削除を確認します。

### 二段階認証

Passwordだけでなく、確認Codeを使ってAccountを保護します。

設定時には、認証Appへの登録と確認を行います。

### Backup Code

二段階認証を使えない場合に備えるCodeです。

- 安全な場所へ保存する
- 他人へ送らない
- 使用後や紛失時は再生成する

### 接続Account

Google、GitHubなど、接続済みLogin方法を確認します。

接続解除前には、別のLogin方法が残っていることを確認します。

### Login履歴・Session

不審な端末や場所からの利用がないか確認し、必要に応じて他のSessionを終了します。

---

## 5. Plan・Subscription

Plan画面では、現在の契約と利用可能な範囲を確認します。

主な項目：

- 現在のPlan
- 契約期間
- 更新日
- 利用可能な機能
- Storage容量
- Developer API利用範囲
- Option
- Plan変更
- 解約状態

料金やPlan内容は、固定された古い表示ではなく、現在のCatalogに基づいて表示します。

Plan変更時は、次を確認します。

- いつから変更されるか
- CreditやStorageがどう変わるか
- 利用中の機能へ影響があるか
- 解約後にDataがどう扱われるか

---

## 6. Credit

Asteraの実行やOption、Developer APIなどで使用する利用量をCreditとして管理します。

Credit画面では、次を確認します。

- 現在残高
- 購入可能なCredit
- 購入履歴
- 使用履歴
- 予約中のCredit
- 返金・補填
- 低残高通知
- 実行停止状態

### Credit残高が少ない場合

実行前に警告を表示し、必要な場合は購入画面へ進みます。

### Creditが不足した場合

新しい実行を開始せず、停止理由と復帰方法を表示します。

処理途中で不正に成功扱いへせず、利用者が状態を確認できるようにします。

### Credit購入後

支払い完了画面だけで判断せず、Astera側で反映状態を確認します。

反映待ち、完了、失敗、確認が必要な状態を区別します。

---

## 7. CheckoutとBilling Status

### Checkout

購入内容を確認し、外部決済画面へ進むための画面です。

確認項目：

- 購入するPlanまたはCredit
- 金額
- 対象Account
- 適用時期
- 返金・解約に関する案内

### Billing Status

決済後の状態を確認します。

- 完了
- 反映待ち
- 失敗
- Cancel
- 確認が必要

Browserを閉じたり、決済画面から戻ったりした場合でも、Account画面から状態を確認します。

---

## 8. 通知・Credit警告

通知画面では、重要通知と任意通知を分けて管理します。

### 重要通知

- Credit不足による実行停止
- 支払い失敗
- Security設定変更
- 不審なLogin
- Account状態変更
- Shareの重要な変更

### 任意通知

- Credit低下予告
- 利用状況
- 更新案内
- Email・Push通知

重要な停止理由は、通知だけで終わらせず、App内にも表示します。

---

## 9. Data・Privacy

Data・Privacy画面では、入力、結果、File、History、Share、外部接続の扱いを確認します。

確認する内容：

- 何が保存されるか
- どこへ保存されるか
- 保存期間
- Share状態
- 外部Storage接続
- DataのDownload
- 削除方法
- Account退会時の扱い

機密情報を扱う場合は、共有先とStorage設定を確認します。

---

## 10. Accountに問題がある場合

### Loginできない

- Emailが正しいか
- Email確認が完了しているか
- Password再設定が必要か
- 二段階認証Codeが正しいか
- Backup Codeが残っているか

### 外部Login後に進めない

Astera用Password設定やEmail確認が必要な場合があります。

### Creditを購入したが反映されない

Billing Statusで、完了、反映待ち、失敗を確認します。

### 実行が停止した

Credit、Account状態、Plan、System Statusを確認します。

### Passkey端末を失った

別のLogin方法で入り、対象Passkeyを削除します。Loginできない場合はSupportへ連絡します。

---

## 関連Document

- [Astera App完全ガイド](app-guide.md)
- [Workspace・結果管理](workspace-and-results.md)
- [Mobile・Tablet・Accessibility](mobile-and-accessibility.md)
- [FAQ](faq.md)
- [Support](../SUPPORT.md)
