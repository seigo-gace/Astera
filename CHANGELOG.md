# Changelog

AsteraのPublic Repositoryへ追加・更新した公式情報を記録します。

## 2026-08-05

### User-facing Documentation Overhaul

Public Repositoryを利用者目線で再監査し、Option、Developer Mode、Plan、料金、Creditが一か所で理解できない問題を修正しました。

#### New Documents

- `docs/options.md` — 現行4 Optionの内容、選び方、Credit、独立機能との違い
- `docs/plans-and-credits.md` — Plan、税込月額、月次Credit、追加Credit、Storage、計算式
- `docs/developer-mode.md` — API、Key管理、Sandbox、Usage、Credit停止・再開

#### Current Options

現在の正式な実行Optionを次の4種へ統一しました。

- 高精度翻訳
- エージェントモード
- 書類作成
- 外部Storage転送

旧表記の`文書生成`、`高度な書き換え`をPublic Documentationから除外しました。

Private Mode、暗号化、Astera Storage、Developer Modeは実行Optionではなく独立機能として分離しました。

#### Plans and Credits

次のCurrent Catalogを利用者向けに掲載しました。

| Plan | 税込月額 | 月次Credit |
|---|---:|---:|
| Free | 0円 | 初回20,000／以後10,000 |
| Basic | 980円 | 180,000 |
| Pro | 2,980円 | 640,000 |
| Business | 9,980円 | 2,200,000 |
| Enterprise | 29,800円 | 6,600,000 |

追加Credit Pack、自由購入、文字種とOption数によるCredit計算式、Astera Storageの月次CreditとPlan上限も追加しました。

#### Developer Mode

- 判断材料生成、根拠検索、判定、Astera統合、Webhook Gateway接続を説明
- Sandbox／Production Key、Scope、Rotate、Pause、Resume、削除を説明
- Usage、Credit、Rate、Quota、停止理由を説明
- Credit不足時は実行前拒否・非課金とする動作を説明
- Auto Resumeが他の停止理由を解除しないことを説明
- Deterministic Japanese Parser MCP、Skill Runtime、Vault、TGserverとの区分を整理

#### Rewritten Documents

次のPageを、内部監査中心の説明から利用者向けの機能・操作・選択基準へ書き換えました。

- `README.md`
- `docs/README.md`
- `docs/current-status.md`
- `docs/app-guide.md`
- `docs/getting-started.md`
- `docs/account-security-and-billing.md`
- `docs/integrations.md`
- `docs/app-screen-map.md`
- `docs/faq.md`
- `docs/press-kit.md`

提供状態の注意は`docs/current-status.md`へ集約し、各Pageで同じ内部実装・検証説明を繰り返さない構成へ変更しました。

## 2026-08-04

### Current-Scope Public Release

現在完成している範囲だけを、事実に基づいて公開できる状態へ修正しました。

- `docs/current-status.md`を追加し、現在の公開状態の正本とした
- 「仕様・設計」「Source実装」「公開環境での実動作確認」を分離した
- 現在完成しているAsteraの目的、8つの判断材料、Astera v8の処理構造、Use Case、公開Sampleを公開対象として確定した
- Astera Appの43 Route Pattern、入力、目的選択、Template、Option、Result Mapping、Turn、Copy、Markdown Download、Responsive Shell等をSource実装範囲として確定した
- File機能は、File名・Size・Type等のMetadataをFrontend Payloadへ含める段階であり、File本体Upload・内容解析は現在の公開実績に含めないことを明記した
- Production Web、Backend、Account、認証、Passkey、二段階認証、Project・History・Share保存、Storage、Plan、Credit、決済、Developer API、Native実機、Store公開を現在利用可能な機能として案内しない構成へ修正した
- Public Repositoryを、現在完成している範囲の公式公開先として`GO`と判定した

### Corrected Documents

- `README.md`
- `docs/README.md`
- `docs/app-guide.md`
- `docs/getting-started.md`
- `docs/app-and-runtime.md`
- `docs/app-screen-map.md`
- `docs/workspace-and-results.md`
- `docs/account-security-and-billing.md`
- `docs/mobile-and-accessibility.md`
- `docs/integrations.md`
- `docs/faq.md`
- `docs/press-kit.md`
- `SUPPORT.md`
- `SECURITY.md`

### Astera App Documentation

- READMEへAstera AppのProduct構成を追加
- 新しい実行、目的選択、File、Project情報、Template、Optionを説明
- Result、Turn、Project、History、Copy、Download、Shareを説明
- Settings、表示・言語、Storage、Data・Privacy、通知を説明
- Account、Password、Passkey、二段階認証、Backup Codeを説明
- Plan、Subscription、Credit、Checkout、Billing Statusを説明
- Developer Modeと外部Application連携を説明
- Web、Smartphone、Tablet、縦横画面、画面分割、Touch、Keyboard、Accessibilityを説明

### Public Examples

- 予約System変更の比較
- AIによる全面移行提案の検証
- 退職・独立判断
- 新Service公開判断

## 2026-08-03

### Added

- Asteraを初めて見る人向けのREADME
- Asteraのはじめかた
- Asteraの処理説明
- Astera AppとAstera v8の関係
- 活用例
- よくある質問
- 連携の基本説明
- Public Press Kit
- 入力と8つの判断材料の公開Sample
- Support、Security、Contribution、Code of Conduct
- LicenseとTrademark案内
- GitHub Issue Templates

### Purpose

Public Repositoryを、Asteraの価値、仕組み、利用方法、実例、問い合わせ先を誰でも理解できる公式案内場所として開始しました。
