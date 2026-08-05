# AsteraのPlan・料金・Credit

このページでは、AsteraのPlan、月額料金、月次Credit、追加Credit、Storageを一つにまとめています。

> 以下は現在確定しているCommercial Catalogの内容です。実際の契約・購入は、Astera Appの`/pricing`と決済接続が公開された後に利用できます。現時点では購入可能とは案内していません。

---

## Plan一覧

| Plan | 税込月額 | 月次Credit | 主な対象 |
|---|---:|---:|---|
| Free | 0円 | 初回20,000／以後10,000 | 個人で基本処理を試したい人 |
| Basic | 980円 | 180,000 | 継続利用、Private Mode、翻訳・外部転送を使いたい人 |
| Pro | 2,980円 | 640,000 | 書類Template、Developer Mode・APIを使いたい人 |
| Business | 9,980円 | 2,200,000 | 利用量が多く、Storage容量を広げたい人 |
| Enterprise | 29,800円 | 6,600,000 | 最大利用枠と大容量Storageが必要な人 |

月次Creditは、Planの更新単位で付与する設計です。利用可能なOptionや上限は、公開中のCatalogに表示します。

---

## 未登録利用とFree

### 未登録

Accountを作成する前に、次の範囲で試せる設計です。

- 合計7,500 Credit
- 最大5回
- 1回最大1,500 Credit
- 未登録分は、Account作成後の残高へ合算しない

### Free

Accountが有効になった後、初回20,000 Creditを付与し、その後は月次10,000 Creditとする設計です。

---

## Planごとの主な違い

| 機能 | Free | Basic | Pro | Business | Enterprise |
|---|:---:|:---:|:---:|:---:|:---:|
| Asteraの基本処理 | ○ | ○ | ○ | ○ | ○ |
| 高精度翻訳 | ― | ○ | ○ | ○ | ○ |
| 外部Storage転送 | ― | ○ | ○ | ○ | ○ |
| Private Mode | ― | ○ | ○ | ○ | ○ |
| Astera Storage | ― | 最大10GB | 最大100GB | 最大500GB | 最大1TB |
| 書類Template | ― | ― | ○ | ○ | ○ |
| Developer Mode・API | ― | ― | ○ | ○ | ○ |
| エージェントモード | 公開Catalogの利用条件に従う | 公開Catalogの利用条件に従う | 公開Catalogの利用条件に従う | 公開Catalogの利用条件に従う | 公開Catalogの利用条件に従う |

`○`はPlan設計上の対象です。実際に利用できる機能は、公開時点のCatalogと[現在の公開状態](current-status.md)で確認してください。

Optionの詳しい内容は[追加Option](options.md)をご覧ください。

---

## Creditとは

Creditは、Asteraの実行量を管理する単位です。

主に次で使います。

- 通常の判断材料生成
- 高精度翻訳などの追加Option
- Developer API
- Astera Storageの月次利用

Creditは先に必要量を見積り、実行前に予約します。必要量を確保できない場合は処理を開始せず、その実行分のCreditも消費しません。

---

## 基本的なCredit計算

| 入力 | 換算 |
|---|---:|
| ASCII文字 | 1文字＝1 Credit |
| 日本語・CJK等 | 1文字＝1.5 Credit |
| 追加Option | 1個ごとに入力換算量の50%を追加 |
| 出力文字数 | 減算しない |

計算式：

```text
floor(入力換算文字数 × (1 + 0.5 × Option数))
```

### 計算例

日本語1,000文字を、Optionなしで実行する場合：

```text
1,000 × 1.5 = 1,500 Credit
```

同じ入力で高精度翻訳を追加する場合：

```text
1,500 × (1 + 0.5) = 2,250 Credit
```

実際の予定Creditは実行前の確認画面に表示します。

---

## 追加Credit Pack

| 価格 | 付与Credit |
|---:|---:|
| 500円 | 75,000 |
| 1,000円 | 155,000 |
| 3,000円 | 480,000 |
| 10,000円 | 1,650,000 |
| 30,000円 | 5,000,000 |

### 自由購入

- 最低15,000 Creditから
- 1 Credit＝0.007円
- 円未満は1円単位へ切り上げ

追加Creditの購入可否や有効条件は、公開時点のCatalogと購入画面に表示します。

---

## Astera Storage

Astera Storageは、結果やFileを保存するための契約容量です。Private Modeの本文や結果はAstera Storageへ保存しません。

| 容量 | 月次Credit |
|---:|---:|
| 1GB | 3,000 |
| 10GB | 15,000 |
| 50GB | 50,000 |
| 100GB | 90,000 |
| 500GB | 350,000 |
| 1TB | 650,000 |

### Planごとの選択上限

- Basic：10GBまで
- Pro：100GBまで
- Business：500GBまで
- Enterprise：1TBまで

Storage分のCreditは月次で減算し、残高不足時は保存停止や契約状態を明確に表示する設計です。

---

## Credit残高が少なくなった場合

Credit画面では、次を確認できる構成です。

- 利用可能残高
- 実行のために予約中の残高
- 概算の残り実行回数
- 使用・購入・返却・補填の履歴
- 低残高と不足状態
- Credit不足で停止しているDeveloper API

残高が少ない場合は、処理前に警告し、予定Creditと不足量を表示します。

---

## Creditが不足した場合

通常のApp実行では、次のように扱います。

```text
この実行にはCreditが不足しています。
処理は開始されておらず、Creditは消費されていません。
```

利用者は次を選べます。

- Creditを追加する
- 元の入力へ戻る
- 入力やOptionを減らして必要量を下げる

購入後も元の実行を勝手に開始しません。元の入力へ戻り、再見積り後に利用者がもう一度実行します。

Developer APIの停止・再開については[Developer Mode](developer-mode.md)をご覧ください。

---

## 決済後の状態

決済画面から戻っただけでは、PlanやCreditが反映済みとは扱いません。

画面では次の状態を分けます。

- 支払確認中
- Credit反映待ち
- 反映完了
- 失敗・取消
- 確認が必要

決済情報の確認とCredit Ledgerへの反映が完了してから、利用可能残高へ加えます。

---

## 料金を確認して契約する流れ

公開後は、Astera Appの料金Pageを唯一の料金・Plan選択画面とします。

```text
/pricingでPlanを比較
↓
Planを選択
↓
未Loginの場合は登録・Login
↓
選択Planを保持してCheckout確認へ戻る
↓
決済
↓
Billing Statusで反映状態を確認
```

公式HPには料金表を重複掲載せず、Astera Appの料金Pageへ案内します。

---

## 関連Document

- [追加Option](options.md)
- [Developer Mode](developer-mode.md)
- [Account・Security・Plan・Credit](account-security-and-billing.md)
- [現在の公開状態](current-status.md)
