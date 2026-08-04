# Security Policy

AsteraのSecurityに関する報告へご協力いただき、ありがとうございます。

現在のPublic Repositoryでは、Astera AppのProduction利用、Account、決済、Credit、Share、Developer API、Native Appを利用可能な完成機能として案内していません。

ただし、公開Documentation、公開Sample、Route・Frontend Sourceの説明、Security設計に関する問題は報告対象です。

最新の公開判定は[現在の公開状態](docs/current-status.md)を確認してください。

---

## 現在のSecurity報告対象

- Public Repositoryに秘密情報が含まれている
- Documentationが危険な操作を推奨している
- 公開Sampleに個人情報・秘密情報が含まれている
- 公開Linkが不正なDestinationへ移動する
- Source実装説明に、認証や権限を回避できる構造が明記されている
- Route・API境界の設計上、Open Redirect、CSRF、権限漏れ等が発生する可能性がある
- Public／Private Share設計に認可上の欠陥がある
- File、Storage、Download、Delete設計に権限上の欠陥がある
- Checkout、Billing、Credit設計に重複・改ざん・不正反映の可能性がある
- API Key、Token、Cookie等がPublic RepositoryやDocumentationへ露出している
- GitHub ActionsやRepository設定から秘密情報が露出する

Documentationの誤字、通常のLink切れ、内容の分かりにくさは[Support](SUPPORT.md)またはGitHub Issueを利用できます。

---

## 将来のProduction機能で対象となる問題

次の機能が公開確認済みになった後は、以下もSecurity報告対象になります。

- 他人のAccountへアクセスできる
- Loginを回避できる
- Password再設定を本人以外が利用できる
- Passkey、二段階認証、Backup Codeの問題
- Sessionが正しく終了しない
- 権限のないProject、History、Result、Fileへアクセスできる
- 停止したShareへアクセスできる
- 個人情報や秘密情報が別利用者へ表示される
- CheckoutやBilling Statusの不整合
- Creditが不正に増減する
- Developer APIで権限を越えた操作ができる

現在これらを利用可能機能として案内しているわけではありません。

---

## 報告方法

[Astera公式Site](https://asterav8.jp)の問い合わせ窓口から、Securityに関する報告であることを明記してください。

Public Issue、SNS、公開Chatへ、再現手順や秘密情報を書かないでください。

---

## 報告に含める内容

分かる範囲で次を含めてください。

- 対象Repository、Document、File、Route、設計
- 問題の内容
- 再現または確認手順
- 想定される影響
- 問題を確認した最小限の証拠
- 関連するCommitまたはPublic URL
- 公開を避けるべき情報が含まれるか

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
- 顧客・第三者の個人情報
- 契約書全文
- Private RepositoryのSource全文
- 本人以外のData

ScreenshotやLogを送る場合は、秘密情報を伏せてください。

---

## 安全な確認の範囲

報告のために次を行わないでください。

- 他人のAccountやDataを意図的に取得する
- 公開環境を停止させる
- 大量Requestを送る
- Dataを変更・削除する
- Passwordや認証Codeを推測する
- 第三者へ問題を利用させる
- 個人情報を保存・公開する

問題を確認した時点で操作を止め、最小限の情報で報告してください。

---

## 報告後に確認する内容

1. 報告を受け取れているか
2. Public Repositoryまたは設計へ影響するか
3. 秘密情報の削除・失効が必要か
4. 公開停止または説明修正が必要か
5. 修正方法
6. Documentation、CHANGELOG、Release情報への反映
7. 将来のProduction実装へ追加すべきTest

Security上の理由により、調査中の詳細を公開できない場合があります。

---

## Public Issueで報告できる内容

- Documentationの誤り
- Link切れ
- 公開Sampleの問題
- 公開状態の誤表記
- 個人情報を含まない一般的なError

秘密情報、認証・権限回避の詳細、決済・Token関連の問題はPublic Issueへ書かないでください。

---

## 関連Document

- [現在の公開状態](docs/current-status.md)
- [Support](SUPPORT.md)
- [Contributing](CONTRIBUTING.md)
