# Astera Documentation

AsteraのDocumentationは、初めて知る人、現在の公開範囲を確認する人、Astera AppのSource実装を理解したい人、判断の仕組みを確認したい人が、目的に合う順番で読めるように分かれています。

最初に[現在の公開状態](current-status.md)を確認してください。

このDocumentationでは、次を区別しています。

- **公開済み**：現在このRepositoryで外部へ示せる内容
- **Source実装済み**：画面・Route・Frontend処理がSourceに存在する状態
- **実稼働未確認**：Backend、認証、決済、Storage、Production、実機を含む確認前の状態

画面やRouteが存在するだけの機能を、現在利用可能とは表記しません。

---

## 初めてAsteraを知った人

次の順番で読むと、Astera全体と現在地をつかめます。

1. [Repository README](../README.md)
2. [現在の公開状態](current-status.md)
3. [Astera AppとAstera v8](app-and-runtime.md)
4. [Asteraの仕組み](how-it-works.md)
5. [公開Sample](../examples/README.md)

---

## 現在のApp Source実装を確認する人

| Document | 分かること |
|---|---|
| [Astera App Guide](app-guide.md) | 入力、目的、Result、Turn、Project、Settings、Account等のSource実装と接続状態 |
| [App画面一覧](app-screen-map.md) | 43 Route Pattern、各画面の役割、Source実装と実稼働の区別 |
| [操作Flow](getting-started.md) | 現在のSourceに沿った入力からResult再利用までの流れ |
| [Workspace・結果管理](workspace-and-results.md) | Project、History、Turn、Result、Shareの設計と現在地 |
| [Account・Security・Plan・Credit](account-security-and-billing.md) | Account関連Route・画面構成と外部接続の確認状態 |
| [Mobile・Tablet・Accessibility](mobile-and-accessibility.md) | Responsive Source対応と実端末確認状態 |
| [FAQ](faq.md) | 現在利用可能な範囲と、設計・実装中の範囲 |

---

## Asteraの判断処理を理解したい人

| Document | 分かること |
|---|---|
| [Asteraの仕組み](how-it-works.md) | 入力から8つの判断材料へ整理される工程 |
| [Astera AppとAstera v8](app-and-runtime.md) | App、Runtime、主役AIの役割分担 |
| [活用例](use-cases.md) | 日常、事業、契約、開発、AI回答Reviewでの使い方 |
| [公開Sample](../examples/README.md) | 具体的な入力と8項目のResult |

---

## 外部連携やDeveloper利用を検討する人

| Document | 分かること |
|---|---|
| [現在の公開状態](current-status.md) | Developer API、認証、決済、Storage等が現在の公開実績に含まれるか |
| [連携の考え方](integrations.md) | 主役AI、File、Storage、Share、認証、決済、Developer APIの設計上の関係 |
| [App画面一覧](app-screen-map.md) | Developer ModeやAccount画面のSource上の位置付け |
| [Support](../SUPPORT.md) | 質問、不具合、Security以外の連絡方法 |
| [Security Policy](../SECURITY.md) | Security問題の報告方法 |

---

## Asteraを紹介する人

| Document | 分かること |
|---|---|
| [現在の公開状態](current-status.md) | 現在、公開実績として紹介できる範囲 |
| [Press Kit](press-kit.md) | 正式名称、短い説明、標準紹介文、Product構成、英語説明 |
| [活用例](use-cases.md) | 具体的に何へ使えるか |
| [公開Sample](../examples/README.md) | 紹介に使える入出力例 |
| [Trademark](../TRADEMARKS.md) | Astera名称・Logoの扱い |

---

## Documentationを改善する人

- [Contributing](../CONTRIBUTING.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)
- [Changelog](../CHANGELOG.md)

Markdown内の相対Linkは、次のCommandで確認できます。

```bash
python3 scripts/check_docs.py
```

---

## 迷った場合

- Asteraが何か知りたい → [README](../README.md)
- 現在何が公開済みか知りたい → [現在の公開状態](current-status.md)
- App Sourceの内容を確認したい → [Astera App Guide](app-guide.md)
- 目的のRoute・画面を探したい → [App画面一覧](app-screen-map.md)
- Resultの意味を知りたい → [Asteraの仕組み](how-it-works.md)
- 実例を見たい → [公開Sample](../examples/README.md)
- Account・Credit・決済の現在地を知りたい → [Account・Security・Plan・Credit](account-security-and-billing.md)
- 問い合わせたい → [Support](../SUPPORT.md)
