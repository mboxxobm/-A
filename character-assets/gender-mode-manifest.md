# 男女版 / 裏モード基準アセット台帳

20体展開前の基準サンプル。既存の本職キャラを上書きせず、男性・女性と本職・裏モードを別ファイルで管理する。

## 一覧

比較用：[gender-mode-contact-sheet-v01.png](./gender-mode-contact-sheet-v01.png)

| キャラ | 男性・本職 | 女性・本職 | 男性・裏モード | 女性・裏モード |
|---|---|---|---|---|
| 騎士型 | [01-knight-m-v01.png](./main/male/01-knight-m-v01.png) | [01-knight-f-v01.png](./main/female/01-knight-f-v01.png) | [01-flag-protocol-m-v01.png](./hidden-mode/male/01-flag-protocol-m-v01.png) | [01-flag-protocol-f-v01.png](./hidden-mode/female/01-flag-protocol-f-v01.png) |
| 僧侶型 | [04-priest-m-v01.png](./main/male/04-priest-m-v01.png) | [04-priest-f-v01.png](./main/female/04-priest-f-v01.png) | [04-soft-reset-m-v01.png](./hidden-mode/male/04-soft-reset-m-v01.png) | [04-soft-reset-f-v01.png](./hidden-mode/female/04-soft-reset-f-v01.png) |

## 確認結果

- 8枚すべて 1254 × 1254 px
- 8枚すべて RGBA PNG
- 8枚すべてアルファ透過あり
- 既存の20体本職画像は上書きしていない
- 本職と裏モードで、キャラの顔・髪の基本形・象徴カラー・象徴アイテムを維持
- 男性版・女性版で髪型とシルエットを変えたが、人格や職能は変更していない

## 残り18体の命名規則

```text
character-assets/main/male/{id}-{slug}-m-v01.png
character-assets/main/female/{id}-{slug}-f-v01.png
character-assets/hidden-mode/male/{id}-{hidden-slug}-m-v01.png
character-assets/hidden-mode/female/{id}-{hidden-slug}-f-v01.png
```

## 設定の正本

- [gender-variant-character-settings.md](../gender-variant-character-settings.md)：男女版の全20体設定
- [dual-mode-character-settings.md](../dual-mode-character-settings.md)：本職・裏モードの全20体設定
- [character-settings-and-prompts.md](../character-settings-and-prompts.md)：元キャラ、セリフ、目差分、結果構成

