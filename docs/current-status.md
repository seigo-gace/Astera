# Astera 現在の公開状態

最終更新：2026-08-05

このページでは、Asteraについて**現在確認できるもの、準備中のもの、まだ利用できないもの**をまとめています。

---

## 現在公開しているもの

| 内容 | 状態 |
|---|---|
| Asteraの目的と役割 | 公開済み |
| 8つの判断材料 | 公開済み |
| Astera v8の処理構造 | 公開済み |
| 活用例とInput・Output Sample | 公開済み |
| 追加Optionの仕様 | 公開済み |
| Plan・料金・Credit Catalog | 公開済み |
| Developer ModeとAPI管理仕様 | 公開済み |
| Appの画面構成と利用Flow | 公開済み |
| Support、Security、Contribution情報 | 公開済み |

現在のPublic Repositoryは、Asteraの仕組み、Appの設計、料金と機能、開発者向け利用方法を確認する公式案内場所です。

---

## 現在準備中のもの

| 内容 | 現在地 |
|---|---|
| Astera App | 画面とFrontend処理を実装中。Production公開前 |
| 高精度翻訳 | 仕様確定。Provider接続と品質検証前 |
| エージェントモード | Low・Medium・Highの仕様確定。実行環境検証前 |
| 書類作成 | Templateと書式保持仕様確定。外部連携検証前 |
| 外部Storage転送 | 一方向転送仕様確定。OAuthと転送検証前 |
| Private Mode | 保存しない処理方針と暗号化仕様確定。実環境検証前 |
| Astera Storage | 容量と月次Creditを確定。保存Backend検証前 |
| Account・Security | 画面とFlowを準備中。認証Provider実運用前 |
| Plan・Credit・決済 | Catalogを確定。契約・購入・Ledger実運用前 |
| Developer Mode | 画面とKey管理仕様を準備中。実Key発行・Endpoint公開前 |
| Android・iOS | 共通App構成を準備中。Store公開前 |

---

## 現在利用できないもの

現時点では、次を利用可能とは案内していません。

- Astera AppのProduction版
- Account登録・Loginの本番運用
- Plan契約とCredit購入
- Square決済
- File本体のUploadと内容解析
- Project、History、ShareのServer保存
- 外部Storageへの実転送
- Developer APIの実EndpointとAPI Key
- Android／iOS Store版

準備中の機能について、画面や仕様が存在することだけを理由に「現在使える」とは表示しません。

---

## 公開中のOption

現在の正式なOption構成は次の4種類です。

1. 高精度翻訳
2. エージェントモード
3. 書類作成
4. 外部Storage転送

Private Mode、暗号化、Astera Storage、Developer Modeは独立機能です。詳細は[追加Option](options.md)をご覧ください。

---

## 公開中のPlan Catalog

| Plan | 税込月額 | 月次Credit |
|---|---:|---:|
| Free | 0円 | 初回20,000／以後10,000 |
| Basic | 980円 | 180,000 |
| Pro | 2,980円 | 640,000 |
| Business | 9,980円 | 2,200,000 |
| Enterprise | 29,800円 | 6,600,000 |

これは現在確定しているCatalogです。契約・購入はAppの料金Pageと決済接続が公開された後に開始します。

追加CreditやStorageを含む詳細は[Plan・料金・Credit](plans-and-credits.md)をご覧ください。

---

## Developer Mode

Developer ModeはPro以上を対象とし、判断材料生成、根拠検索、判定、Astera統合などのAPIを管理する設計です。

現在はAPIの目的、Key管理、Credit停止・再開、Sandbox Explorer等の仕様を公開しています。実EndpointとKey発行はまだ提供していません。

詳細は[Developer Mode](developer-mode.md)をご覧ください。

---

## このRepositoryからInstallできるか

現在のPublic Repositoryは、Astera AppのInstall Packageや全Sourceを配布するReleaseではありません。

公開しているのは次です。

- 製品の目的と仕組み
- 利用Flowと画面説明
- Option、Plan、料金、Credit
- Developer Mode
- 公開Sample
- SupportとSecurity情報

---

## 更新方針

新しい機能の接続確認、実環境検証、公開が完了した場合は、このページを更新してから各Guideへ反映します。

---

## 関連Document

- [Repository README](../README.md)
- [追加Option](options.md)
- [Plan・料金・Credit](plans-and-credits.md)
- [Developer Mode](developer-mode.md)
- [Astera App Guide](app-guide.md)
- [公開Sample](../examples/README.md)
- [Changelog](../CHANGELOG.md)
