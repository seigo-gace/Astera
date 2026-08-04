# 連携の考え方

Asteraは、すべてを一つのApplicationへ閉じ込めるものではありません。

Astera Appで入力と結果を管理し、Astera v8で判断材料を作り、必要に応じて主役AI、Storage、Developer APIなどへつなぎます。

このDocumentでは、各連携が何のためにあるのかを利用者向けに説明します。

---

## 1. 主役AIとの連携

Asteraは、ChatGPT、Claude、Gemini、自作AI、自社AIなどを置き換えるものではありません。

役割は次のように分かれます。

```text
Astera
目的・不足・事実・Risk・反対視点・比較案を整理する

主役AI
判断材料を使って、文章・計画・Code・説明へ仕上げる
```

### 主役AIへ渡すもの

- 本当の目的
- 前提不足
- 事実確認
- 危機察知
- 比較案
- 推奨判断
- 主役AIへの再指示

### 使い方の例

#### 提案書

Asteraで提案の前提、Risk、比較案を整理し、主役AIへ提案書の文章化を依頼します。

#### Code

Asteraで要件、依存関係、失敗条件、検証項目を整理し、主役AIへ実装を依頼します。

#### 問い合わせ回答

Asteraで利用者の本当の問題と確認事項を整理し、主役AIへ分かりやすい回答を作らせます。

---

## 2. Fileとの連携

Astera Appでは、資料を実行へ追加できます。

例：

- 企画書
- 見積書
- 契約資料
- AI回答
- Error Log
- 設計資料
- 比較表

Fileを使うときは、「何を確認したいか」を入力へ書きます。

Fileの存在だけでは、目的や優先順位は決まりません。

---

## 3. Projectとの連携

Projectは、同じ目的に関係する実行、File、Resultをまとめます。

単発の入力と違い、Projectでは前回からの変化を扱えます。

- 新しい事実
- 解決した前提不足
- 変更された期限
- 追加された候補
- 新しいRisk
- 推奨判断の変更

---

## 4. 外部Storage

外部Storage接続は、FileやResultの保存先を管理するために使います。

確認する内容：

- どのStorageへ保存するか
- 誰がアクセスできるか
- 保存期間
- 削除方法
- Projectとの関連
- Shareとの違い

外部Storageへ保存する場合でも、Astera App上のProject名、Result、Share状態と混同しないようにします。

---

## 5. Astera Storage

Astera Storageは、Astera Account内で扱う保存領域です。

主な管理項目：

- 契約容量
- 使用量
- 残量
- 保存File
- Download
- Delete
- 容量変更
- 保存停止状態

保存容量と実行用Creditは別の目的を持ちます。

---

## 6. Share

### Public Share

共有用URLを使い、外部へ見せるための連携です。

### Private Share

権限を持つ相手と限定共有するための連携です。

ShareはStorageへの保存とは異なります。保存されていても共有されているとは限らず、共有を停止しても元のResultが削除されるとは限りません。

---

## 7. Developer API

Developer Modeでは、Asteraの判断材料生成を外部Applicationや業務Systemから利用するためのAPIを管理します。

利用例：

- 自社の問い合わせ画面へ組み込む
- 業務Systemのレビュー工程へ加える
- 独自AIの前処理として利用する
- Document確認Workflowへ組み込む
- 障害対応の入力を一定形式へ整理する

管理する項目：

- API Key
- 接続先
- 使用量
- Credit
- 停止状態
- Error
- 権限

APIの具体的な仕様は、公開されている正式なAPI Documentを基準にします。

---

## 8. 認証連携

GoogleやGitHubなどのLogin Providerは、本人確認の入口として利用します。

ProviderのPasswordをAsteraへ渡すものではありません。

Astera Accountでは、必要に応じて次を管理します。

- Astera用Password
- Passkey
- 二段階認証
- Backup Code
- 接続Provider
- Session

---

## 9. 決済連携

PlanやCredit購入では、決済画面とAstera Accountの状態を連携します。

決済画面で支払いが完了したことと、Astera側へ反映されたことを分けて確認します。

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

---

## 10. System StatusとSupport

実行できない場合は、入力内容だけでなく、Account、Credit、接続先、System Statusを確認します。

Supportへ連絡するときは、次を伝えると確認しやすくなります。

- 発生日時
- 利用端末とBrowser
- 画面名
- 操作内容
- 表示されたError
- Result IDやProject ID
- 再現するか

Password、Backup Code、API Key、決済情報は送らないでください。

---

## 関連Document

- [Astera App完全ガイド](app-guide.md)
- [Astera AppとAstera v8](app-and-runtime.md)
- [Workspace・結果管理](workspace-and-results.md)
- [Account・Security・Plan・Credit](account-security-and-billing.md)
