# Changelog

AsteraのPublic Repositoryへ追加・更新した公式情報を記録します。

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

次のDocumentから、未確認機能を現在利用可能と誤解させる表現を除き、Source実装状態と実稼働状態を明確に分けました。

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

### Publication Decision

| 判定対象 | 判定 |
|---|---|
| Asteraの目的・仕組み・8つの判断材料 | GO |
| Astera v8の処理構造・Use Case・公開Sample | GO |
| Astera Appの現在のFrontend Source実装範囲 | GO |
| Public Documentation・Support・Security情報 | GO |
| Astera Appを本番利用可能な完成Productとして案内 | NO-GO |
| Backend・認証・決済・Storage・API・Native Appを利用可能機能として案内 | NO-GO |

未完成機能の完成を待つのではなく、**現在完成している事実だけを公開する**方針で統一しました。

### Astera App Documentation

- READMEへAstera Appの実際のProduct構成を追加
- 新しい実行、目的選択、File、Project情報、Template、Optionの説明を拡充
- Result、Turn、Project、History、Copy、Download、Shareの利用フローを追加
- Settings、表示・言語、Storage、Data・Privacy、通知の説明を追加
- Account、Password、Passkey、二段階認証、Backup Codeの説明を追加
- Plan、Subscription、Credit、Checkout、Billing Statusの説明を追加
- Developer Modeと外部Application連携の説明を追加
- Web、Smartphone、Tablet、縦横画面、画面分割、Touch、Keyboard、Accessibilityの説明を追加

### New Documents

- `docs/app-guide.md` — Astera App Guide
- `docs/app-screen-map.md` — Astera Appの画面とRoute一覧
- `docs/workspace-and-results.md` — Project、History、Turn、Result、Share
- `docs/account-security-and-billing.md` — Account、Security、Plan、Credit、Billing
- `docs/mobile-and-accessibility.md` — Mobile、Tablet、画面向き、操作性
- `docs/integrations.md` — 主役AI、File、Storage、Share、認証、決済、Developer API
- `docs/README.md` — 利用目的別のDocumentation案内

### Expanded Documents

- `docs/getting-started.md`
- `docs/app-and-runtime.md`
- `docs/how-it-works.md`
- `docs/use-cases.md`
- `docs/faq.md`
- `docs/press-kit.md`
- `SUPPORT.md`
- `SECURITY.md`
- `CONTRIBUTING.md`

### Public Examples

次の入力例と8つの判断材料を追加しました。

- 予約System変更の比較
- AIによる全面移行提案の検証
- 退職・独立判断

既存の新Service公開例と合わせ、日常、事業、開発、AI回答ReviewでAsteraがどう使われるかを比較できる構成にしました。

### Repository Maintenance

- 古い簡易連携Pageを削除し、詳細な`docs/integrations.md`へ統合
- Documentationの読み順と目的別Navigationを追加
- Local Markdown Link CheckerとGitHub Actionsによる確認を維持

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
