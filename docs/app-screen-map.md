# Astera App画面・Route一覧

Astera App Sourceには43のRoute Patternがあります。

この一覧は、**Source上に存在する画面経路**を示します。各RouteがBackend・認証・決済・Storage等と接続し、本番利用可能であることを示すものではありません。

最新の公開判定は[現在の公開状態](current-status.md)を確認してください。

---

## Statusの読み方

| Status | 意味 |
|---|---|
| Source実装 | Route・画面経路がSourceにある |
| 接続確認前 | Backendや外部Serviceを含む実動作を公開実績に含めない |
| Public説明 | Staticな説明画面としての役割を示す |

---

## 1. 入口・公開情報

| No. | Path | 画面の役割 | 現在の扱い |
|---:|---|---|---|
| 1 | `/` | App入口。`/app/new`へ解決する構成 | Source実装 |
| 2 | `/pricing` | Plan・料金情報 | Source実装、Catalog接続確認前 |
| 3 | `/s/:token` | Public Share Result | Source実装、Token・Data接続確認前 |
| 4 | `/legal` | Legal入口 | Source実装 |
| 5 | `/legal/terms` | 利用規約 | Source実装、正式Contentは公開環境確認対象 |
| 6 | `/legal/privacy` | Privacy Policy | Source実装、正式Contentは公開環境確認対象 |
| 7 | `/legal/commercial` | 特定商取引法表記 | Source実装、正式Contentは公開環境確認対象 |
| 8 | `/legal/api-terms` | Developer API利用条件 | Source実装、API提供は確認前 |

---

## 2. Login・Account登録

| No. | Path | 画面の役割 | 現在の扱い |
|---:|---|---|---|
| 9 | `/login` | Login | Source実装、認証接続確認前 |
| 10 | `/register` | Account登録 | Source実装、登録Backend確認前 |
| 11 | `/verify-email` | Email確認 | Source実装、Email・Token確認前 |
| 12 | `/forgot-password` | Password再設定要求 | Source実装、Email送信確認前 |
| 13 | `/reset-password` | Password再設定 | Source実装、Token処理確認前 |
| 14 | `/account/password/setup` | Astera用Password設定 | Source実装、Account接続確認前 |
| 15 | `/auth/2fa` | 二段階認証Challenge | Source実装、認証App接続確認前 |

認証必須RouteではAccount APIを確認し、未認証時にLoginへ移動するFrontend境界があります。

Session、Cookie、CSRF、Provider連携を含むProduction動作は確認前です。

---

## 3. 実行・Result・Workspace

| No. | Path | 画面の役割 | 現在の扱い |
|---:|---|---|---|
| 16 | `/app` | Workspace入口 | Source実装 |
| 17 | `/app/new` | Input、Purpose、Template、Option、Result | Source実装、Backend実行確認前 |
| 18 | `/app/results/:id` | Result詳細 | Source実装、Result Data接続確認前 |
| 19 | `/app/projects` | Project管理 | Source実装、保存・取得確認前 |
| 20 | `/app/history` | History検索 | Source実装、実Data接続確認前 |
| 21 | `/app/about` | Astera Appとv8の説明 | Source実装 |

`/app/new`のFrontend Sourceには次が含まれます。

- Text入力
- 10種類の目的選択
- File選択UIとMetadata
- Template
- 追加Option
- 処理段階表示
- 8 Section Result Mapping
- Turn Rail
- Copy
- Markdown Download
- 端末共有

File本体Upload、Backend Result、Project・History保存は確認前です。

---

## 4. Settings

| No. | Path | 画面の役割 | 現在の扱い |
|---:|---|---|---|
| 22 | `/app/settings` | Settings入口 | Source実装 |
| 23 | `/app/settings/options` | 追加Option設定 | Source実装、外部処理確認前 |
| 24 | `/app/settings/language` | Theme・表示言語 | Source実装、全環境確認前 |
| 25 | `/app/settings/templates` | 個別Template | Source実装、Server保存確認前 |
| 26 | `/app/settings/storage-destinations` | 外部Storage接続 | Source実装、Storage接続確認前 |
| 27 | `/app/settings/astera-storage` | Astera Storage | Source実装、容量・File接続確認前 |
| 28 | `/app/settings/data-privacy` | Data・Privacy | Source実装、実Data処理確認前 |
| 29 | `/app/settings/notifications` | 通知・Credit警告 | Source実装、配信・残高接続確認前 |

---

## 5. Account・Security・Billing

| No. | Path | 画面の役割 | 現在の扱い |
|---:|---|---|---|
| 30 | `/account` | Account概要 | Source実装、Account API確認前 |
| 31 | `/account/security` | Password・Passkey・2FA等 | Source実装、Security実動作確認前 |
| 32 | `/account/subscription` | Plan・Subscription | Source実装、契約Data確認前 |
| 33 | `/account/credit` | Credit残高・Ledger | Source実装、Credit Backend確認前 |
| 34 | `/account/checkout` | 購入内容確認 | Source実装、外部決済確認前 |
| 35 | `/account/billing/status` | 決済状態 | Source実装、Webhook・反映確認前 |

詳細は[Account・Security・Plan・Credit](account-security-and-billing.md)にまとめています。

---

## 6. Developer・Share

| No. | Path | 画面の役割 | 現在の扱い |
|---:|---|---|---|
| 36 | `/app/developer` | Developer Mode | Source実装、API提供確認前 |
| 37 | `/share/:id` | Private Share | Source実装、認可・Data接続確認前 |
| 38 | `/app/shares` | Share管理 | Source実装、発行・停止・期限確認前 |

---

## 7. System・Support

| No. | Path | 画面の役割 | 現在の扱い |
|---:|---|---|---|
| 39 | `/status` | System Status | Source実装、監視Data接続確認前 |
| 40 | `/offline` | Offline案内 | Source実装 |
| 41 | `/maintenance` | Maintenance案内 | Source実装、状態切替確認前 |
| 42 | `/support` | Support案内 | Source実装、窓口連携確認対象 |
| 43 | その他 | Not Found | Source実装 |

未知Pathを汎用App画面へ流さず、明示的なNot Foundへ送る構成です。

---

## Route数

```text
入口・公開情報             8
Login・Account登録          7
実行・Result・Workspace     6
Settings                    8
Account・Security・Billing  6
Developer・Share            3
System・Support             5
--------------------------------
合計                       43 Route Pattern
```

---

## 現在の公開上の読み方

- 43 Route PatternがSourceへ実装されていることは公開可能
- 各画面の目的とNavigation構成は公開可能
- Backendや外部Serviceを含む動作は接続確認後に公開判定
- RouteがあるだけでLogin、決済、Share、API等を利用可能とは案内しない

---

## 関連Document

- [現在の公開状態](current-status.md)
- [Astera App Guide](app-guide.md)
- [操作Flow](getting-started.md)
- [Workspace・Result管理](workspace-and-results.md)
- [Account・Security・Plan・Credit](account-security-and-billing.md)
