# Astera Appのはじめかた

このGuideでは、Asteraへ入力してから8つの判断材料を読み、結果を再利用するまでの流れを説明します。

現在の提供状態は[現在の公開状態](current-status.md)をご覧ください。

---

## Step 1｜整理したいことを書く

新しい実行画面で、質問・相談・計画・比較したい案・確認したいAI回答などを入力します。

次の情報があると、判断材料が具体的になります。

| 情報 | 内容 |
|---|---|
| 目的 | 最終的に何を決めたいか |
| 背景 | なぜ今この判断が必要か |
| 期限 | いつまでに決めるか |
| 制約 | 予算、人数、時間、使えない方法 |
| 候補 | 比較中の案 |
| 事実 | 数字、日時、実際に起きたこと |
| 推測 | まだ確認できていない考え |
| 避けたい失敗 | 損失、安全、信用、運用停止など |

入力例：

```text
現在使っている予約Systemを変更するか迷っています。
スタッフは5人です。候補はA、B、Cです。
価格よりも操作性と予約ミス防止を優先します。
移行期間、Support、障害時の戻しやすさも比較してください。
```

---

## Step 2｜目的を選ぶ

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

迷う場合は自動を選びます。比較したい場合は比較、計画の抜けを確認したい場合はReviewなど、今回一番重視する目的を選びます。

---

## Step 3｜必要なOptionを選ぶ

現在のOptionは4種類です。

| Option | 選ぶ場面 |
|---|---|
| 高精度翻訳 | 文書構造を保って翻訳したい |
| エージェントモード | 複数Stepで調査・確認したい |
| 書類作成 | 公式・個別Templateへ反映したい |
| 外部Storage転送 | 完成結果を自分のStorageへ送りたい |

必要のないOptionは選びません。Optionを追加すると予定Creditが増える場合があります。

詳しくは[追加Option](options.md)をご覧ください。

---

## Step 4｜Template・File・保存方法を確認する

### Template

Review、比較、計画、Risk確認などの判断用Templateや、書類作成用Templateを選びます。

### File

関連Fileを選び、入力欄へ「何を確認したいか」も書きます。

### Private Mode

通常の履歴やAstera Storageへ本文・File・結果を残したくない場合に使います。Private ModeはBasic以上、追加Creditなしの独立Modeです。

### 保存・転送

通常保存、端末Download、Astera Storage、外部Storage転送などから、利用できる方法を確認します。

---

## Step 5｜予定Creditを確認する

実行前に、入力量、Option、保存方法などから予定Creditを確認します。

Creditが不足している場合は処理を始めません。

利用者は次を選べます。

- Creditを追加する
- 入力を短くする
- 不要なOptionを外す
- 元の入力へ戻る

料金とCredit計算は[Plan・料金・Credit](plans-and-credits.md)をご覧ください。

---

## Step 6｜実行する

PCではEnterを改行、Ctrl／Command＋Enterを実行に使う設計です。Smartphoneでは画面上の実行Buttonを使います。

処理中は、情報確認、条件照合、比較、構造化などの進行を表示します。

---

## Step 7｜8つの判断材料を読む

1. 本当の目的
2. 前提不足
3. 事実確認
4. 危機察知
5. 反対視点
6. 比較案
7. 推奨判断
8. 主役AIへの再指示

最初は次の3つから読むと分かりやすくなります。

- **前提不足**：判断前に追加確認すること
- **危機察知**：失敗した場合の影響と停止条件
- **推奨判断**：現時点の方向と成立条件

その後、事実確認と比較案を読み、推奨理由を確認します。

---

## Step 8｜不足情報を追加する

前提不足や事実確認を読んで、情報を追加して再実行します。

```text
前回不足していた移行費用が分かりました。
Aは20万円、Bは5万円、Cは無料です。
ただしCは電話Supportがありません。
この条件を加えて再比較してください。
```

各実行はTurnとして移動・比較できる構成です。

---

## Step 9｜結果を再利用する

- 必要なSectionだけをCopyする
- Result全体をCopyする
- Markdownとして保存する
- 端末共有を使う
- Projectへまとめる
- Historyから探す
- Shareする
- 主役AIへ渡す

主役AIへ渡す場合は、8番目の再指示だけでなく、前提不足、危機察知、比較案も一緒に渡すと、判断条件を保ちやすくなります。

---

## Plan・Account・Developer Mode

- Planと月次Creditを確認する → [Plan・料金・Credit](plans-and-credits.md)
- AccountやSecurityを確認する → [Account・Security・Plan・Credit](account-security-and-billing.md)
- APIから利用する → [Developer Mode](developer-mode.md)

---

## 現在Repositoryで確認できること

- Asteraの目的と8つの判断材料
- 入力方法と目的選択
- 4つのOption
- Plan・料金・Credit Catalog
- Developer Mode仕様
- Appの画面Flow
- 公開Sample

Production App、契約、決済、実APIなどの提供状態は[現在の公開状態](current-status.md)で更新します。

---

## 次に読む

- [Astera App Guide](app-guide.md)
- [追加Option](options.md)
- [Plan・料金・Credit](plans-and-credits.md)
- [Developer Mode](developer-mode.md)
- [公開Sample](../examples/README.md)
