# Astera App Guide

このDocumentは、Astera Appの**現在のSource実装範囲**を説明します。

操作画面やRouteがSourceへ存在することと、Backend・認証・決済・Storage・Production環境を含めて実際に利用できることは同じではありません。

最新の公開判定は[現在の公開状態](current-status.md)を正本とします。

---

## 状態の読み方

| 表記 | 意味 |
|---|---|
| 公開済み | Public Repositoryで内容を確認できる |
| Source実装済み | Frontend Source、Route、画面、処理が存在する |
| 接続確認前 | Backendや外部Serviceを含む実動作をまだ公開実績に含めない |
| 実機確認前 | Smartphone、Tablet、Android、iOS等の実端末確認を公開実績に含めない |

---

## 1. App全体の現在地

Astera Appは、React、TypeScript、Vite、Capacitorの共通Sourceを、Web、Android、iOSへ展開する構成です。

現在のSourceには、43のRoute Patternと、次の画面領域が含まれています。

```text
Astera App
├─ 新しい実行・Result
├─ Project・History・Turn
├─ Settings
├─ Account・Security
├─ Plan・Credit・Billing
├─ Developer Mode
├─ Public／Private Share
├─ Legal・Status・Support
└─ Web・Smartphone・Tablet・Native Shell
```

現在公開できる事実は、これらの**画面経路とFrontend処理がSourceへ実装されていること**です。

Account、決済、Storage、Share、Developer API等が本番で利用可能であるとは、まだ表記しません。

---

## 2. 新しい実行画面

新しい実行画面は、Asteraへ渡す内容と処理条件を設定するFrontendです。

現在のSourceでは、次を扱います。

- Text入力
- 目的選択
- File選択UI
- Project情報の選択UI
- Template
- 追加Option
- 実行開始
- 処理段階表示
- 停止操作
- Result表示
- Turn移動

実際のResult生成はBackend EndpointとResponse Schemaに依存します。Production接続を含む動作確認が終わるまで、Frontend画面の存在だけで「実行可能」とは表記しません。

---

## 3. 入力

入力欄には、質問だけでなく次の内容を入れる構成です。

- 迷っていること
- 複数案の比較
- 企画・計画
- 資料の確認目的
- AIが作った回答
- 障害や失敗の状況
- 契約や提案の確認事項
- 改善したい文章や設計
- 調査前に整理したい論点

判断材料を具体的にするため、次の情報を一緒に入れることを想定しています。

- 最終的な目的
- 背景
- 期限
- 予算・人数・時間等の制約
- 現在の候補
- 確認済みの事実
- 未確認の推測
- 避けたい失敗

---

## 4. 目的選択

現在のFrontend Sourceには、次の10種類の目的が定義されています。

| 目的 | 想定する使い方 |
|---|---|
| 自動 | 入力内容から見る方向を選ぶ |
| Review | 資料・計画・提案の抜けを確認する |
| 比較 | 複数案を同じ条件で比べる |
| 検証 | 説明・根拠・結論が成立するか確認する |
| 改善 | 現在案の弱点と改善方向を整理する |
| 調査 | 調べるべき項目と情報源を整理する |
| 計画 | 順序、依存関係、停止条件を整理する |
| 検討 | 方向を決める前に複数視点を出す |
| 判断 | 最終選択に必要な成立条件を整理する |
| 原因 | 問題の原因候補と確認順を整理する |

目的選択UIがSourceへ存在することは確認済みです。目的ごとのBackend処理結果は、実接続確認後に利用可能範囲へ加えます。

---

## 5. Templateと追加Option

現在のSourceには、次のTemplateが定義されています。

- Review
- 比較
- 計画
- Risk確認

追加Optionとして、次の選択UIがあります。

- 高精度翻訳
- 文書生成
- 高度な書き換え

これらはFrontend上の選択肢です。各Optionの外部処理・課金・完成Outputまでを現在利用可能とは表記しません。

---

## 6. File機能

File選択UIとFile Metadataを扱うSourceは存在します。

現在Payloadへ含める構造があるのは、主に次の情報です。

- File名
- Size
- Type

**File本体をUploadし、内容を読み取って判断材料へ反映する動作は、現在の公開実績に含めません。**

そのため、現在公開できる説明は「Fileを選択し、関連FileのMetadataを実行条件へ含める画面がある」までです。

企画書、見積書、契約書、Log等を実際に解析できるという表記は、Upload・Storage・解析Backendの確認後に追加します。

---

## 7. 実行Payloadと安全停止

現在のFrontend Sourceでは、入力内容を次のような情報へまとめてAPIへ渡す構成です。

- Input
- Purpose
- Additional Option
- File Metadata
- Template

API Baseがない、Endpointが応答しない、Response Schemaが合わない等の場合に、Mockの成功結果へ置き換えないFail-Closed方針です。

つまり、接続できていない状態を「成功したように見せる」ことは、現在のSource方針に含めません。

---

## 8. 処理段階表示

Frontendには、処理中の状態を段階表示する構造があります。

想定される表示は次の流れです。

1. 判断材料を読み込む
2. 情報を確認する
3. 条件を照合する
4. 複数案を比較する
5. Resultを構造化する
6. 8つの項目へ割り当てる

この表示はFrontend Source実装範囲です。各段階でBackendが実際に行う処理との一致は、接続検証後に公開判定します。

---

## 9. 8つの判断材料

Responseを次の8項目へ割り当てるFrontend Mappingがあります。

1. 本当の目的
2. 前提不足
3. 事実確認
4. 危機察知
5. 反対視点
6. 比較案
7. 推奨判断
8. 主役AIへの再指示

Resultは一枚の長文ではなく、項目ごとに確認する構成です。

Astera v8の処理内容は[Asteraの仕組み](how-it-works.md)をご覧ください。

---

## 10. TurnとResult再利用

現在のFrontend Sourceには、次の操作があります。

- Turn Rail
- Turn間の移動
- Turn名の変更
- Turn削除
- Section単位のCopy
- Result全体のCopy
- Markdown Download
- 端末共有

CopyとMarkdown生成はFrontendで扱う範囲です。

Project保存、History保存、Server側Result ID、Share URLの発行等はBackend接続を含むため、現在の公開実績には含めません。

---

## 11. ProjectとHistory

ProjectとHistoryのRoute・画面経路はSourceへ実装されています。

設計上の役割は次のとおりです。

- **Project**：同じ目的の実行、資料、Result、判断変更をまとめる
- **History**：過去の実行を日時や条件から探す

ただし、実Dataの保存、取得、検索、同期はBackend EndpointとDatabaseに依存します。

そのため、現在は「Project・History画面のSource実装」を公開範囲とし、「実Dataを保存・再取得できること」は接続確認後の判定対象です。

---

## 12. Settings

Source上には、次のSettings Routeがあります。

- Option
- 表示・言語
- Template
- 外部Storage接続
- Astera Storage
- Data・Privacy
- 通知・Credit警告

Theme、表示言語、全画面入力、Reduced Motion等のFrontend設定を扱う構造があります。

外部Storage、契約Storage容量、通知配信、Credit警告等は外部接続を含むため、現在利用可能とは表記しません。

---

## 13. Account・Security

Source上には次のRoute・画面経路があります。

- Login
- Account登録
- Email確認
- Password再設定
- Astera用Password設定
- 二段階認証Challenge
- Account概要
- Account Security

Security画面の設計には、Password、Passkey、二段階認証、Backup Code、接続Account、Session等が含まれます。

現在公開できるのは、Route・画面・API境界のSource実装です。

認証Provider、Session、Email送信、Passkey登録、二段階認証の本番動作は、実接続確認が終わるまで利用可能機能として扱いません。

---

## 14. Plan・Credit・Billing

Source上には次のRoute・画面経路があります。

- 料金・Plan
- Plan・Subscription
- Credit
- Checkout
- Billing Status

設計上は、Plan、Credit残高、購入、利用履歴、決済状態等を扱います。

Square等の外部決済、Credit Ledger、反映処理、返金・補填、停止・復帰処理は実接続確認前です。

現在は、これらの画面構成とFrontend境界を公開し、購入可能・決済可能とは表記しません。

---

## 15. Developer Mode

Developer ModeのRouteと管理画面構成はSourceへ実装されています。

設計上の管理対象は次のとおりです。

- API利用状態
- API Key
- 使用量
- Credit
- 接続先
- Error・停止理由
- API Terms

Developer APIのEndpoint、Key発行、権限、使用量計測、課金を含む実運用は、現在の公開実績には含めません。

---

## 16. Share

Public Share、Private Share、Share管理のRouteはSourceへ実装されています。

設計上は、公開URL、限定共有、期限、停止等を扱います。

実際のShare発行、認可、保存、停止、期限処理はBackend接続を含むため、現在利用可能とは表記しません。

---

## 17. Web・Smartphone・Tablet

共通Frontend Sourceには次のResponsive対応が含まれます。

- Desktop Sidebar
- Smartphone Header・Drawer
- Tablet幅への対応
- OrientationとWindow Resize
- Visual Viewport
- Safe Area
- Touch Target
- Software Keyboard対策
- Reduced Motion
- Light／Dark
- Hoverなし端末への対応
- Horizontal Overflow防止

これらはSource実装範囲です。

実Smartphone Browser、実Tablet、Foldable、Android実機、iPhone／iPad実機での確認は、現在の公開実績に含めません。

詳細は[Mobile・Tablet・Accessibility](mobile-and-accessibility.md)をご覧ください。

---

## 18. Android・iOS

Capacitorを利用したAndroid／iOS Native Shell用の設定とWorkflowがあります。

現在の公開実績には、次を含めません。

- Android APK／AABの実Build成功
- Android実機動作
- iOS Simulator Build成功
- iPhone／iPad実機動作
- TestFlight
- Google Play公開
- App Store公開

Native Appを公開済みとは表記しません。

---

## 現在公開できるApp情報のまとめ

| 項目 | 公開上の扱い |
|---|---|
| Appの目的・画面構成 | 公開可能 |
| 43 Route Pattern | Source実装として公開可能 |
| 入力・目的・Template・Option UI | Source実装として公開可能 |
| Result Mapping・Turn・Copy・Markdown | Source実装として公開可能 |
| Responsive・Native Shell設定 | Source実装として公開可能 |
| Backendを含む実行 | 確認前 |
| File内容解析 | 確認前 |
| Project・History・Shareの実保存 | 確認前 |
| Account・認証・Securityの実運用 | 確認前 |
| Plan・Credit・決済 | 確認前 |
| Developer API | 確認前 |
| Android・iOS実機／Store | 確認前 |

---

## 関連Document

- [現在の公開状態](current-status.md)
- [App画面一覧](app-screen-map.md)
- [Astera AppとAstera v8](app-and-runtime.md)
- [Asteraの仕組み](how-it-works.md)
- [Workspace・結果管理](workspace-and-results.md)
- [Account・Security・Plan・Credit](account-security-and-billing.md)
- [Mobile・Tablet・Accessibility](mobile-and-accessibility.md)
