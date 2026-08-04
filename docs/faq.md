# よくある質問

このFAQは、Asteraそのものと、現在Public Repositoryで公開できる範囲を説明します。

Appの画面やRouteがSourceへ存在することと、Productionで利用できることを分けて回答します。

最新の判定は[現在の公開状態](current-status.md)を確認してください。

---

## 現在の公開状態

### 今、Asteraは何を公開していますか？

現在公開している主な内容は次です。

- Asteraの目的と役割
- 8つの判断材料
- Astera v8の処理構造
- Use Case
- 入力・Output Sample
- Astera AppのFrontend Source実装範囲
- 43 Route Pattern
- Documentation、Support、Security、Contribution情報

---

### Astera Appは今すぐ本番利用できますか？

現在のPublic Repositoryでは、本番利用可能とは案内していません。

Frontend Sourceに画面、Route、入力、Result Mapping、Turn、Copy、Markdown Download、Responsive Shell等は実装されています。

Backend、認証、決済、Storage、Production環境、実端末を含む確認は別の段階です。

---

### 画面がSourceにあるなら、機能は完成しているのではありませんか？

画面・RouteのSource実装と、実際に機能が成立することは別です。

たとえばLogin画面があっても、Account Database、Session、Email、Provider接続等が確認されるまでは、本番Login可能とは表記しません。

同じ基準をProject、History、Share、Credit、決済、Developer APIにも適用します。

---

### 現在公開できるAppの実装は何ですか？

Source上で確認できる主な範囲は次です。

- 新しい実行画面
- 10種類の目的選択
- Templateと追加Optionの選択UI
- File選択UIとMetadata
- 処理段階表示
- 8 Section Result Mapping
- Turn Rail
- Section／全体Copy
- Markdown Download
- 端末共有
- 43 Route Pattern
- Desktop、Smartphone、Tablet向けResponsive Shell
- Android／iOS Native Shell用設定とWorkflow
- API未接続時に成功表示へ置き換えないFail-Closed方針

---

### 今後の機能まで完成したように書いていませんか？

現在は、Public Documentation全体で次を区別しています。

- 公開済み
- Source実装済み
- 接続確認前
- 実機確認前

未確認の機能を利用可能とは表記しません。

---

## Asteraについて

### AsteraはAIですか？

Astera v8は生成AIそのものではありません。

固定された処理順とRuleを使い、質問、相談、計画、AI回答等を8つの判断材料へ整理するRuntimeです。

---

### ChatGPT、Claude、Geminiとの違いは何ですか？

ChatGPT、Claude、Gemini等は、文章、説明、要約、提案、Codeを作ることが得意です。

Asteraは、その前に必要な目的、前提、事実、危険、反対視点、比較案を整理します。

```text
Astera ＝ 判断の骨組みを作る
主役AI ＝ 骨組みを使って最終成果物を作る
```

---

### Asteraだけでも使う考え方ですか？

はい。

8つの判断材料を自分で読み、選択肢の比較や最終判断へ使う設計です。

文章、計画、手順、Code等へ仕上げる場合は、主役AIへ渡します。

---

### Asteraが最終決定を強制しますか？

強制しません。

推奨判断だけでなく、前提不足、Risk、反対視点、別案、成立条件、停止条件を一緒に示す考え方です。

---

### 8つの判断材料は何ですか？

1. 本当の目的
2. 前提不足
3. 事実確認
4. 危機察知
5. 反対視点
6. 比較案
7. 推奨判断
8. 主役AIへの再指示

詳しくは[Asteraの仕組み](how-it-works.md)をご覧ください。

---

### 最新情報を自動で調べますか？

Asteraは、最新確認が必要な箇所や根拠不足を判断材料として整理する考え方です。

実際の価格、法律、製品仕様、News等は、公式Sourceや検索機能で確認する必要があります。

---

## Input・目的選択

### どんな内容を入力する想定ですか？

- 質問
- 相談
- 複数案の比較
- 計画
- AI回答
- 障害状況
- 契約確認
- 改善したい文章や設計
- 調査前の論点

等を想定しています。

---

### どのような情報を入れるとよいですか？

特に次が役立ちます。

- 目的
- 背景
- 期限
- 予算
- 人数
- 制約
- 候補
- 確認済みの事実
- 未確認の推測
- 避けたい失敗

---

### 目的選択はいくつありますか？

現在のFrontend Sourceには次の10種類があります。

- 自動
- Review
- 比較
- 検証
- 改善
- 調査
- 計画
- 検討
- 判断
- 原因

目的選択UIはSource実装済みです。

目的ごとのBackend Resultは接続確認前です。

---

### Templateは何ですか？

現在のSourceには、Review、比較、計画、Risk確認のTemplateがあります。

繰り返し使う確認観点を入力条件へ加えるためのUIです。

---

### 翻訳や文書生成Optionは使えますか？

高精度翻訳、文書生成、高度な書き換えの選択UIはSourceにあります。

各Optionの外部処理、品質、課金を含む実動作は、現在の公開実績には含めません。

---

## File

### Fileを追加できますか？

File選択UIとMetadataをPayloadへ含めるSourceがあります。

現在扱う構造は、File名、Size、Type等です。

---

### Fileの中身を解析できますか？

現在の公開実績には含めません。

File本体のUpload、Storage保存、内容抽出、解析、Result反映は接続確認前です。

---

### 4GBのFileを解析できますか？

Frontend SourceにFile Sizeを扱う設定があっても、4GBの実Upload・保存・解析が成立するとは表記しません。

File容量の実上限は、Backend、Storage、Network、Plan、解析処理の確認後に確定します。

---

## Result・Turn

### Resultはどのように表示しますか？

Responseを8つの判断材料へMappingするFrontend構成があります。

Backendから正しいResponseを受け取るProduction動作は確認前です。

---

### ResultをCopyできますか？

Section単位とResult全体のCopy処理はFrontend Sourceにあります。

---

### Markdownとして保存できますか？

Markdown生成・Download処理はFrontend Sourceにあります。

実Browser・実端末ごとの確認は端末検証の対象です。

---

### Turnとは何ですか？

一つの作業内で行った各実行です。

Turn Rail、Turn間移動、名称変更、削除のFrontend Sourceがあります。

Server保存と別Sessionからの再取得は確認前です。

---

## Project・History・Share

### Project画面はありますか？

Routeと画面経路はSourceにあります。

Project作成、保存、更新、削除、再取得等のBackend動作は確認前です。

---

### History画面はありますか？

Routeと画面経路はSourceにあります。

実Dataの保存、検索、Paging、別端末同期等は確認前です。

---

### Public ShareやPrivate Shareは使えますか？

Public Share、Private Share、Share管理のRouteはSourceにあります。

Token発行、認可、期限、停止、Data非公開化等のBackend動作は確認前です。

---

## Account・Security

### LoginやAccount登録はできますか？

Login、登録、Email確認、Password再設定等のRouteと画面経路はSourceにあります。

認証Backend、Email、Session、Provider接続を含む本番動作は確認前です。

---

### GoogleやGitHub Loginは利用できますか？

外部Providerを本人確認の入口として使う設計とFrontend境界があります。

Provider OAuth実接続は現在の公開実績に含めません。

ProviderのPasswordをAsteraが取得・流用しない方針です。

---

### Passkeyは利用できますか？

Security画面の設計にPasskeyがあります。

WebAuthn、端末Authenticator、登録、Login、削除等の実動作は確認前です。

---

### 二段階認証は利用できますか？

二段階認証Challenge Routeと管理設計があります。

TOTP、Backup Code、Recovery等の実動作は確認前です。

---

## Plan・Credit・決済

### 料金・Plan画面はありますか？

`/pricing`とPlan・Subscription画面のRouteはSourceにあります。

正式Catalog、契約Data、変更・解約等の実動作は確認前です。

---

### Creditとは何ですか？

Asteraの実行、Option、Developer API等の利用量を管理する設計上の単位です。

Credit画面のRoute・画面構成はありますが、Ledger、残高、購入、使用履歴等のBackend動作は確認前です。

---

### 決済できますか？

CheckoutとBilling StatusのRoute・画面構成があります。

外部決済、Webhook、署名検証、Plan・Credit反映、返金等は確認前です。

現在、決済可能とは案内しません。

---

## Developer API

### Developer Modeはありますか？

Developer ModeのRouteと画面構成はSourceにあります。

---

### APIを今利用できますか？

現在のPublic Repositoryでは提供中とは案内していません。

Endpoint、Schema、Key発行、Authentication、Rate Limit、使用量計測、課金等の確認後に正式Documentを公開します。

---

## Mobile・Tablet・Native App

### Smartphone向けSourceはありますか？

Header、Drawer、Safe Area、Touch Target、Keyboard対策等のResponsive Sourceがあります。

実Smartphone Browserでの確認は現在の公開実績に含めません。

---

### Tablet向けSourceはありますか？

Tablet幅、Orientation、Window Resize、Pointer等を扱うSourceがあります。

実Tablet、Split View、Foldable等の確認は未完了です。

---

### Android Appは公開されていますか？

公開済みとは案内していません。

Capacitor設定とWorkflowはありますが、APK／AAB実Build、実機、Google Play公開は確認前です。

---

### iPhone・iPad Appは公開されていますか？

公開済みとは案内していません。

Capacitor設定とWorkflowはありますが、Simulator、実機、TestFlight、App Store公開は確認前です。

---

## Public Repository

### このRepositoryからAppをInstallできますか？

現在のPublic Repositoryは、AppのInstall Packageや全Sourceを配布するReleaseではありません。

Asteraの目的、処理構造、App Source実装範囲、Sample、Documentationを公開するRepositoryです。

---

### Public Repositoryとして今公開してよい状態ですか？

現在完成している範囲を公開するRepositoryとしてはGOです。

ただし、Production App、Account、決済、Storage、Developer API、Native App等を利用可能機能として紹介することはNO-GOです。

公開範囲の正本は[現在の公開状態](current-status.md)です。

---

### 不具合やSecurity問題はどこへ報告しますか？

一般的な質問・不具合は[Support](../SUPPORT.md)、Security問題は[Security Policy](../SECURITY.md)を確認してください。

Password、Backup Code、API Key、決済情報、個人情報をPublic Issueへ書かないでください。
