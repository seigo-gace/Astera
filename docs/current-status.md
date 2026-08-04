# Astera 現在の公開状態

最終更新：2026-08-04

このページは、Asteraについて**現在公開できる状態まで到達している範囲**を示す正本です。

Asteraでは、次の3つを同じ意味として扱いません。

1. 仕様・設計が決まっている
2. Sourceへ実装されている
3. 公開環境で実際に利用できることを確認している

このPublic Repositoryで公開実績として扱うのは、以下の範囲です。

---

## 現在公開しているもの

| 領域 | 現在の状態 | このRepositoryで確認できるもの |
|---|---|---|
| Asteraの目的 | 公開済み | 判断材料生成レイヤーとしての役割、生成AIとの違い |
| 8つの判断材料 | 公開済み | 本当の目的、前提不足、事実確認、危機察知、反対視点、比較案、推奨判断、主役AIへの再指示 |
| Astera v8の処理構造 | 公開説明済み | 入力を分解・比較・構造化する考え方と処理順 |
| 活用方法 | 公開済み | 日常、事業、開発、AI回答確認などのUse Case |
| 入出力例 | 公開済み | 具体的な入力と8項目のOutput Sample |
| Public Documentation | 公開済み | README、仕組み、App構成、Security、Support、FAQなど |
| Documentation検査 | Repositoryへ実装済み | Markdown相対Link CheckerとGitHub Actions Workflow |

---

## Astera Appの現在地

Astera Appは、React、TypeScript、Vite、Capacitorの共通Sourceで、Web、Android、iOSへ展開する構成です。

現在のSourceには、次の範囲が実装されています。

- 43のRoute Pattern
- 新しい実行画面
- 10種類の目的選択
- Templateと追加Optionの選択UI
- 処理段階の表示
- 8つの判断材料へのResult Mapping
- Turn移動
- Section単位とResult全体のCopy
- Markdown Download
- 端末共有
- Project、History、Settings、Account、Security、Plan、Credit、Developer、Share、Legal、Status、Supportの画面経路
- Desktop、Smartphone、Tablet向けResponsive Shell
- Android／iOS Native Shell用の設定とWorkflow
- API未接続・不整合時に成功表示へ置き換えないFail-Closed方針

これらは**Source実装範囲**です。すべてを本番利用可能とする表記ではありません。

---

## 現在の公開実績に含めないもの

次の項目は、接続・実環境・実機での確認が完了するまで、現在利用可能な機能として扱いません。

- Cloudflare上のProduction表示
- Backend EndpointとResponse Schemaの実接続
- File本体のUploadと内容解析
- Project、History、ShareのServer保存
- Account登録、Login、Passkey、二段階認証の実運用
- Plan、Credit、Checkout、Billingの決済連携
- 外部Storage接続
- Developer APIの提供
- Android APK／AABの実Buildと実機確認
- iOS／iPadOSのSimulator・実機確認
- Google Play／App Store公開

画面やRouteがSourceに存在していても、外部ServiceやBackendを含む動作確認が終わるまでは、利用可能とは表記しません。

---

## File機能の現在地

現在のFrontend Sourceでは、選択したFileの名称、Size、TypeなどのMetadataを実行Payloadへ含める構造があります。

File本体をUploadし、内容を読み取って判断材料へ反映する動作は、現在の公開実績には含めません。

そのため、Public Documentation上でも「Fileを追加できる画面があること」と「File内容を解析できること」を分けて説明します。

---

## このPublic Repositoryの位置付け

現在のPublic Repositoryは、次の目的で公開しています。

- Asteraが何を解決する仕組みかを伝える
- Astera v8とAstera Appの役割を説明する
- 8つの判断材料と具体例を確認できるようにする
- 現在のSource実装範囲と実稼働確認範囲を混同させない
- 開発の進行に合わせて、公開できる事実を更新する

現在のRepositoryは、Astera AppのInstall Packageや全Sourceを配布するReleaseではありません。

---

## 公開判定

| 判定対象 | 判定 |
|---|---|
| Asteraの構想・仕組み・判断材料の公開 | GO |
| Public DocumentationとSampleの公開 | GO |
| 現在のApp Source実装範囲の紹介 | GO |
| Astera Appを本番利用可能な完成Productとして案内 | NO-GO |
| Account・決済・Native App等を利用可能機能として案内 | NO-GO |

新しい接続検証や実機確認が完了した場合は、このページを先に更新してから各Documentへ反映します。

---

## 関連Document

- [Repository README](../README.md)
- [Astera Documentation](README.md)
- [Astera AppとAstera v8](app-and-runtime.md)
- [Astera App Guide](app-guide.md)
- [公開Sample](../examples/README.md)
- [Changelog](../CHANGELOG.md)
