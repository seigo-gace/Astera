# Mobile・Tablet・Accessibility

Astera Appは、PCだけを前提にしたApplicationではありません。

同じ情報と操作を、Web Browser、Android、iPhone、iPad、Android Tablet、画面分割やWindow Size変更でも扱えるように設計されています。

このDocumentでは、端末ごとの見え方と、操作しやすさの考え方を説明します。

---

## 1. 共通の考え方

端末ごとに別のAsteraを作るのではなく、同じFrontendを画面幅、向き、入力方法に合わせて変化させます。

```text
共通Frontend
├─ Desktop Browser
├─ Smartphone Browser
├─ Android App
├─ iPhone App
├─ Android Tablet
└─ iPad
```

入力、Project、History、Result、Settings、Accountの内容は共通です。

---

## 2. PC

PCでは、広い画面を使って次を同時に確認しやすくします。

- Sidebar Navigation
- 実行履歴
- 入力欄
- 8つの判断材料
- Turn移動
- ProjectとHistory

長い結果を読みながら、別のTurnへ移動したり、必要な項目をコピーしたりする使い方に向いています。

---

## 3. スマートフォン

スマートフォンでは、常にSidebarを表示すると入力と結果が狭くなるため、HeaderとDrawerを使います。

主な特徴：

- 画面上部からMenuを開く
- 入力欄と結果を画面幅いっぱいに使う
- Turn数を小さな表示で確認する
- 必須操作はHoverなしで表示する
- 実行Buttonを明確に分ける
- Keyboard表示中も入力欄とButtonを確認できるようにする
- Safe Areaへ対応する

### 縦向き

入力と結果を上から下へ読む形です。

### 横向き

高さが小さくなるため、Header、Dialog、入力欄が画面を埋め尽くさないように調整します。

横向きになっても、操作を隠したり、横Scrollを前提にしたりしません。

---

## 4. Tablet

Tabletでは、スマートフォンより広い画面を使いながら、Touch操作を前提にします。

- 画面幅に応じてSidebarまたはDrawerを使う
- 縦向き・横向きの両方へ追従する
- iPadのSplit ViewやWindow Size変更を考慮する
- Android TabletやFoldableのResizeへ追従する
- Mouse、Trackpad、Touchのどれでも必須操作を使えるようにする

Tablet専用の別画面へ切り替えるのではなく、利用可能な幅に合わせて配置を変えます。

---

## 5. 画面向きが変わったとき

縦向きから横向き、横向きから縦向きへ変わった場合でも、次の状態を維持します。

- 入力中の文章
- 選択した目的
- 追加したFile
- 開いているResult
- 現在のTurn
- Dialogの内容

画面向きが変わるたびに、最初の画面へ戻したり、入力を消したりしないことを重視します。

---

## 6. 画面分割・Window Size変更

Tablet、Foldable、Desktopでは、利用中に画面幅が変わる場合があります。

Astera Appは、特定の機種名で判断するのではなく、現在利用できる画面幅、高さ、Pointer、Touch、向きを見て配置を変えます。

これにより、次のような使い方を想定します。

- iPadで別資料と並べて使う
- Android Tabletで2つのApplicationを並べる
- Foldableを開閉する
- Desktop BrowserのWindow幅を変える
- 外部Displayへ移動する

---

## 7. 横Scrollを発生させない

通常操作で画面が左右へぶれたり、不要な横Scrollが発生したりすると、入力と結果が読みにくくなります。

そのため、次を前提にします。

- 長い文字列を画面内で折り返す
- ButtonやCardを固定幅にしすぎない
- Tableは内容に応じて表示方法を変える
- Dialogを画面外へはみ出させない
- Safe Areaを含めて幅を計算する
- Sidebarを開いたときに本文を不自然に押し出さない

Code、URL、識別子など、長い一続きの文字列は、コピー可能な状態を保ちながら折り返します。

---

## 8. Touch操作

Touch端末では、Mouseより正確に小さな場所を押しにくいため、次を重視します。

- ButtonやLinkを押しやすい大きさにする
- Button同士を近づけすぎない
- Hoverしないと出ない必須操作を作らない
- Swipeだけを唯一の操作にしない
- File削除やShare停止などの重要操作を誤って押しにくくする
- Scroll中に入力やButtonが勝手に反応しないようにする

---

## 9. Keyboardと入力

スマートフォンでは、Software Keyboardが表示されると、利用できる画面の高さが大きく変わります。

Astera Appでは、次を考慮します。

- 入力欄がKeyboardの下へ隠れない
- 実行Buttonへ到達できる
- Dialog内の入力もScrollできる
- 日本語入力の変換中に誤送信しない
- 改行と実行を明確に分ける
- 入力文字が小さすぎてBrowser Zoomが起きないようにする

PCではKeyboard Shortcutを使える場合がありますが、スマートフォンでは画面上の実行Buttonを基本にします。

---

## 10. Light・Dark・System連動

表示Themeは、利用環境に合わせて選べます。

- Light
- Dark
- 端末設定へ連動

Themeを変えても、文字、Button、選択状態、Error、警告が見分けられることを重視します。

色だけで状態を伝えず、TextやIconも併用します。

---

## 11. 動きを抑える設定

Animationが負担になる利用者向けに、動きを抑える設定を扱います。

- Scroll Animationを短縮または停止する
- Processing表示の動きを抑える
- DialogやMenuのTransitionを抑える
- 端末のReduced Motion設定へ連動する

---

## 12. 文字と読みやすさ

- 入力文字を小さくしすぎない
- 長い結果を見出しで分ける
- 8項目の番号とTitleを固定する
- Error理由をCodeだけで終わらせない
- 専門用語へ説明を加える
- Button名をIconだけに依存しない

結果は、見た目の装飾よりも、順番と意味が分かることを優先します。

---

## 13. Keyboard・Screen Reader

Web Browserでは、Keyboardだけでも主要操作へ移動できることを目指します。

- Focus位置が分かる
- Dialogを開いた後、操作対象へFocusが移る
- Dialogを閉じると元の場所へ戻る
- Button、Link、入力欄へ意味のある名前を付ける
- Processingや完了を状態として伝える
- 見出し順を保つ

---

## 14. 古いBrowser・WebView

必要な機能が使えないBrowserや古いWebViewでは、画面が壊れたまま続行させず、更新や別の利用方法を案内します。

一部の見た目機能に対応していない場合でも、入力、Navigation、Result確認などの基本操作を優先します。

---

## 15. 端末を変えたとき

Accountへ保存される情報と、端末内だけに保存される設定があります。

端末を変えた場合は、次を確認します。

- Login
- Passkey
- 二段階認証
- 表示言語
- Theme
- Share状態
- Download済みFile
- 外部Storage接続

Passkeyは登録した端末や同期環境によって利用可否が異なるため、別のLogin方法も確保します。

---

## 関連Document

- [Astera App完全ガイド](app-guide.md)
- [はじめかた](getting-started.md)
- [Workspace・結果管理](workspace-and-results.md)
- [Account・Security・Plan・Credit](account-security-and-billing.md)
