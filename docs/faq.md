# よくある質問

Asteraの仕組み、Option、Plan、Credit、Developer Mode、現在の提供状態についてまとめています。

---

## Astera

### AsteraはAIですか？

Astera v8は生成AIそのものではありません。質問や計画を、目的、前提、事実、危険、反対視点、比較案などの判断材料へ整理するRuntimeです。

### ChatGPT、Claude、Geminiとの違いは？

```text
Astera：答えを作る前の判断材料を整理する
主役AI：判断材料を使って文章・計画・Codeへ仕上げる
```

### 8つの判断材料は？

本当の目的、前提不足、事実確認、危機察知、反対視点、比較案、推奨判断、主役AIへの再指示です。

### Asteraが最終決定をしますか？

推奨判断は示しますが、最終決定を強制しません。成立条件、停止条件、別案も一緒に示します。

---

## 入力と目的

### 何を入力できますか？

質問、相談、比較案、企画、計画、AI回答、契約確認、障害状況、改善したい文章や設計などです。

### 何を書けば具体的になりますか？

目的、背景、期限、予算、人数、候補、確認済み事実、推測、避けたい失敗を書きます。

### 目的選択は何種類ですか？

自動、Review、比較、検証、改善、調査、計画、検討、判断、原因の10種類です。

---

## Option

### 現在のOptionは？

- 高精度翻訳
- エージェントモード
- 書類作成
- 外部Storage転送

### SettingsでOptionをONにすると課金されますか？

いいえ。SettingsのToggleは、Composerへ候補を表示するかを管理するだけです。実行前にOptionを選択し、予定Creditを確認して実行した場合だけ処理対象になります。

### 高精度翻訳とは？

見出し、段落、表、Code、URL、数字、Placeholder、情報量を維持して翻訳だけを行います。要約、改善、Tone変更、追記・削除は行いません。

### エージェントモードとは？

複数Stepで調査や確認を進めます。

- Low：最大3 Step、読取中心
- Medium：最大8 Step、外部書込前に承認
- High：最大15 Step、危険性のある操作ごとに承認

### 書類作成とは？

Astera公式Templateまたは個別Templateへ内容を反映します。Googleスプレッドシートでは指定CellやNamed Rangeだけを更新し、数式やLayoutを維持します。

### 外部Storage転送とは？

完成結果を利用者管理のStorageへ一方向にCopyします。転送後、Asteraは継続同期・編集・削除しません。

### Private ModeはOptionですか？

いいえ。Dataの保存方法を決める独立Modeです。Basic以上、追加Creditなしで、本文・File・結果を通常のHistoryやAstera Storageへ残さない設計です。

詳しくは[追加Option](options.md)をご覧ください。

---

## Planと料金

### Planはいくらですか？

| Plan | 税込月額 | 月次Credit |
|---|---:|---:|
| Free | 0円 | 初回20,000／以後10,000 |
| Basic | 980円 | 180,000 |
| Pro | 2,980円 | 640,000 |
| Business | 9,980円 | 2,200,000 |
| Enterprise | 29,800円 | 6,600,000 |

### 未登録でも試せますか？

合計7,500 Credit、最大5回、1回最大1,500 Creditの試用範囲を設ける設計です。未登録分はAccount作成後の残高へ合算しません。

### Basicの主な追加範囲は？

高精度翻訳、外部Storage転送、Private Mode、最大10GBのAstera Storageです。

### Proの主な追加範囲は？

書類Template、Developer Mode・API、最大100GBのAstera Storageです。

### BusinessとEnterpriseは？

- Business：月次2,200,000 Credit、最大500GB
- Enterprise：月次6,600,000 Credit、最大1TB

### エージェントモードの対象Planは？

利用条件は公開時点のCatalogへ表示します。確定前のPlan境界は固定しません。

詳しくは[Plan・料金・Credit](plans-and-credits.md)をご覧ください。

---

## Credit

### Creditはどう計算しますか？

- ASCII：1文字＝1 Credit
- 日本語・CJK等：1文字＝1.5 Credit
- 追加Option：1個ごとに入力換算量の50%を追加
- 出力文字数：減算しない

```text
floor(入力換算文字数 × (1 + 0.5 × Option数))
```

### 追加Creditはいくらですか？

| 価格 | Credit |
|---:|---:|
| 500円 | 75,000 |
| 1,000円 | 155,000 |
| 3,000円 | 480,000 |
| 10,000円 | 1,650,000 |
| 30,000円 | 5,000,000 |

自由購入は最低15,000 Credit、1 Credit＝0.007円です。

### Credit不足時は？

処理開始前に停止し、その実行分は消費しません。現在残高、予定Credit、不足量を表示します。

### 購入後に元の実行は自動開始しますか？

しません。元の入力へ戻り、再見積り後に利用者が実行します。

### Astera StorageのCreditは？

| 容量 | 月次Credit |
|---:|---:|
| 1GB | 3,000 |
| 10GB | 15,000 |
| 50GB | 50,000 |
| 100GB | 90,000 |
| 500GB | 350,000 |
| 1TB | 650,000 |

---

## Developer Mode

### 誰が使えますか？

Pro以上です。Pro未満では入口をLocked表示する設計です。

### 提供対象APIは？

判断材料生成、根拠検索、判定、Astera統合、Webhook Gateway接続です。

### API Keyで何を管理しますか？

Key発行、名前変更、Rotate、Pause、Resume、削除、Scope、Sandbox／Production、Usage、Credit、Rate、Quota、停止理由です。

### Key全文は後から見られますか？

発行直後に一度だけ表示します。紛失時は再表示せずRotateします。

### SandboxとProductionの違いは？

Sandboxは開発・接続Test用でExplorerを使います。Productionは実運用用でBrowser Explorerからの実行を禁止する設計です。

### APIでCredit不足になった場合は？

Astera本体へ送る前にRequestを拒否し、そのRequestのCreditは消費しません。

### Credit追加後は自動再開しますか？

Auto ResumeがONならCredit不足による停止だけを解除します。Security、Account、Plan、手動Pauseなど別の停止理由は解除しません。停止Request自体も自動再送しません。

### Deterministic Japanese Parser MCPとの関係は？

別Repositoryで公開する独立Projectです。Developer ModeのAPIとは分けて扱います。

詳しくは[Developer Mode](developer-mode.md)をご覧ください。

---

## File・Storage・Share

### File内容を解析できますか？

File本体Uploadと内容解析の提供状態は[現在の公開状態](current-status.md)で案内します。現在は利用可能とは案内していません。

### Astera Storageと外部Storage転送の違いは？

- Astera Storage：Astera Account内の保存容量
- 外部Storage転送：利用者管理のStorageへの一方向Copy

### Private ModeのResultは保存・Shareできますか？

通常のHistoryやAstera Storageへ保存せず、Shareもできない設計です。端末Downloadまたは対応する外部Storage転送で受け取ります。

---

## Account・Security

### GoogleやGitHubのPasswordをAsteraへ渡しますか？

渡しません。ProviderのPasswordを取得・流用しません。

### Passkeyと二段階認証は必須ですか？

任意です。

### 秘密情報をGitHub Issueへ書いてよいですか？

Password、Passkey、認証Code、Backup Code、API Key、Token、決済情報は書かないでください。[Security Policy](../SECURITY.md)に従ってください。

---

## 現在の提供状態

### Astera Appは今すぐ使えますか？

現時点ではProduction版を利用可能とは案内していません。このRepositoryでは、仕組み、画面、Option、Plan、Credit、Developer Mode、Sampleを公開しています。

### Plan契約やCredit購入はできますか？

現在はCatalog内容の公開段階です。Appの料金Pageと決済接続の公開後に開始します。

### Developer APIは使えますか？

現在は仕様公開段階で、実EndpointとAPI Key発行は準備中です。

最新情報は[現在の公開状態](current-status.md)をご覧ください。
