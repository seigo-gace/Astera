# Workspace・Result管理

このDocumentは、Astera App SourceにあるProject、History、Turn、Result、Shareの構成と、現在の実装状態を説明します。

Routeや画面がSourceへ存在することと、Server保存・検索・共有が本番で利用できることは別です。

最新の公開判定は[現在の公開状態](current-status.md)を確認してください。

---

## 現在の状態

| 領域 | Source状態 | 公開上の扱い |
|---|---|---|
| Result Section表示 | Source実装済み | Frontend構成として公開可能 |
| Turn Rail | Source実装済み | Frontend操作として公開可能 |
| Section／全体Copy | Source実装済み | Frontend操作として公開可能 |
| Markdown Download | Source実装済み | Frontend操作として公開可能 |
| 端末共有 | Source実装済み | Frontend操作として公開可能 |
| Project Route・画面 | Source実装済み | Server保存は未確認 |
| History Route・画面 | Source実装済み | 実Data取得・検索は未確認 |
| Result詳細Route | Source実装済み | Backend Result ID連携は未確認 |
| Public／Private Share Route | Source実装済み | URL発行・認可・停止は未確認 |

---

## 1. Result

Frontend Sourceは、Responseを次の8項目へ割り当てる構成です。

1. 本当の目的
2. 前提不足
3. 事実確認
4. 危機察知
5. 反対視点
6. 比較案
7. 推奨判断
8. 主役AIへの再指示

Result Sectionの表示、Section単位Copy、Result全体Copy、Markdown生成はSource実装として公開できます。

Responseを返すBackend EndpointとSchemaのProduction確認は、現在の公開実績には含めません。

---

## 2. Turn

一つの作業内で行う各実行をTurnとして扱う構成です。

現在のFrontend Sourceには次があります。

- Turn Rail
- Turn間移動
- Turn名変更
- Turn削除

想定するFlow：

```text
Turn 1：最初の相談
Turn 2：不足情報を追加
Turn 3：比較条件を変更
Turn 4：Riskを優先して再評価
Turn 5：最終判断用に整理
```

TurnをServerへ保存し、後日または別端末で取得する動作は未確認です。

---

## 3. Project

Project Routeと画面経路はSourceにあります。

設計上は、同じ目的に関係する次の情報をまとめます。

- 背景と目的
- 実行Result
- 関連File
- 比較候補
- 未確認事項
- 決定事項
- 見直し条件
- Share状態

現在公開できるのは、Project画面とAPI境界のSource実装です。

Project作成、保存、更新、削除、別Sessionでの再取得等はBackend接続確認前です。

---

## 4. History

History Routeと画面経路はSourceにあります。

設計上は、次の条件から過去の実行を探します。

- Title
- 日時
- 目的
- Project
- Result状態
- File
- Share状態

実History Dataの保存、検索、Paging、別端末同期等はBackend接続確認前です。

---

## 5. Result詳細

`/app/results/:id`のRoute Patternがあります。

設計上は、次を一緒に確認します。

- 元の入力
- 選択した目的
- 使用したTemplate・Option・File情報
- 実行日時
- Result状態
- 8つの判断材料
- Projectとの関係
- Share状態

BackendからResult IDを取得し、正しいDataを表示するProduction動作は未確認です。

---

## 6. Copy・Download・端末共有

現在のFrontend Sourceには次の操作があります。

### Section単位Copy

「前提不足だけ」「主役AIへの再指示だけ」等、必要なSectionを再利用します。

### Result全体Copy

8項目をまとめて別Documentや主役AIへ渡します。

### Markdown Download

見出し構造を保ったTextとして保存する処理があります。

### 端末共有

BrowserまたはNative Shellから、端末の共有機能へ渡す構成です。

これらはFrontend Source実装範囲です。実端末ごとの確認は[Mobile・Tablet・Accessibility](mobile-and-accessibility.md)の状態に従います。

---

## 7. Share

次のRoute Patternがあります。

```text
/s/:token
/share/:id
/app/shares
```

設計上の役割：

- Public Share：共有用URLからResultを表示する
- Private Share：Login・権限を前提にResultを表示する
- Share管理：期限、公開状態、停止等を管理する

現在公開できるのはRoute・画面構成です。

Token発行、認可、期限、停止、Data非公開化、URL無効化等のBackend動作は未確認です。

---

## 8. Fileとの関係

ProjectやResultへFileを関連付ける画面構成があります。

現在のFrontend Sourceで扱うのは、File名、Size、Type等のMetadataです。

File本体のUpload、保存、Download、内容解析、Project間共有は現在の公開実績に含めません。

---

## 9. 主役AIへの再利用

8番目の「主役AIへの再指示」と関連SectionをCopyし、別の生成AIへ渡す使い方はPublic DocumentationとSampleで説明できます。

例：

```text
【本当の目的】
...

【前提不足】
...

【危機察知】
...

【比較案】
...

【主役AIへの再指示】
...
```

これはAsteraの公開済みUse Caseです。

---

## 現在の公開範囲まとめ

| 項目 | 判定 |
|---|---|
| Resultの8 Section構成 | 公開可能 |
| Turn・Copy・Markdown・端末共有のSource実装 | 公開可能 |
| Project・History・Result詳細・ShareのRoute構成 | 公開可能 |
| Serverへの保存・検索・同期 | 未確認 |
| Share URL発行・認可・停止 | 未確認 |
| File本体保存・解析 | 未確認 |

---

## 関連Document

- [現在の公開状態](current-status.md)
- [Astera App Guide](app-guide.md)
- [App画面一覧](app-screen-map.md)
- [Asteraの仕組み](how-it-works.md)
