# Astera Appの操作Flow

このDocumentは、現在のAstera App Sourceに沿って、入力からResult再利用までの画面Flowを説明します。

Production環境で全機能が利用可能であることを示すManualではありません。

最新の利用可能範囲は[現在の公開状態](current-status.md)を確認してください。

---

## 最初に理解すること

Asteraは、質問へ直接「正解」を返す生成AIではありません。

入力された内容を、次の8つの判断材料へ整理する仕組みです。

1. 本当の目的
2. 前提不足
3. 事実確認
4. 危機察知
5. 反対視点
6. 比較案
7. 推奨判断
8. 主役AIへの再指示

現在のApp Sourceには、入力、目的選択、処理状態、Result Mapping、Turn、Copy、Markdown Download、端末共有等のFrontend処理があります。

Backend接続を含む実行結果は別の検証対象です。

---

## Step 1｜新しい実行画面

Source上の`/app/new`は、新しい入力を行う中心画面です。

現在のFrontendでは、次を一つの画面で扱います。

- Text入力
- 目的選択
- File選択UI
- Project情報UI
- Template
- 追加Option
- 実行開始
- 処理段階表示
- Result表示
- Turn移動

この画面がSourceにあることは確認済みです。

Production URL上でBackendと接続した実行が成立することは、現在の公開実績に含めません。

---

## Step 2｜整理したい内容を入力する

入力欄は、短い質問だけでなく次の内容を想定しています。

- 迷っていること
- 比較したい商品・Service・案
- 作成中の計画
- 資料の確認目的
- AIが作った回答
- 問題が起きた状況
- 契約や提案の確認事項
- 誰かへ説明したい考え

次の情報を入れると、判断条件を具体化できます。

| 情報 | 書く内容 |
|---|---|
| 目的 | 最終的に何を決めたいか |
| 背景 | なぜ今この判断が必要か |
| 期限 | いつまでに決める必要があるか |
| 制約 | 予算、時間、人数、使えない方法 |
| 候補 | すでに考えている案 |
| 事実 | 日時、数字、実際に起きたこと |
| 推測 | まだ確認していないが考えていること |
| 避けたいこと | 損失、危険、関係悪化、運用停止等 |

### 入力例

```text
現在使っている予約Systemを変更するか迷っています。
スタッフは5人で、全員が毎日使います。
候補はA、B、Cです。

月額費用は下げたいですが、操作が難しくなって予約ミスが増えることは避けたいです。
2か月以内に決める必要があります。
料金、操作性、移行の手間、問い合わせ対応、障害時の戻しやすさを比べてください。
```

---

## Step 3｜目的を選ぶ

現在のSourceには次の10種類の目的があります。

| 目的 | 想定する使い方 |
|---|---|
| 自動 | 入力内容から見る方向を選ぶ |
| Review | 資料や計画の抜けを確認する |
| 比較 | 複数案を同じ条件で比べる |
| 検証 | 説明、根拠、結論が成立するか確かめる |
| 改善 | 現在の案をより良くする |
| 調査 | 調べるべき論点を整理する |
| 計画 | 順序、依存関係、判断点を整理する |
| 検討 | 方向を決める前に広く考える |
| 判断 | 最終選択と成立条件を整理する |
| 原因 | 問題の原因候補と確認順を作る |

目的選択UIはSource実装済みです。

各目的がBackend側の処理へ正しく反映されることは、実接続確認後に公開判定します。

---

## Step 4｜Templateと追加Option

現在のSourceには次のTemplateがあります。

- Review
- 比較
- 計画
- Risk確認

追加Optionとして次の選択UIがあります。

- 高精度翻訳
- 文書生成
- 高度な書き換え

これらはFrontend上の選択肢です。

翻訳・文書生成・書き換えの外部処理、品質、課金を含む実動作は、現在の公開実績には含めません。

---

## Step 5｜Fileを選ぶ

現在のSourceにはFile選択UIがあります。

Frontend Payloadへ含める構造があるのは、File名、Size、Type等のMetadataです。

**File本体のUploadと内容解析は、現在の公開実績には含めません。**

したがって、現段階の操作Flowでは「関連Fileを選択したことを実行条件へ含める」までを説明対象とします。

---

## Step 6｜実行Payloadを作る

Frontendは主に次をPayloadへまとめる構成です。

- Input
- Purpose
- Additional Option
- File Metadata
- Template

API未接続、Endpoint Error、Response不整合時に、Mockの成功Resultへ置き換えないFail-Closed方針です。

Production Backendとの実接続は現在の公開実績に含めません。

---

## Step 7｜処理段階を見る

Sourceには、処理中の状態を段階表示する構造があります。

1. 判断材料を読み込む
2. 情報を確認する
3. 条件を照合する
4. 複数案を比較する
5. Resultを構造化する
6. 8つの項目へ出力する

この表示はFrontend Source実装範囲です。

Backendの実処理と段階表示の一致は、接続検証後に判定します。

---

## Step 8｜8つのResult Section

FrontendはResponseを8項目へMappingする構成です。

最初に確認する場合は、次の3項目から読むと全体をつかみやすくなります。

### 前提不足

決める前に確認する必要がある条件です。

### 危機察知

失敗した場合の影響、停止条件、戻せるかを確認します。

### 推奨判断

おすすめだけでなく、その案が成立する条件を確認します。

その後、事実確認、反対視点、比較案を読み、推奨の根拠を確認します。

---

## Step 9｜Turnを移動する

現在のFrontend SourceにはTurn Railがあります。

Source上の操作には次が含まれます。

- Turn間の移動
- Turn名の変更
- Turn削除

TurnをServerへ保存し、別端末や後日のSessionから再取得できることはBackend接続を含むため、現在の公開実績には含めません。

---

## Step 10｜Resultを再利用する

現在のFrontend Sourceには、次の再利用操作があります。

- Section単位のCopy
- Result全体のCopy
- Markdown Download
- 端末共有

これらはFrontend Source実装として公開できます。

Project保存、History保存、Share URL発行はBackendを含むため、現在利用可能とは表記しません。

---

## Project・History・Shareの現在地

次のRouteと画面経路はSourceへ実装されています。

- Project
- History
- Result詳細
- Public Share
- Private Share
- Share管理

設計上の役割は次のとおりです。

- Project：同じ目的の作業とResultをまとめる
- History：過去の実行を探す
- Share：Resultを外部または限定相手へ見せる

実Data保存、検索、認可、URL発行、期限、停止等は接続確認前です。

---

## Settings・Accountの現在地

Settings、Account、Security、Plan、Credit、Billing、Developer ModeのRouteと画面経路はSourceにあります。

ただし、外部Storage、認証、Passkey、二段階認証、決済、Credit Ledger、Developer API等を本番利用可能とは案内しません。

詳細は次を確認してください。

- [Account・Security・Plan・Credit](account-security-and-billing.md)
- [Astera App Guide](app-guide.md)
- [App画面一覧](app-screen-map.md)

---

## 現在の公開範囲で試せること

このRepositoryでは、次を確認できます。

- Asteraの目的
- 8つの判断材料
- 入力方法の考え方
- 目的選択の種類
- App画面とRouteの構成
- Frontend Sourceに実装されている操作
- 具体的な入力・Output Sample

公開Sampleは[examples](../examples/README.md)にあります。

---

## 次に読む

- [現在の公開状態](current-status.md)
- [Astera App Guide](app-guide.md)
- [App画面一覧](app-screen-map.md)
- [Astera AppとAstera v8](app-and-runtime.md)
- [Asteraの仕組み](how-it-works.md)
- [公開Sample](../examples/README.md)
