# キャラクター画像アセット台帳

実装前の初版アセット。すべて参考画像の画風を基準にした透明PNGです。

## 共通仕様

- 用途：キャラクター図鑑・診断結果カード用のSDキャラ
- 生成方式：内蔵画像生成、参考画像付きの新規生成
- 参照画像：[knight_cutout.png](/Users/th/Downloads/knight_cutout.png)、[priest_cutout_mask.png](/Users/th/Downloads/priest_cutout_mask.png)
- 出力：1254 × 1254 px、RGBA PNG、アルファ透過あり
- 背景：透明。マゼンタや黒はプレビュー上の表示であり、完成画像の背景として固定しない
- 共通画風：ちびキャラ、SD、2頭身、太めの輪郭、やわらかい陰影、表情豊か、全身中央配置
- 現在の状態：v01（初版、未採用確定）

## 20体の初版ファイル

一覧確認用：[contact-sheet-v01.png](./contact-sheet-v01.png)
Threads投稿用（番号・キャラ名ラベル付き）：[contact-sheet-threads-v01.png](./contact-sheet-threads-v01.png)

男女版・裏モードの基準8枚：[gender-mode-manifest.md](./gender-mode-manifest.md)

青年変身の方向性確認用：[transformation-demo/README.md](./transformation-demo/README.md)

ビジュアル方向性 v02（身長差・髪色・種族感）：[../character-visual-direction-v02.md](../character-visual-direction-v02.md)

| No. | キャラ | ファイル | 状態 | 主役の装備・特徴 |
|---:|---|---|---|---|
| 01 | 騎士型 | [01-knight-v01.png](./01-knight-v01.png) | 初版 | 銀の鎧、青いマント、木剣、青い光 |
| 02 | 戦士型 | [02-warrior-v01.png](./02-warrior-v01.png) | 初版 | 赤いはちまき、戦斧、前進するポーズ |
| 03 | 武闘家型 | [03-martial-artist-v01.png](./03-martial-artist-v01.png) | 初版 | オレンジ道着、拳の包帯、構え |
| 04 | 僧侶型 | [04-priest-v01.png](./04-priest-v01.png) | 初版 | 白緑ローブ、杖、癒やしの光、葉 |
| 05 | 魔法使い型 | [05-wizard-v01.png](./05-wizard-v01.png) | 初版 | 星の帽子、紫ローブ、魔導書 |
| 06 | 賢者型 | [06-sage-v01.png](./06-sage-v01.png) | 初版 | 青いローブ、眼鏡、巻物、幾何学魔法 |
| 07 | 盗賊型 | [07-thief-v01.png](./07-thief-v01.png) | 初版 | 灰色フード、短剣、コイン袋、地図 |
| 08 | 忍者型 | [08-ninja-v01.png](./08-ninja-v01.png) | 初版 | 黒い忍装束、手裏剣、巻物、効率ポーズ |
| 09 | 弓使い型 | [09-archer-v01.png](./09-archer-v01.png) | 初版 | 緑のレンジャー服、弓、葉の意匠 |
| 10 | 商人型 | [10-merchant-v01.png](./10-merchant-v01.png) | 初版 | 黄土色のコート、帳簿、硬貨、天秤 |
| 11 | 鍛冶屋型 | [11-blacksmith-v01.png](./11-blacksmith-v01.png) | 初版 | 茶色のエプロン、ハンマー、煤、工具 |
| 12 | 吟遊詩人型 | [12-bard-v01.png](./12-bard-v01.png) | 初版 | ピンクの衣装、リュート、音符、花びら |
| 13 | 航海士型 | [13-navigator-v01.png](./13-navigator-v01.png) | 初版 | 青い船長服、地図、コンパス、望遠鏡 |
| 14 | 王様型 | [14-king-v01.png](./14-king-v01.png) | 初版 | 小さな王冠、赤いマント、王笏、決断の手 |
| 15 | 召喚士型 | [15-summoner-v01.png](./15-summoner-v01.png) | 初版 | 紫ローブ、魔法陣、3体の小さな精霊 |
| 16 | 錬金術師型 | [16-alchemist-v01.png](./16-alchemist-v01.png) | 初版 | 青緑コート、ゴーグル、薬瓶、実験 |
| 17 | 竜騎士型 | [17-dragoon-v01.png](./17-dragoon-v01.png) | 初版 | 赤い竜騎士鎧、竜翼意匠、槍、跳躍 |
| 18 | 聖騎士型 | [18-paladin-v01.png](./18-paladin-v01.png) | 初版 | 金白の鎧、ハートの盾、守護の光 |
| 19 | 道化師型 | [19-jester-v01.png](./19-jester-v01.png) | 初版 | 赤桃の道化服、鈴帽子、ジャグリング |
| 20 | 番人型 | [20-guardian-v01.png](./20-guardian-v01.png) | 初版 | 濃灰の重装鎧、大盾、鍵穴の紋章 |

## 採用前のチェック項目

- [x] 20体すべてに初版ファイルがある
- [x] 全ファイルがPNGである
- [x] 全ファイルにアルファ透過がある
- [x] 全身と主役の装備がキャンバス内に収まっている
- [ ] 20体の顔・頭身・線の太さを並べて比較する
- [ ] キャラごとの色がアクセントカラー表と一致するか確認する
- [ ] 小さいカード表示でシルエットが識別できるか確認する
- [ ] 診断結果の文章と画像の印象が一致するか確認する
- [ ] v01から採用版（v02以降）を決める

## 設定の正本

- キャラ設定・セリフ・結果カード構成：[../character-settings-and-prompts.md](../character-settings-and-prompts.md)
- 元の詳細設定スナップショット：[../character-settings-memo.md](../character-settings-memo.md)
- 元の20体プロンプト：[Job-Character-Prompts.json](/Users/th/Downloads/Job-Character-Prompts.json)
- 元の140通りデータ：[Job-Character-140.json](/Users/th/Downloads/Job-Character-140.json)
