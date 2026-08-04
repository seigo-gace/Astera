# Astera Documentation

AsteraのDocumentationは、初めて知る人、Astera Appを使う人、判断の仕組みを理解したい人、外部連携を検討する人が、目的に合う順番で読めるように分かれています。

---

## 初めてAsteraを知った人

次の順番で読むと、Astera全体をつかめます。

1. [Repository README](../README.md)
2. [Asteraのはじめかた](getting-started.md)
3. [Astera AppとAstera v8](app-and-runtime.md)
4. [Asteraの仕組み](how-it-works.md)
5. [公開サンプル](../examples/README.md)

---

## Astera Appを使う人

| Document | 分かること |
|---|---|
| [Astera App完全ガイド](app-guide.md) | 入力、目的、File、Result、Project、History、Settings、AccountなどApp全体 |
| [App画面一覧](app-screen-map.md) | 各画面の役割と、どこで何を行うか |
| [はじめかた](getting-started.md) | 初回実行からResultの保存・再利用まで |
| [Workspace・結果管理](workspace-and-results.md) | Project、History、Turn、Result、Share |
| [Account・Security・Plan・Credit](account-security-and-billing.md) | Login、Passkey、2FA、契約、Credit、決済 |
| [Mobile・Tablet・Accessibility](mobile-and-accessibility.md) | Smartphone、Tablet、画面向き、Touch、Keyboard |
| [FAQ](faq.md) | よくある疑問と困ったときの確認先 |

---

## Asteraの判断処理を理解したい人

| Document | 分かること |
|---|---|
| [Asteraの仕組み](how-it-works.md) | 入力から8つの判断材料へ整理される工程 |
| [Astera AppとAstera v8](app-and-runtime.md) | App、Runtime、主役AIの役割分担 |
| [活用例](use-cases.md) | 日常、事業、契約、開発、AI回答Reviewでの使い方 |
| [公開サンプル](../examples/README.md) | 具体的な入力と8項目のResult |

---

## 外部連携やDeveloper利用を検討する人

| Document | 分かること |
|---|---|
| [連携の考え方](integrations.md) | 主役AI、File、Storage、Share、認証、決済、Developer APIとの関係 |
| [App画面一覧](app-screen-map.md) | Developer ModeやAccount画面の位置付け |
| [Support](../SUPPORT.md) | 質問、不具合、Account問題の窓口 |
| [Security Policy](../SECURITY.md) | Security問題の報告方法 |

---

## Asteraを紹介する人

| Document | 分かること |
|---|---|
| [Press Kit](press-kit.md) | 正式名称、短い説明、標準紹介文、Product構成、英語説明 |
| [活用例](use-cases.md) | 具体的に何へ使えるか |
| [公開サンプル](../examples/README.md) | 紹介に使える入出力例 |
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
- Appを操作したい → [Astera App完全ガイド](app-guide.md)
- 目的の画面を探したい → [App画面一覧](app-screen-map.md)
- Resultの意味を知りたい → [Asteraの仕組み](how-it-works.md)
- 実例を見たい → [公開サンプル](../examples/README.md)
- Login・Credit・決済で困った → [Account・Security・Plan・Credit](account-security-and-billing.md)
- 問い合わせたい → [Support](../SUPPORT.md)
