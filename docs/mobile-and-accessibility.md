# Mobile・Tablet・Accessibility

このDocumentは、Astera App Sourceに実装されているResponsive・端末対応と、現在の実機確認状態を説明します。

Sourceに対応Codeや設定があることと、すべての端末で動作確認済みであることは同じではありません。

最新の公開判定は[現在の公開状態](current-status.md)を確認してください。

---

## 現在の状態

| 対象 | Source状態 | 公開上の扱い |
|---|---|---|
| Desktop Browser | Responsive Shell実装 | Production Browser確認前 |
| Smartphone Web | Header、Drawer、Safe Area、Keyboard対策 | 実端末Browser確認前 |
| Tablet Web | 幅、向き、Pointer、Resize対応 | 実Tablet確認前 |
| Android | Capacitor設定・Workflowあり | APK／AAB実Build・実機未確認 |
| iOS／iPadOS | Universal設定・Workflowあり | Simulator・実機未確認 |
| Foldable・Multi-window | Resize対応Sourceあり | 実機未確認 |
| Accessibility | Focus、Reduced Motion、Touch等の方針・Sourceあり | 総合実機検証前 |

---

## 1. 共通Frontend

Astera Appは、端末ごとに別のUI Sourceを複製せず、共通Frontendを画面幅、向き、入力方法に合わせて変化させる構成です。

```text
共通Frontend
├─ Desktop Browser
├─ Smartphone Browser
├─ Tablet Browser
├─ Android Native Shell
└─ iOS／iPadOS Native Shell
```

このArchitectureとResponsive Sourceは実装されています。

各配信経路でのProduction動作は別の確認対象です。

---

## 2. Responsive境界

Sourceでは主に次の画面幅を基準にします。

```text
Desktop : 1101px以上
Tablet  : 761〜1100px
Mobile  : 760px以下
Compact : 420px以下
Small   : 360px以下
```

固定Breakpointだけでなく、Visual Viewport、Pointer、Hover、Orientation、Window Resizeを扱う構成です。

---

## 3. Desktop

Desktop向けSourceには次が含まれます。

- Sidebar Navigation
- 広い入力・Result領域
- Turn Rail
- Project・HistoryへのNavigation
- Window幅変更への追従

Production Browserでの表示確認は現在の公開実績に含めません。

---

## 4. Smartphone Web

Smartphone向けSourceには次が含まれます。

- 固定Header
- Drawer Navigation
- 画面幅いっぱいの入力・Result
- Safe Area
- Software Keyboardを考慮した高さ調整
- Touch Target
- Hoverなしでも使える必須操作
- 横向き低Height対応

これらはSource実装範囲です。

実Android Browser、実iPhone Browserでの確認は未完了です。

---

## 5. Tablet

Tablet向けSourceには次が含まれます。

- 幅に応じたSidebar／Drawer
- 縦向き・横向き
- Window Resize
- Pointer、Mouse、Trackpad、Touch
- iPad Split View相当の幅変化
- Android Tablet／Foldable／Multi-window相当のResize

実Tabletでの操作確認は現在の公開実績に含めません。

---

## 6. OrientationとWindow Size変更

Sourceでは、画面の向きやSizeが変わった場合に、入力・選択・Result等の状態を維持することを前提にしています。

確認対象：

- 縦向きから横向き
- 横向きから縦向き
- Browser Window Resize
- Tablet画面分割
- Foldable開閉
- Software Keyboard表示・非表示

状態維持の実端末検証は未完了です。

---

## 7. Horizontal Overflow

Sourceでは、通常操作で不要な横Scrollを発生させない方針です。

- 長いTextの折り返し
- Button・Cardの可変幅
- Dialogの画面内配置
- Safe Areaを含む幅計算
- Code・URL・識別子の折り返しとCopy
- Sidebar／Drawer開閉時のLayout維持

実Browser Matrixでの総合確認は未完了です。

---

## 8. Touch操作

Touch対応Sourceでは次を重視します。

- 44〜48px以上を目安にしたTouch Target
- Button間隔
- Hover依存を避ける
- Swipe以外の操作手段を残す
- Delete・Share停止等の誤操作防止
- Scroll中の誤反応防止

実端末でのTouch精度・操作性確認は未完了です。

---

## 9. Keyboardと日本語入力

Sourceでは次を考慮します。

- 入力欄をSoftware Keyboardの下へ隠さない
- 実行Buttonへ到達できる
- Dialog内入力のScroll
- 日本語IME変換中の誤送信防止
- 改行と実行の分離
- Mobile Browserの意図しないZoom防止

実端末と各IMEでの確認は未完了です。

---

## 10. Theme・Reduced Motion

Sourceには次の表示設定があります。

- Light
- Dark
- System連動
- Reduced Motion

状態を色だけで伝えず、TextやIconを併用する方針です。

実画面でのContrast・視認性・Animation抑制確認は未完了です。

---

## 11. Keyboard・Screen Reader

Web Sourceでは次を目標にしています。

- Keyboardだけで主要操作へ移動する
- Focus位置を表示する
- Dialogを開いた後に適切な対象へFocusする
- Dialogを閉じた後に元の位置へ戻す
- Button、Link、入力欄へ意味のある名前を付ける
- Processing・完了状態を伝える
- 見出し順を保つ

Screen Reader、VoiceOver、TalkBack等の実機・実Browser総合確認は未完了です。

---

## 12. 古いBrowser・WebView

Sourceには、必要なWeb機能を確認し、非対応環境で壊れた画面を続行させないためのCompatibility処理があります。

含まれる方針：

- 必須Web機能の検査
- `randomUUID`等のFallback
- 古いWebViewへの更新案内
- `color-mix()`非対応Fallback
- `backdrop-filter`非対応Fallback

実古Version端末の確認は未完了です。

---

## 13. Android

Android向けにはCapacitor Native Shell、Phone／Tablet／Foldable／Multi-windowを想定した設定とWorkflowがあります。

現在の公開実績には次を含めません。

- APK実Build成功
- AAB実Build成功
- Android実機動作
- App Link
- Native共有
- Keyboard Resize
- Back操作
- Google Play公開

---

## 14. iOS・iPadOS

iPhone／iPad Universal、Orientation、Split View等を想定したCapacitor設定とWorkflowがあります。

現在の公開実績には次を含めません。

- Simulator Build成功
- iPhone実機動作
- iPad実機動作
- Universal Link
- Native共有
- TestFlight
- App Store公開

---

## 現在公開できる説明

現在、外部へ正しく説明できる内容：

- 共通Frontend SourceでDesktop、Smartphone、Tabletへ対応する構成
- Responsive Shell、Drawer、Safe Area、Visual Viewport、Touch等のSource実装
- Android／iOS Native Shell用の設定とWorkflow
- 古いBrowserや非対応機能で安全停止する方針

現在、動作確認済みとは説明しない内容：

- 実Smartphone・Tabletでの操作
- Android／iOS Build
- Native実機
- Store公開
- Screen Readerを含む総合Accessibility適合

---

## 関連Document

- [現在の公開状態](current-status.md)
- [Astera App Guide](app-guide.md)
- [App画面一覧](app-screen-map.md)
- [操作Flow](getting-started.md)
