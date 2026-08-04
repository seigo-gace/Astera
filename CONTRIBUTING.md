# Contributing to Astera

AsteraのPublic Documentation、公開Sample、案内文、Accessibility、公開環境の改善に関心を持っていただき、ありがとうございます。

このRepositoryでは、Asteraを初めて知る人、利用者、連携を検討する開発者が、**何のProductで、どう使い、どの画面で何ができるのかを理解できること**を重視しています。

---

## 参加できる内容

### Documentation

- 説明が分かりにくい箇所の改善
- 誤字、脱字、表記ゆれ
- 専門用語の説明追加
- Link切れ
- 古い機能説明の修正
- Astera Appの画面とDocumentの食い違い
- FAQの追加
- 初心者向け手順の改善

### 公開Sample

- 入力例
- 8つの判断材料の例
- 日常、事業、開発、AI回答ReviewのUse Case
- 事実と推測の分け方が分かる例
- 二択から第三案を作る例
- 開始条件、停止条件、Rollback条件を含む例

### Accessibility・端末対応

- Keyboard操作
- Screen Reader向け説明
- Smartphone・Tablet表示
- 縦向き・横向き
- 画面分割
- 不要な横Scroll
- Touch操作
- 読みやすい文字と見出し

### 公開環境のBug報告

- 画面が表示されない
- Linkが動かない
- Buttonが押せない
- Resultが読めない
- 特定端末で画面がはみ出す
- Public Shareの一般的な表示問題

Account、決済、Security、個人情報を含む内容は、公開Pull RequestやIssueではなく[SUPPORT.md](SUPPORT.md)と[SECURITY.md](SECURITY.md)を利用してください。

---

## 最初にIssueを作る場合

内容に合うIssue Templateを選びます。

- Documentation
- Public Bug
- Feature Request

### Issueに書くこと

- どのFileまたは画面か
- 現在の内容
- 何が分かりにくいか、または何が起きたか
- どう改善するとよいか
- 初めて読む人、利用者、開発者の誰に影響するか

同じ内容のIssueがないか検索すると、議論を一つにまとめられます。

---

## Pull Requestの流れ

1. RepositoryをForkする
2. 変更用Branchを作る
3. 対象Fileだけを修正する
4. Local Linkを確認する
5. 表示と文脈を読み直す
6. 変更理由を書いてPull Requestを作る

### Branch名の例

```text
docs/improve-app-guide
fix/broken-sample-link
docs/add-comparison-example
accessibility/mobile-navigation-copy
```

---

## Documentationの書き方

### 初めて読む人を基準にする

説明を読む人が、Asteraの内部構造や固有用語を知っている前提にしません。

### 最初に何のPageかを書く

Pageの冒頭で、何を理解できるDocumentなのかを説明します。

### 抽象語だけで終わらせない

「高品質」「高度」「最適化」だけでなく、何がどう変わるのかを書きます。

### 例を使う

悪い例：

```text
Asteraは判断を強化します。
```

良い例：

```text
AIが「全面移行すれば解決する」と答えた場合、Asteraは原因が確認されているか、局所改善や段階移行が可能か、TestとRollbackがあるかを整理します。
```

### 事実と予定を混ぜない

利用できると確認された機能、Source上の構成、将来の案を同じ表現にしません。

### Asteraと主役AIを分ける

- Astera：判断材料を作る
- 主役AI：最終文章や成果物へ仕上げる

### App全体を反映する

Astera Appを入力欄だけとして説明せず、必要に応じて次を含めます。

- 新しい実行
- 目的
- File・Project情報
- Result
- Turn
- Project
- History
- Share
- Settings
- Account・Security
- Plan・Credit
- Developer Mode
- Web・Smartphone・Tablet

---

## 用語と表記

| 対象 | 表記 |
|---|---|
| Product全体 | Astera |
| Application | Astera App |
| 中核Runtime | Astera v8 |
| 最終成果物を作るAI | 主役AI |
| 判断結果 | 8つの判断材料 |
| Tagline | 問いを星図に変える。 |
| 開発者 | Seigo / seigo-gace |

日本語文中で英単語を使う場合は、意味が伝わるように説明を加えます。

---

## 公開Sampleの形式

新しいSampleは、原則として次の構成にします。

```text
examples/
└─ sample-name/
   ├─ input.md
   └─ output.md
```

### input.md

- 背景
- 確認済み事実
- 候補
- 制約
- 避けたい失敗
- 何を整理してほしいか

### output.md

8つの見出しを使用します。

```text
01｜本当の目的
02｜前提不足
03｜事実確認
04｜危機察知
05｜反対視点
06｜比較案
07｜推奨判断
08｜主役AIへの再指示
```

Resultを絶対的な正解として書かず、成立条件と未確認情報を含めます。

---

## Link Check

Repositoryには、Markdown内の相対Linkを確認するScriptがあります。

```bash
python3 scripts/check_docs.py
```

Pull Requestでは、GitHub Actionsの`Documentation Check`も確認してください。

---

## Pull Requestに書くこと

- 何を変更したか
- なぜ変更したか
- 誰にとって分かりやすくなるか
- どのDocumentやSampleへ影響するか
- 確認した内容
- Link Checkの結果

### PR説明例

```text
## 変更
Astera App GuideへProject、History、Shareの説明を追加しました。

## 理由
現在は新しい実行だけが詳しく、継続利用の流れが分からないためです。

## 確認
- READMEからのLink
- app-guide.md内の相対Link
- python3 scripts/check_docs.py
```

---

## Reviewで確認すること

- 初めて読む人が理解できるか
- AppとRuntimeの役割が混ざっていないか
- 実際の画面や機能と食い違わないか
- 不要に難しい専門用語がないか
- 例があるか
- Local Linkが壊れていないか
- 個人情報や秘密情報が含まれていないか

---

## 行動規範

参加する際は[Code of Conduct](CODE_OF_CONDUCT.md)をご確認ください。

---

## 質問

Contributionに関する質問は、GitHub Issueまたは[Support](SUPPORT.md)からお知らせください。
