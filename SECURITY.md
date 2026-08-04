# Security Policy

Asteraの安全性に関する報告へご協力いただき、ありがとうございます。

認証、Account、個人情報、Share、決済、Credit、Developer APIなどに関する問題は、公開Issueへ詳細を書かず、非公開の問い合わせ窓口から報告してください。

---

## Security報告の対象

次のような問題が対象です。

- 他人のAccountへアクセスできる
- Loginを回避できる
- Password再設定が本人以外に利用できる
- Passkey、二段階認証、Backup Codeの問題
- Sessionが正しく終了しない
- 権限のないProject、History、Result、Fileを確認できる
- Public ShareとPrivate Shareの権限問題
- 停止したShareへ引き続きアクセスできる
- 個人情報や秘密情報が表示される
- CheckoutやBilling Statusの不整合
- Creditが不正に増減する
- API Key、Token、Cookie、秘密情報が露出する
- Developer APIで権限を越えた操作ができる
- 入力した内容が別の利用者へ表示される
- File Downloadや削除の権限問題
- 外部URLへの不正な移動
- 利用者の操作なしで重要な変更が行われる

Documentationの誤字や通常の表示崩れは、Security報告ではなくGitHub Issueを利用できます。

---

## 報告方法

[Astera公式Site](https://asterav8.jp)の問い合わせ窓口から、Securityに関する報告であることを明記してください。

公開Issue、SNS、公開Chatへ、再現手順や秘密情報を書かないでください。

---

## 報告に含める内容

分かる範囲で次を含めてください。

- 問題が起きる画面・機能
- 発生日時
- 再現手順
- 毎回再現するか
- 想定される影響
- 自分のAccountだけか、他Accountにも影響する可能性があるか
- 利用端末
- OS
- BrowserとVersion
- Public／Private Shareの種類
- 表示されたError Message
- 問題を確認した最小限の証拠

### 識別情報

必要な場合は、次のような公開して問題のない識別子を伝えてください。

- Result ID
- Project ID
- Share ID
- 発生日時
- Request ID

実際の秘密情報そのものは送らないでください。

---

## 送らない情報

- Password
- Passkeyの秘密情報
- 二段階認証Code
- Backup Code
- API Key
- Access Token
- Refresh Token
- Cookie全文
- 決済Card番号
- Security Code
- 顧客の個人情報
- 契約書全文
- 本人以外のData

ScreenshotやLogを送る場合は、秘密情報を伏せてください。

---

## 安全な確認の範囲

報告のために、次の行為を行わないでください。

- 他人のAccountやDataを意図的に取得する
- Serviceを停止させる
- 大量Requestを送る
- Dataを変更・削除する
- Passwordや認証Codeを推測する
- 第三者へ問題を利用させる
- 個人情報を保存・公開する

問題を確認した時点で操作を止め、最小限の情報で報告してください。

---

## Astera側で確認する内容

報告後、次を確認します。

1. 報告を受け取れているか
2. 再現できるか
3. 影響する画面・Account・Data
4. 緊急停止が必要か
5. 一時的な回避方法があるか
6. 修正方法
7. 利用者への案内が必要か
8. DocumentationやRelease情報へ反映する内容

Security上の理由により、調査中の詳細を公開できない場合があります。

---

## Accountが危険だと思った場合

自分のAccountに不審な動きがある場合は、可能な範囲で次を行ってください。

- Passwordを変更する
- 不明なSessionを終了する
- 不明なPasskeyを削除する
- 二段階認証を確認する
- Backup Codeを再生成する
- 接続中のGoogle／GitHub Accountを確認する
- Public／Private Shareを確認する
- API Keyを停止・更新する
- BillingとCredit履歴を確認する

Loginできない場合は、公式Support窓口へ連絡してください。

---

## Public Documentationと通常のBug

次はGitHub Issuesから報告できます。

- Documentationの誤り
- Link切れ
- 公開Sampleの問題
- 一般的な表示崩れ
- 特定端末での操作問題
- 個人情報を含まないError

通常のSupport案内は[SUPPORT.md](SUPPORT.md)をご覧ください。
