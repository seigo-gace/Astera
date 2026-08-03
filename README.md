# Astera

> **問いを星図に変える。**

Asteraは、質問・相談・資料・計画・AIの回答をそのまま受け取るのではなく、**判断に必要な材料へ整理するための仕組み**です。

文章をきれいにすることより先に、目的、足りない前提、確認できる事実、危険、反対意見、比較できる案を整理します。その上で、人やAIがより納得できる判断を行える状態を作ります。

[公式サイト](https://asterav8.jp) ｜ [Astera App](https://app.asterav8.jp) ｜ [仕組みを読む](docs/how-it-works.md) ｜ [使い方を見る](docs/getting-started.md)

---

## Asteraを一言でいうと

**答えを急ぐ前に、判断の土台を作る仕組みです。**

たとえば、次のような質問があるとします。

> 新しいサービスを今月中に公開したい。すぐ作り始めるべきか？

普通は「作り方」や「おすすめの手順」から考え始めます。

Asteraは、その前に次を整理します。

- 本当に達成したいことは何か
- 今月中に公開する必要は本当にあるか
- 誰が使うのか
- 何が完成すれば公開できるのか
- 失敗した場合に何が起きるか
- 小さく試す方法はあるか
- 中止や延期を判断する条件は何か

その結果、勢いだけで進めるのではなく、**確認すべきことと、選ぶべき案が見える状態**になります。

---

## Asteraが整理する8つの判断材料

| 番号 | 判断材料 | 何が分かるか |
|---:|---|---|
| 01 | 本当の目的 | 表面的な質問の奥で、本当に達成したいこと |
| 02 | 前提不足 | 判断する前に確認しなければならない条件 |
| 03 | 事実確認 | 分かっていること、未確認のこと、推測 |
| 04 | 危機察知 | 失敗、損失、安全、運用上の危険 |
| 05 | 反対視点 | 見落としている反論や別の立場 |
| 06 | 比較案 | 同じ条件で比べられる複数の選択肢 |
| 07 | 推奨判断 | 現時点で最も妥当な判断と、その条件 |
| 08 | 主役AIへの再指示 | AIへ渡す場合の、より正確な依頼文 |

Asteraは、ひとつの結論を押しつけるものではありません。

**なぜその判断になるのか、何が変われば判断も変わるのか**を分かる形にします。

---

## Astera AppとAstera v8

Asteraは、利用者が操作する部分と、判断材料を作る部分に分かれています。

```text
利用者
  ↓
Astera App
入力・目的選択・結果確認・履歴・共有
  ↓
Astera v8
問いを分解し、判断材料を組み立てる
  ↓
利用者 または 主役AI
最終的な回答・計画・判断を作る
```

### Astera App

Asteraを使うための画面です。

- 質問や資料を入力する
- 比較、検証、改善、調査、計画などの目的を選ぶ
- 整理された結果を読む
- 履歴として残す
- 必要に応じて共有する

### Astera v8

入力された内容を、決められた処理順で分解・比較し、8つの判断材料へ組み立てる中核です。

Astera v8は生成AIそのものではありません。固定された処理とルールを使い、同じ条件では同じ順序で判断材料を作ることを目指しています。

詳しくは[Astera AppとAstera v8](docs/app-and-runtime.md)をご覧ください。

---

## どんな場面で使えるのか

Asteraは、正解をすぐに決めにくい場面ほど役立ちます。

- 複数の商品やサービスを比較する
- 企画や事業計画を見直す
- 契約や提案の見落としを確認する
- 開発方針や技術選択を比較する
- 障害や失敗の原因を整理する
- 転職、進路、住居などの選択肢を考える
- AIの回答に思い込みや不足がないか確認する
- 自分の考えを、他人へ説明できる形に整理する

具体例は[活用例](docs/use-cases.md)と[公開サンプル](examples/README.md)にまとめています。

---

## Asteraの使い方

最も簡単な使い方は次の3段階です。

1. 相談、質問、資料、計画をAsteraへ入れる
2. Asteraが8つの判断材料へ整理する
3. 自分で判断するか、その材料を主役AIへ渡して最終回答を作る

主役AIは、ChatGPT、Claude、Gemini、自作AIなど、用途に合うものを選べます。

詳しい手順は[はじめかた](docs/getting-started.md)をご覧ください。

---

## このRepositoryについて

このRepositoryは、Asteraを初めて知る人、利用を検討する人、連携を考える開発者へ向けた公式情報をまとめています。

```text
docs/      Asteraの説明、仕組み、使い方、FAQ
examples/  入力と判断材料の公開サンプル
.github/   問い合わせ・提案用のGitHub設定
```

---

## 開発者

Asteraは、**Seigo (`seigo-gace`) が個人で構想・設計・開発しているプロジェクト**です。

既存の生成AIを作り直すのではなく、AIや人が答えを出す前の「判断」を支える仕組みとして開発しています。

---

## English overview

**Astera turns questions into structured decision material before a person or an AI produces a final answer.**

It organizes the real objective, missing assumptions, known and unknown facts, risks, opposing views, comparable options, a recommended decision, and a refined instruction for a primary AI.

Astera consists of two main parts:

- **Astera App** — the user-facing application
- **Astera v8** — the deterministic runtime that builds decision material

Website: [asterav8.jp](https://asterav8.jp)
