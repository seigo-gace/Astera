# Astera App Guide

Astera Appは、相談や計画を入力し、8つの判断材料を確認・保存・再利用するためのApplicationです。

このGuideでは、利用者が画面で何を選び、結果をどう読むかを説明します。現在利用できる範囲は[現在の公開状態](current-status.md)をご覧ください。

---

## App全体

```text
Astera App
├─ 新しい実行
├─ Result・Turn
├─ Project・History
├─ Settings
├─ Account・Security
├─ Plan・Credit
├─ Developer Mode
└─ Share・Support
```

PCではSidebar、SmartphoneではHeaderとDrawer、Tabletでは画面幅に応じた配置を使います。

---

## 1. 新しい実行

新しい実行では、次を一つの画面で設定します。

- 整理したい内容
- 目的
- Option
- Template
- File
- Private Mode
- 保存・転送先
- 予定Credit

### 入力するとよい内容

- 最終的に決めたいこと
- 背景と期限
- 予算、人数、時間などの制約
- 比較中の候補
- 確認済みの事実
- まだ確認できていない推測
- 避けたい失敗

入力例：

```text
予約Systemを変更するか迷っています。
候補はA、B、Cです。
スタッフ5人が毎日使います。
価格だけでなく、操作性、移行の手間、Support、障害時の戻しやすさを比較してください。
```

---

## 2. 目的を選ぶ

| 目的 | 使う場面 |
|---|---|
| 自動 | 内容に合う確認方法を選びたい |
| Review | 資料や計画の抜けを確認したい |
| 比較 | 複数案を同じ条件で比べたい |
| 検証 | 根拠や結論が成立するか確認したい |
| 改善 | 現在案をより良くしたい |
| 調査 | 調べる項目を先に整理したい |
| 計画 | 順序、依存関係、停止条件を整理したい |
| 検討 | 方向を決める前に広く考えたい |
| 判断 | 最終選択と成立条件を整理したい |
| 原因 | 原因候補と確認順を整理したい |

目的は、今回一番重視したいものを選びます。

---

## 3. 追加Option

現在の正式なOptionは4種類です。

| Option | 内容 |
|---|---|
| 高精度翻訳 | 文書構造と情報量を維持して翻訳だけを行う |
| エージェントモード | Low・Medium・Highの複数Stepで作業を進める |
| 書類作成 | 公式・個別Templateへ内容を反映する |
| 外部Storage転送 | 完成した結果を利用者のStorageへ一方向転送する |

SettingsのToggleは、Composerに候補を表示するかを管理します。ToggleをONにしただけで実行・課金されることはありません。

Private Mode、暗号化、Astera Storage、Developer Modeは独立機能です。

詳しくは[追加Option](options.md)をご覧ください。

---

## 4. Template

Templateは、繰り返し使う確認方法や書式を選ぶ機能です。

### 判断用Template

- Review
- 比較
- 計画
- Risk確認

### 書類Template

- Astera公式Template
- 利用者が登録する個別Template

書類作成では、Googleスプレッドシートの指定CellやNamed Rangeだけを更新し、数式やLayoutを維持する設計です。

---

## 5. File

File Pickerでは、実行に関係するFileを選びます。

入力欄には、Fileを選ぶだけでなく、確認目的も書きます。

```text
添付した3社の見積書について、初期費用、月額、解約条件、追加料金を同じ表で比較してください。
```

現在の公開範囲ではFile選択画面とMetadata処理を説明しています。File本体のUpload・内容解析が利用可能になる時期は[現在の公開状態](current-status.md)で案内します。

---

## 6. Private Mode

Private Modeは、通常の履歴やAstera Storageへ本文・File・結果を残さず処理するための独立Modeです。

- Basic以上
- Composerを開いたとき既定ON
- 追加Creditなし
- 通常Modeへ勝手に切り替えない
- 結果は端末Downloadまたは外部Storage転送で受け取る
- Private Modeの本文はShareできない

Private Modeは追加Optionではなく、Dataの扱いを決める設定です。

---

## 7. 実行前確認

実行前に次を確認します。

- 入力内容
- 選択した目的
- OptionとMode
- Template
- File
- Private Mode
- 保存・転送先
- 予定Credit

Creditが足りない場合は処理を開始せず、不足量と変更できる項目を表示します。

---

## 8. 処理中

処理中は利用者向けに段階を表示します。

1. 判断材料を読み込む
2. 情報を確認する
3. 条件を照合する
4. 複数案を比較する
5. Resultを構造化する
6. 8つの項目へ整理する

停止操作を選んだ場合は、新しい処理を続けません。

---

## 9. Result

Resultは次の8項目で表示します。

1. 本当の目的
2. 前提不足
3. 事実確認
4. 危機察知
5. 反対視点
6. 比較案
7. 推奨判断
8. 主役AIへの再指示

最初は、**前提不足・危機察知・推奨判断**の3項目を見ると全体をつかみやすくなります。

その後、事実確認と比較案を読み、推奨が成立する理由を確認します。

---

## 10. Turn

一つの作業内で行った各実行をTurnとして扱います。

```text
Turn 1：最初の相談
Turn 2：不足情報を追加
Turn 3：比較条件を変更
Turn 4：Riskを優先して再評価
```

Turn間を移動し、名称変更や削除を行う構成です。

---

## 11. Resultの再利用

- Section単位でCopy
- Result全体をCopy
- Markdown Download
- 端末の共有機能へ渡す
- Projectへまとめる
- Historyから探す
- Shareを作成する
- 主役AIへ渡す

Project、History、ShareのServer保存は準備中です。提供状態は[現在の公開状態](current-status.md)をご覧ください。

---

## 12. ProjectとHistory

### Project

同じ目的に関係する実行、File、Result、判断変更をまとめます。

### History

過去の実行を日時、目的、Projectなどから探します。

古いResultを使う場合は、価格、期限、法律、人数、仕様などが変わっていないか確認します。

---

## 13. Settings

Settingsでは次を管理します。

- Optionの表示
- 表示言語とTheme
- 個別Template
- 外部Storage接続
- Astera Storage
- Data・Privacy
- 通知・Credit警告

Option表示をOFFにしても、契約や過去の実行を変更しません。

---

## 14. Plan・Credit

Plan画面では、現在Plan、月次Credit、利用可能な機能、Storage上限などを確認する構成です。

Credit画面では、残高、予約中Credit、概算残り実行回数、Pack、自由購入、使用履歴、返却・補填、Developer APIの停止状態を確認します。

詳しい金額と計算方法は[Plan・料金・Credit](plans-and-credits.md)をご覧ください。

---

## 15. Developer Mode

Pro以上の利用者向けに、API Key、Scope、Sandbox／Production、Usage、Credit、Rate、Quota、停止理由を管理します。

Developer Modeの機能と現在の提供状態は[Developer Mode](developer-mode.md)にまとめています。

---

## 16. Account・Security

Account画面では、Profile、Plan、Credit、Security状態を確認します。

Security画面では、Password、Passkey、二段階認証、Backup Code、接続Account、Sessionを管理する設計です。

本番認証の提供状態は[現在の公開状態](current-status.md)で案内します。

---

## 17. Smartphone・Tablet

- Smartphone：HeaderとDrawer、画面幅いっぱいの入力・Result
- Tablet：縦横表示、画面分割、Window Resize
- Touch端末：押しやすいButton、Hoverなしで必須操作を表示
- Keyboard表示中：入力欄と実行Buttonを隠さない
- PC：Enterは改行、Ctrl／Command＋Enterで実行する設計

詳細は[Mobile・Tablet・Accessibility](mobile-and-accessibility.md)をご覧ください。

---

## 関連Document

- [操作Flow](getting-started.md)
- [追加Option](options.md)
- [Plan・料金・Credit](plans-and-credits.md)
- [Developer Mode](developer-mode.md)
- [画面案内](app-screen-map.md)
- [現在の公開状態](current-status.md)
