# Astera Developer Mode

Developer Modeは、Asteraを自分のApplication、業務System、独自UI、Automationから利用するための開発者向け管理画面です。

対象はPro以上です。Pro未満でも入口と概要を確認できますが、API Key発行などの操作はLocked表示となる設計です。

> 現在、このページは確定しているDeveloper Mode仕様を公開するものです。実API Key発行と公開Endpointの提供は準備中です。[現在の公開状態](current-status.md)も確認してください。

---

## Developer Modeでできること

提供開始後は、次を一つの画面で管理します。

- 利用できるAPIを確認する
- Sandbox／Production用のAPI Keyを発行する
- Key名・Scope・接続先を確認する
- KeyをRotate、停止、再開、削除する
- Request数、使用Credit、残高を確認する
- Rate、Quota、Error、停止理由を確認する
- OpenAPIとCode例を見る
- Credit不足後の再開方法を設定する
- 緊急時に全Keyを一括停止する

---

## 提供対象のAPI

| API | 役割 |
|---|---|
| 判断材料生成 | 入力を8つの判断材料へ整理する |
| 根拠検索 | 判断に必要な根拠や確認対象を検索・整理する |
| 判定 | 条件と基準に基づいて結果を判定する |
| Astera統合 | 判断材料生成・根拠検索・判定を正規Flowで実行する |
| Webhook Gateway接続 | 完成したSystemとAccount単位で接続する |

API一覧では、表示名、目的、利用条件、Version、状態、必要Scopeを確認できる構成です。

### 別Project・提供対象外

- **Deterministic Japanese Parser MCP**は別Repositoryで公開する独立Projectです。Developer Modeの未完成APIとして扱いません。
- **Skill Runtime**は現在未構築のため、API一覧、Key発行、Explorerへ表示しません。
- **Vault**は安全性の確認が終わるまで発行対象にしません。
- **TGserver Self-hosted**はOpen Sourceの別区分で、AsteraのAPI Key・Plan・Credit対象外です。

---

## 画面上部で確認する情報

- Login中のAccount
- 利用中のWorkspace／Tenant
- Current Plan
- API利用資格
- 利用可能Credit
- 予約中Credit
- API全体の状態
- 低残高警告

これにより、「Keyがあるか」だけでなく、「今Requestを送れる状態か」を最初に確認できます。

---

## API Key一覧

各Keyでは次を表示します。

- Key名
- Prefix
- API Target
- Sandbox／Production
- Scope
- 現在の主状態
- 停止理由
- Credit補給後の自動再開ON／OFF
- 最終利用日時
- 今月のRequest数と使用Credit
- 概算の残りRequest数

利用者が行える主な操作：

- 詳細確認
- 名前変更
- Rotate
- Pause／Resume
- Revoke／削除

API Key全文は発行直後に一度だけ表示します。その後はPrefixだけを表示し、紛失した場合は既存Keyを再表示せずRotateします。

---

## SandboxとProduction

SandboxとProductionのKeyは分けます。

| Environment | 用途 | Explorer |
|---|---|---|
| Sandbox | 開発・接続Test | 利用可能 |
| Production | 実運用 | Browser上のExplorer実行は禁止 |

Production Keyの発行、Rotate、削除など重要な操作では、再認証を要求する設計です。

---

## API Keyの状態

| 表示 | 意味 | 主なAction |
|---|---|---|
| 稼働中 | 新しいRequestを受け付けられる | 停止／Rotate |
| Credit残量低下 | 現在は利用できるが停止が近い | Creditを追加 |
| Credit不足で停止中 | 新規Requestを実行前に拒否 | Creditを追加 |
| 補給確認中 | 決済またはCredit反映待ち | 状態を更新 |
| 補給済み・自動再開 | Credit不足の停止を解除済み | Requestを再送 |
| 補給済み・手動再開待ち | Auto ResumeがOFF | 再開 |
| 利用者が停止中 | 利用者自身がPause | 再開 |
| Plan変更で停止 | API利用資格がない | Planを確認 |
| Account停止 | Accountを利用できない | Accountを確認 |
| Security確認中 | 漏えい疑いなどで停止 | Security確認／Rotate |
| API提供側停止 | 対象APIが停止中 | Statusを確認 |
| 削除済み | Keyを再利用できない | 新規発行 |

Creditを追加しても、Security停止、Account停止、Plan停止、利用者によるPause、削除済み状態を勝手に解除しません。

---

## Credit不足時

Requestごとに、実行前に必要Creditを見積ります。

```text
API Request
↓
Key・Account・Scope・Planを確認
↓
必要Creditを見積り
↓
予約できる場合だけ実行
```

Creditが足りない場合：

- Astera本体へRequestを送らない
- 処理開始前に拒否する
- そのRequestのCreditは消費しない
- 現在残高と必要量を返す
- Credit追加先を案内する

停止されたRequestを、Credit購入後に勝手に再実行しません。Client側から再送します。

---

## Credit追加後の再開

決済画面から戻っただけでは再開しません。Credit反映を確認した後、Credit不足による停止だけを再評価します。

### Auto Resume ON

Credit不足の停止を解除します。他の停止理由がなければ稼働中へ戻ります。

### Auto Resume OFF

`補給済み・手動再開待ち`となり、利用者が再開Buttonを押します。

どちらの場合も、止められていたRequestそのものは自動送信しません。

---

## Usage・Logs

Key詳細では次を確認する構成です。

- Request数
- 使用Credit
- 成功・失敗
- Error理由
- Rate／Quota
- 停止・再開履歴
- API Version
- Request ID

Prompt本文、API Key全文、Secret、Providerの内部Errorなどを通常の利用履歴へ表示・保存しない設計です。

---

## API Explorer

ExplorerはSandbox専用です。

- Input Schemaを確認する
- Sample Requestを編集する
- 必要Creditと残高を送信前に確認する
- Response Schemaを確認する
- Error Codeを試す

Credit不足時は送信Buttonを無効化します。Production Keyを貼り付けて実行する画面にはしません。

---

## 利用開始までの流れ

```text
Pro以上のPlanを確認
↓
Developer Modeを開く
↓
利用するAPIを選ぶ
↓
Sandbox Keyを発行
↓
OpenAPIとSampleで接続Test
↓
UsageとCreditを確認
↓
必要に応じてProduction Keyを発行
```

---

## 現在の提供状態

現在Public Repositoryで公開しているのは、Developer Modeの目的、画面構成、Key Lifecycle、Credit停止・再開の仕様です。

次はまだ利用可能とは案内していません。

- 実API Key発行
- 公開Endpointへの接続
- Production API
- Usage・Logsの実Data
- Browser Explorerの実行
- API課金とCredit Ledgerの実連携

提供開始時は、このページと[現在の公開状態](current-status.md)を更新します。

---

## 関連Document

- [Plan・料金・Credit](plans-and-credits.md)
- [追加Option](options.md)
- [連携の考え方](integrations.md)
- [現在の公開状態](current-status.md)
