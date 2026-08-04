# 連携の考え方

このDocumentは、Astera App、Astera v8、主役AI、File、Storage、認証、決済、Developer APIの**設計上の関係**と現在の接続状態を説明します。

連携先を説明していることは、現在そのServiceが本番接続済みであることを意味しません。

最新の公開判定は[現在の公開状態](current-status.md)を確認してください。

---

## 現在の状態

| 連携 | 現在の状態 |
|---|---|
| 主役AIへのCopy利用 | 公開Use Caseとして説明可能 |
| File Metadata | Frontend Source実装済み |
| File本体Upload・解析 | 接続確認前 |
| Project・History | Route・画面実装済み、Server保存確認前 |
| 外部Storage | Route・画面実装済み、接続確認前 |
| Astera Storage | Route・画面実装済み、Storage Backend確認前 |
| Public／Private Share | Route・画面実装済み、発行・認可確認前 |
| Developer API | 管理画面・境界設計あり、提供確認前 |
| Google／GitHub Login | Route・方針あり、Provider接続確認前 |
| Plan・Credit・決済 | Route・画面あり、決済・Ledger確認前 |

---

## 1. 主役AIとの関係

Asteraは、ChatGPT、Claude、Gemini、自作AI、自社AI等を置き換えるものではありません。

役割は次のように分かれます。

```text
Astera
目的・不足・事実・Risk・反対視点・比較案を整理する

主役AI
判断材料を使って、文章・計画・Code・説明へ仕上げる
```

AsteraのResultをCopyし、主役AIへ渡す使い方は、現在のPublic DocumentationとSampleで説明できます。

専用APIによる自動連携は、Developer API確認後の公開範囲です。

---

## 2. File

Frontend SourceにはFile選択UIとMetadataをPayloadへ含める構造があります。

現在扱う構造：

- File名
- Size
- Type

現在の公開実績に含めないもの：

- File本体Upload
- Storage保存
- 内容抽出
- Document解析
- 複数File比較
- Resultへの内容反映

したがって、「Fileを選択できる画面があること」と「File内容を解析できること」を分けて説明します。

---

## 3. Project・History

ProjectとHistoryのRoute・画面経路はSourceへ実装されています。

設計上の役割：

- Project：同じ目的の実行、Result、File、判断変更をまとめる
- History：過去の実行を検索・再利用する

実Data保存、取得、検索、別端末同期等はBackend接続確認前です。

---

## 4. 外部Storage

外部Storage接続用のRoute・画面経路があります。

設計上は次を管理します。

- 接続先
- 権限
- 保存先
- 保存期間
- 削除
- Projectとの関係

現在、特定の外部Storageへ接続済みとは案内しません。

OAuth、権限確認、Upload、Download、Delete、同期等は実接続確認前です。

---

## 5. Astera Storage

Astera Storage画面は、設計上次を扱います。

- 契約容量
- 使用量
- 残量
- 保存File
- Download
- Delete
- 容量変更
- 保存停止状態

現在はRoute・画面構成がSourceにあります。

Storage Backend、容量計測、File保存、削除保証等は確認前です。

---

## 6. Share

次のRoute Patternがあります。

- Public Share
- Private Share
- Share管理

設計上は、共有URL、権限、期限、停止等を扱います。

現在の公開実績に含めないもの：

- Share Token発行
- Result Data保存
- Public／Private認可
- 期限切れ処理
- URL停止
- 共有解除後のAccess遮断

---

## 7. Developer API

Developer ModeのRouteと管理画面構成があります。

設計上の管理対象：

- API Key
- 接続先
- 使用量
- Credit
- 停止状態
- Error
- 権限
- API Terms

現在、Developer APIを提供中とは案内しません。

Endpoint、Schema、Key発行、Authentication、Rate Limit、使用量計測、課金等の確認後に、正式なAPI Documentを公開します。

---

## 8. 認証

Login、Account登録、Email確認、Password再設定、Passkey、二段階認証等のRoute・画面構成があります。

GoogleやGitHub等のProvider PasswordをAsteraが取得・流用しない方針です。

現在の公開実績に含めないもの：

- Provider OAuth実接続
- Session発行
- Email送信
- Passkey登録・Login
- 二段階認証
- Backup Code
- Account Recovery

---

## 9. Plan・Credit・決済

Plan、Credit、Checkout、Billing StatusのRoute・画面構成があります。

設計上のFlow：

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

現在の公開実績に含めないもの：

- 外部決済画面への実接続
- Webhook
- 署名検証
- Plan反映
- Credit Ledger反映
- 重複防止
- 返金・補填
- 枯渇停止・復帰

---

## 10. Fail-Closed

Frontend Sourceでは、API未設定、Endpoint Error、Schema不整合等の状態を、Mock成功や仮Dataで隠さない方針です。

連携できていない場合は、成功したように表示せず、Errorとして扱います。

この方針により、「画面があるから機能が動いている」という誤認を避けます。

---

## 現在公開できる連携情報

- 各連携の目的とArchitecture
- Route・Frontend境界のSource実装
- 主役AIへResultをCopyして使うFlow
- File MetadataのFrontend処理
- API未接続時に安全停止する方針

現在、接続済みとは説明しないもの：

- File内容解析
- Storage
- Share
- 認証
- 決済
- Credit
- Developer API

---

## 関連Document

- [現在の公開状態](current-status.md)
- [Astera App Guide](app-guide.md)
- [Workspace・Result管理](workspace-and-results.md)
- [Account・Security・Plan・Credit](account-security-and-billing.md)
