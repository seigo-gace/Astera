# Support

Asteraに関する質問、公開情報の誤り、不具合、Account、Plan、Credit、Security、取材・提携などは、内容に合う窓口からお知らせください。

このPageでは、**GitHub Issueへ書いてよい内容**と、**個別のSupport窓口へ送る内容**を分けて説明します。

---

## GitHub Issuesを使う内容

このRepositoryのIssuesでは、公開情報と公開環境に関する次の内容を受け付けています。

- Documentationの誤り
- 説明が分かりにくい箇所
- Link切れ
- 誤字、表記ゆれ
- 公開Sampleの改善
- 公開環境で確認できる一般的な不具合
- Web、Smartphone、Tabletでの表示問題
- Accessibilityの改善案
- Astera Appの使い方に関する提案
- FAQへ追加してほしい質問

Issueを作成する前に、同じ内容がすでに報告されていないか確認してください。

---

## 公式Support窓口を使う内容

次の内容は、公開Issueへ書かず、[Astera公式Site](https://asterav8.jp)の問い合わせ窓口を利用してください。

- Loginできない
- Email確認
- Password再設定
- Passkey
- 二段階認証
- Backup Code
- Account停止・退会
- Plan・Subscription
- Credit購入・残高・補填
- Checkout・Billing Status
- 決済の反映
- 個人情報
- 契約情報
- 非公開Project
- Private Share
- API Key
- Developer APIの個別利用
- 取材、掲載、支援、提携、事業相談

---

## Astera App内で最初に確認する場所

Supportへ連絡する前に、問題の種類に応じて次を確認します。

### 実行できない

- 入力が空ではないか
- Account状態
- Plan
- Credit残高
- System Status
- Network接続

### Resultが表示されない

- 実行が完了しているか
- Error Message
- HistoryまたはResult詳細
- 再読み込み後も同じか

### Loginできない

- Email確認
- Password再設定
- 二段階認証
- Backup Code
- 外部Login後のAstera用Password設定

### 決済後に反映されない

- Billing Status
- Accountの対象
- 反映待ち表示
- 再読み込み後のCredit・Plan

### Shareを止めたい

- Share管理
- Public／Privateの種類
- 対象Result
- 有効期限

---

## 不具合を伝えるときに役立つ情報

次を分かる範囲で書いてください。

- 発生日時
- 何をしようとしたか
- どの画面で起きたか
- 期待していた結果
- 実際に起きたこと
- 再現手順
- 毎回起きるか
- 表示されたError Message
- 利用端末
- OS
- BrowserとVersion
- 画面向き
- 画面分割の有無
- Network環境
- Result ID、Project ID、Share IDなど、公開して問題ない識別情報

### Mobile／Tabletの表示問題

次もあると確認しやすくなります。

- 端末の種類
- 縦向き・横向き
- Browser AppまたはNative App
- Keyboard表示中か
- 画面が左右へ動くか
- Buttonが押せないか
- Scrollできない場所

---

## 書かない情報

公開Issueへ次を書かないでください。

- Password
- Passkey情報
- 二段階認証Code
- Backup Code
- API Key
- Access Token
- Cookie
- 決済Card情報
- 住所、電話番号、Emailなどの個人情報
- 顧客情報
- 契約書の全文
- 非公開URL
- Private Projectの内容

必要なScreenshotを添付する場合は、個人情報や秘密情報を伏せてください。

---

## Documentationの修正

Documentationの誤りは、IssueまたはPull Requestで提案できます。

特に次を歓迎します。

- 初めて読む人には分からない表現
- 専門用語の説明不足
- Astera Appの画面と説明の食い違い
- PCだけを前提にした説明
- Link切れ
- 古い料金・機能案内
- 公開Sampleの不足

Contribution方法は[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

---

## Securityに関する報告

認証、Account、個人情報、Share、決済、API、権限などのSecurity問題は、公開Issueへ詳しい再現手順を書かず、[Security Policy](SECURITY.md)に沿って報告してください。

---

## 問い合わせ後

報告内容によって、次の確認を行います。

- 再現できるか
- 特定端末だけか
- Account固有か
- 公開環境全体か
- Documentationの問題か
- System側の問題か
- Security上の影響があるか

公開できる修正や案内は、Documentation、CHANGELOG、Release情報へ反映します。
