# Asteraの連携

Asteraは、判断材料を整理するAstera v8、操作を行うAstera App、最終成果物を作る主役AI、利用者のStorageや業務Systemを役割ごとにつなぎます。

現在の提供状態は[現在の公開状態](current-status.md)をご覧ください。

---

## 全体像

```text
入力
↓
Astera App
↓
Astera v8が8つの判断材料を作る
↓
利用者が判断する
├─ 主役AIへ渡す
├─ 書類Templateへ反映する
├─ 端末へDownloadする
├─ Storageへ転送する
└─ Developer APIから業務Systemへ組み込む
```

---

## 主役AIとの連携

AsteraはChatGPT、Claude、Gemini、自作AIなどを置き換えません。

| 役割 | 内容 |
|---|---|
| Astera | 目的、前提、事実、Risk、反対視点、比較案を整理する |
| 主役AI | 判断材料を使って説明、計画、文章、Codeへ仕上げる |

ResultのSectionまたは全体をCopyし、主役AIへ渡す使い方を想定しています。

---

## File

Fileを使う場合は、Fileだけでなく確認目的も入力します。

```text
この見積書について、初期費用、月額、解約条件、追加料金を確認してください。
```

File本体のUploadと内容解析の提供状態は[現在の公開状態](current-status.md)で案内します。

---

## 書類作成

書類作成Optionでは、Astera公式Templateまたは利用者の個別Templateへ内容を反映します。

Googleスプレッドシートでは、原本を複製し、許可されたCell・Named Rangeだけを更新します。数式、Layout、Chart、保護範囲などへ意図しない変更があった場合は完成扱いにしません。

詳しくは[追加Option](options.md)をご覧ください。

---

## 外部Storage転送

外部Storage転送は、完成した結果を利用者管理のStorageへ一方向にCopyします。

- 接続先Accountを選ぶ
- 保存先Folderを選ぶ
- 転送する結果とFile名を確認する
- 転送後のObject IDと最終File名を確認する

Asteraは転送後のFileを継続同期・編集・削除しません。

Private Modeでは、結果を通常保存せず、端末Downloadまたは対応する外部Storage転送で受け取る設計です。

---

## Astera Storage

Astera Storageは、通常ModeのResultやFileをAstera Account内で保存する機能です。

- 1GB
- 10GB
- 50GB
- 100GB
- 500GB
- 1TB

から選択し、Planごとに上限があります。容量と月次Creditは[Plan・料金・Credit](plans-and-credits.md)をご覧ください。

Private Modeの本文・File・結果はAstera Storageへ保存しません。

---

## Project・History

### Project

同じ目的に関係する実行、File、Result、判断変更をまとめます。

### History

過去の実行を日時、目的、Project、状態から探します。

条件が変わった場合は古い結論をそのまま使わず、変更内容を加えて再実行します。

---

## Share

### Public Share

共有用URLからResultを見せる方法です。

### Private Share

指定されたAstera Accountだけが見られる共有です。

Private Modeの本文はShare対象にしません。

共有前に、個人情報、契約情報、顧客情報、API Key、非公開File名が含まれていないか確認します。

---

## Developer API

Developer Modeでは、AsteraをApplicationや業務Systemへ組み込むためのAPIを管理します。

- 判断材料生成
- 根拠検索
- 判定
- Astera統合
- Webhook Gateway接続

API Key、Scope、Sandbox／Production、Usage、Credit、Rate、Quota、停止理由を管理します。

詳しくは[Developer Mode](developer-mode.md)をご覧ください。

---

## Login連携

Login方法として、Email＋Password、Google、GitHub、Passkeyを扱う設計です。

GoogleやGitHubのPasswordをAsteraが取得・流用することはありません。

Account Securityでは、Password、Passkey、二段階認証、Backup Code、Session、接続Accountを管理します。

---

## 決済とCredit

Plan契約、追加Credit、Astera Storageは同じAccountとCredit状態へつながります。

```text
商品を選ぶ
↓
Checkoutで内容を確認
↓
外部決済
↓
Billing Statusを確認
↓
PlanまたはCreditへ反映
```

決済画面から戻っただけで反映済みとは扱いません。

料金、Credit Pack、計算式は[Plan・料金・Credit](plans-and-credits.md)をご覧ください。

---

## Private Mode

Private Modeは、通常の履歴・Storage・Shareへ本文や結果を残さず処理するModeです。

- Basic以上
- 追加Creditなし
- 通常保存へ自動切替しない
- 結果は端末Downloadまたは外部Storage転送
- Private Mode本文はShare不可

Private Modeは追加Optionではなく、Dataの扱いを決める独立機能です。

---

## 連携先で問題が起きた場合

Asteraは、接続できない状態を仮の成功結果で隠さない方針です。

- Storageへ転送できない → 転送失敗として表示
- Creditが足りない → 処理開始前に停止
- Loginが必要 → Login後に元の画面へ戻る
- APIが停止中 → 停止理由を表示
- 書類のLayoutが崩れた → 完成扱いにしない

---

## 関連Document

- [追加Option](options.md)
- [Plan・料金・Credit](plans-and-credits.md)
- [Developer Mode](developer-mode.md)
- [Account・Security・Plan・Credit](account-security-and-billing.md)
- [現在の公開状態](current-status.md)
