# キャラクター設定 & 画像生成プロンプト 正本メモ

> 実装前の設定資料。キャラクター20体の世界観・性格・見た目と、SDイラスト生成用プロンプトを一つにまとめたもの。
> このファイルは設定を固めるためのメモであり、アプリ本体の実装・公開状態は変更していない。

## 1. 設計の基本

- 診断の軸1：キャラタイプ20体（性格・戦い方）
- 診断の軸2：職能ロール7タイプ（会社での役割）
- 組み合わせ：20 × 7 = 140通り
- 結果名の基本形：`{キャラ名}の{職能ロール}`
- キャラ設定の詳細は、先に保存した [character-settings-memo.md](./character-settings-memo.md) を基礎にしている。
- 140通りの結果データは、入力元の [Job-Character-140.json](/Users/th/Downloads/Job-Character-140.json) を参照する。
- 画像用プロンプトは、入力元の [Job-Character-Prompts.json](/Users/th/Downloads/Job-Character-Prompts.json) を反映する。

## 2. 参考画像とビジュアル方針

### 参考画像

- [knight_cutout.png](/Users/th/Downloads/knight_cutout.png)：騎士型の基準。銀色の鎧、青いマント、木剣、勇敢な笑顔。
- [priest_cutout_mask.png](/Users/th/Downloads/priest_cutout_mask.png)：僧侶型の基準。白と緑のローブ、杖、やわらかい光、穏やかな笑顔。
- どちらも 1600 × 1600 px、RGBA PNG、透明領域あり。
- ImageMagickで確認した描画領域は、騎士型 `1112 × 1311 + 252 + 155`、僧侶型 `1079 × 1302 + 251 + 168`。
- プレビュー環境によって透明部分がマゼンタに見える場合がある。マゼンタを完成画像の背景色として固定せず、納品時はアルファ透過を正とする。

### 共通の画風設定

- ちびキャラ、SD、2頭身、頭が大きく体が小さい、かわいいデフォルメ
- RPG職業クラスのシルエットを一目で判別できる
- 表情豊か、やわらかい陰影、ゲームアイコン／診断結果カード向け
- 全身が画面内に収まり、中央寄せ。武器や道具は1点を主役にする
- 各キャラのアクセントカラーを衣装・小物・光の演出に反映する
- 文字、ロゴ、透かし、余計な手足、成人体型、写実表現は入れない
- 背景は透明。生成サービスが透明を扱えない場合だけ白背景で生成し、後工程で切り抜く
- 騎士型と僧侶型の線の太さ、顔の大きさ、目の表情、全身の余白感を20体の共通基準にする

### v02 ビジュアル方向性

- 成人変身後の身長・体格・頭身はキャラごとに変え、20体を同じ体型にそろえない。
- 髪色と衣装色は独立させる。髪色は性格・種族感、衣装色は職能・機能性から決める。
- 参考画像の影響は約20%に限定し、表情の豊かさ、優雅さ、冒険感、モンスター質感などの抽象要素だけを採用する。
- 賢者型には氷雪系の透明感、戦士型には角・鱗・牙・爪などのクリーチャー質感を少量追加できる。
- 20体の身長差、髪色差、性別表現、メガネやゴーグルなどの顔まわりの差を、識別性のために積極的に使う。
- 詳細な基準と仮身長表は [character-visual-direction-v02.md](./character-visual-direction-v02.md) にまとめる。

### 共通プロンプトの骨格

日本語：
`ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、{テーマ}、大きな頭と小さな体、表情豊か、やわらかい陰影、全身、中央配置、ゲームアイコン風、透明背景、文字なし`

英語：
`chibi {class} character, SD style, 2 heads tall, cute deformed, RPG job class, {theme} theme, big head small body, expressive face, soft shading, full body, centered composition, game icon style, transparent background, no text`

共通ネガティブ：
`realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion, text, logo, watermark`

> 入力JSONの既存プロンプトはそのまま保存し、上の共通骨格は今後の再生成・品質統一用のルールとして扱う。英語プロンプト内にある日本語テーマ語は、モデルによっては日本語のままでもよいが、再現性を優先する場合は英語テーマへ置き換える。

## 3. キャラクター設定20体



## 4. 画像生成プロンプト20本

以下を各キャラの現行プロンプトとする。画像生成時は「共通の画風設定」を前置きし、必要に応じてポーズや表情だけを差し替える。

#### 01. 騎士型 / Knight

- **アクセントカラー：** `#3B82F6`
- **テーマ：** 理想・正義・忠誠のイメージ
- **日本語プロンプト：** `騎士型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、理想・正義・忠誠のイメージ、表情豊か`
- **英語プロンプト：** `chibi Knight character, SD style, 2 heads tall, cute deformed, RPG job class, 理想・正義・忠誠 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, silver armor with blue cape, holding small wooden sword, brave smile, shining eyes`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 02. 戦士型 / Warrior

- **アクセントカラー：** `#EF4444`
- **テーマ：** 情熱・行動・勝利のイメージ
- **日本語プロンプト：** `戦士型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、情熱・行動・勝利のイメージ、表情豊か`
- **英語プロンプト：** `chibi Warrior character, SD style, 2 heads tall, cute deformed, RPG job class, 情熱・行動・勝利 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, red headband, battle axe, muscular but chibi, passionate pose`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 03. 武闘家型 / Martial Artist

- **アクセントカラー：** `#F97316`
- **テーマ：** 現場・体現・ストイックのイメージ
- **日本語プロンプト：** `武闘家型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、現場・体現・ストイックのイメージ、表情豊か`
- **英語プロンプト：** `chibi Martial Artist character, SD style, 2 heads tall, cute deformed, RPG job class, 現場・体現・ストイック theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, martial arts gi, fist bandages, stoic training pose, sweatband`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 04. 僧侶型 / Priest

- **アクセントカラー：** `#10B981`
- **テーマ：** 共感・傾聴・癒やしのイメージ
- **日本語プロンプト：** `僧侶型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、共感・傾聴・癒やしのイメージ、表情豊か`
- **英語プロンプト：** `chibi Priest character, SD style, 2 heads tall, cute deformed, RPG job class, 共感・傾聴・癒やし theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, white and green priest robe, holding staff with soft light, gentle smile, healing aura`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 05. 魔法使い型 / Wizard

- **アクセントカラー：** `#8B5CF6`
- **テーマ：** 発想・天才・奇抜のイメージ
- **日本語プロンプト：** `魔法使い型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、発想・天才・奇抜のイメージ、表情豊か`
- **英語プロンプト：** `chibi Wizard character, SD style, 2 heads tall, cute deformed, RPG job class, 発想・天才・奇抜 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, pointy hat with stars, purple robe, holding glowing spellbook, mischievous grin`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 06. 賢者型 / Sage

- **アクセントカラー：** `#6366F1`
- **テーマ：** 論理・分析・冷静のイメージ
- **日本語プロンプト：** `賢者型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、論理・分析・冷静のイメージ、表情豊か`
- **英語プロンプト：** `chibi Sage character, SD style, 2 heads tall, cute deformed, RPG job class, 論理・分析・冷静 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, long blue robe, glasses, holding ancient scroll, wise calm expression`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 07. 盗賊型 / Thief

- **アクセントカラー：** `#6B7280`
- **テーマ：** 機敏・要領・情報のイメージ
- **日本語プロンプト：** `盗賊型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、機敏・要領・情報のイメージ、表情豊か`
- **英語プロンプト：** `chibi Thief character, SD style, 2 heads tall, cute deformed, RPG job class, 機敏・要領・情報 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, hooded cloak, dagger, coin pouch, sly cute smirk`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 08. 忍者型 / Ninja

- **アクセントカラー：** `#1F2937`
- **テーマ：** 効率・裏方・段取りのイメージ
- **日本語プロンプト：** `忍者型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、効率・裏方・段取りのイメージ、表情豊か`
- **英語プロンプト：** `chibi Ninja character, SD style, 2 heads tall, cute deformed, RPG job class, 効率・裏方・段取り theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, black ninja outfit, shuriken, efficient pose, cool eyes`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 09. 弓使い型 / Archer

- **アクセントカラー：** `#059669`
- **テーマ：** 集中・精密・静のイメージ
- **日本語プロンプト：** `弓使い型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、集中・精密・静のイメージ、表情豊か`
- **英語プロンプト：** `chibi Archer character, SD style, 2 heads tall, cute deformed, RPG job class, 集中・精密・静 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, green ranger outfit, bow and arrow, focused aiming pose, quiet`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 10. 商人型 / Merchant

- **アクセントカラー：** `#D97706`
- **テーマ：** 数字・交渉・価値のイメージ
- **日本語プロンプト：** `商人型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、数字・交渉・価値のイメージ、表情豊か`
- **英語プロンプト：** `chibi Merchant character, SD style, 2 heads tall, cute deformed, RPG job class, 数字・交渉・価値 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, merchant coat with gold coins, ledger, confident business smile`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 11. 鍛冶屋型 / Blacksmith

- **アクセントカラー：** `#92400E`
- **テーマ：** 職人・改善・品質のイメージ
- **日本語プロンプト：** `鍛冶屋型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、職人・改善・品質のイメージ、表情豊か`
- **英語プロンプト：** `chibi Blacksmith character, SD style, 2 heads tall, cute deformed, RPG job class, 職人・改善・品質 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, blacksmith apron, hammer, soot on cheek, earnest craftsman face`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 12. 吟遊詩人型 / Bard

- **アクセントカラー：** `#EC4899`
- **テーマ：** 表現・発信・ムードのイメージ
- **日本語プロンプト：** `吟遊詩人型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、表現・発信・ムードのイメージ、表情豊か`
- **英語プロンプト：** `chibi Bard character, SD style, 2 heads tall, cute deformed, RPG job class, 表現・発信・ムード theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, colorful bard outfit, lute, singing pose, sparkling notes`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 13. 航海士型 / Navigator

- **アクセントカラー：** `#0EA5E9`
- **テーマ：** 俯瞰・設計・未来のイメージ
- **日本語プロンプト：** `航海士型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、俯瞰・設計・未来のイメージ、表情豊か`
- **英語プロンプト：** `chibi Navigator character, SD style, 2 heads tall, cute deformed, RPG job class, 俯瞰・設計・未来 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, captain coat, map and compass, pointing to future, adventurous`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 14. 王様型 / King

- **アクセントカラー：** `#B45309`
- **テーマ：** 決断・責任・求心力のイメージ
- **日本語プロンプト：** `王様型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、決断・責任・求心力のイメージ、表情豊か`
- **英語プロンプト：** `chibi King character, SD style, 2 heads tall, cute deformed, RPG job class, 決断・責任・求心力 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, tiny crown, king cape, arms crossed confident, charismatic`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 15. 召喚士型 / Summoner

- **アクセントカラー：** `#A855F7`
- **テーマ：** 巻き込み・人脈・Pのイメージ
- **日本語プロンプト：** `召喚士型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、巻き込み・人脈・Pのイメージ、表情豊か`
- **英語プロンプト：** `chibi Summoner character, SD style, 2 heads tall, cute deformed, RPG job class, 巻き込み・人脈・P theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, summoner robe, magic circle, summoning cute creatures, connector pose`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 16. 錬金術師型 / Alchemist

- **アクセントカラー：** `#14B8A6`
- **テーマ：** 研究・実験・探究のイメージ
- **日本語プロンプト：** `錬金術師型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、研究・実験・探究のイメージ、表情豊か`
- **英語プロンプト：** `chibi Alchemist character, SD style, 2 heads tall, cute deformed, RPG job class, 研究・実験・探究 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, alchemist coat, goggles, potion bottles, curious experiment pose`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 17. 竜騎士型 / Dragoon

- **アクセントカラー：** `#DC2626`
- **テーマ：** 挑戦・独立・野心のイメージ
- **日本語プロンプト：** `竜騎士型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、挑戦・独立・野心のイメージ、表情豊か`
- **英語プロンプト：** `chibi Dragoon character, SD style, 2 heads tall, cute deformed, RPG job class, 挑戦・独立・野心 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, dragoon armor with dragon wing, spear, jumping in sky, daring`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 18. 聖騎士型 / Paladin

- **アクセントカラー：** `#FBBF24`
- **テーマ：** 信念・育成・守護のイメージ
- **日本語プロンプト：** `聖騎士型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、信念・育成・守護のイメージ、表情豊か`
- **英語プロンプト：** `chibi Paladin character, SD style, 2 heads tall, cute deformed, RPG job class, 信念・育成・守護 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, gold and white paladin armor, shield with heart, protective warm smile`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 19. 道化師型 / Jester

- **アクセントカラー：** `#F43F5E`
- **テーマ：** ユーモア・自由・発想転換のイメージ
- **日本語プロンプト：** `道化師型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、ユーモア・自由・発想転換のイメージ、表情豊か`
- **英語プロンプト：** `chibi Jester character, SD style, 2 heads tall, cute deformed, RPG job class, ユーモア・自由・発想転換 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, jester colorful hat, juggling, funny playful pose, laughing`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`

#### 20. 番人型 / Guardian

- **アクセントカラー：** `#4B5563`
- **テーマ：** 安定・保守・責任のイメージ
- **日本語プロンプト：** `番人型、ちびキャラ、SD、2頭身、かわいいデフォルメ、RPG職業、安定・保守・責任のイメージ、表情豊か`
- **英語プロンプト：** `chibi Guardian character, SD style, 2 heads tall, cute deformed, RPG job class, 安定・保守・責任 theme, big head small body, expressive face, soft shading, white background, game icon style, transparent background ready, guardian heavy armor, large shield, standing firm, reliable expression`
- **ネガティブプロンプト：** `realistic, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult proportion`
- **背景・透過：** `transparent: true`


## 5. 職能ロール7タイプ

| ID | ロール | ひとことで | 主な動き | 向いている領域 |
|---|---|---|---|---|
| `idea` | アイデアメーカー | 0→1で火をつける | 突飛なアイデアでチームに火をつける | 企画・新規事業 |
| `strategist` | 参謀役 | 勝ち筋を作る | 裏で分析し勝ち筋を描く | 経営企画・分析 |
| `producer` | 仕掛け人 | 人を繋げ形にする | 人と金を繋げプロジェクト化する | プロデューサー・事業開発 |
| `executor` | 実行部隊 | やり切る | 決めたことを最速でやり切る | 営業・現場・CS |
| `craftsman` | 職人 | 磨き続ける | 品質と仕組みを磨き続ける | エンジニア・品質管理 |
| `supporter` | サポーター | 支え整える | チームを支え整える | 人事・事務・サポート |
| `mood` | ムードメーカー | 広めて盛り上げる | 空気を作り外に広める | 広報・販売・採用 |

ロールはキャラの見た目を変える軸ではなく、診断結果の「会社での役割」と文章生成に使う。たとえば同じ騎士型でも、アイデアメーカーなら理想から旗を立て、職人なら理想を品質に落とし込む。

## 6. 140通りの文章生成ルール

- 結果タイトル：`{character}の{role}`
- 文章の基本構造：
  1. キャラの強みとロールの動きを一文で接続する
  2. キャラの長所を、会社での行動として具体化する
  3. キャラの弱点または注意点を一つ添える
  4. 相性のよい補完役や、活躍しやすい職域で締める
- 既存の140通りデータには、140件の組み合わせテキストがある。実装時はこのデータを固定文として使うか、キャラ設定・ロール設定から自動生成するかを選べる。
- 自動生成する場合も、キャラの「強み」「弱み」「向いている働き方」とロールの「主な動き」を必ず参照し、単なる職業名の置換にしない。

## 7. 実装時に引き継ぐデータ項目

### キャラクター

`id`, `name`, `en`, `keyword`, `color`, `trait`, `strength`, `weak`, `catch`, `口癖`, `向いてる働き方`, `NGな働き方`, `職業例`, `jp_prompt`, `en_prompt`, `negative`, `transparent`

### ロール

`id`, `name`, `desc`, `action`, `best`

### 画像アセット

- ファイル形式：RGBA PNG
- 推奨キャンバス：1600 × 1600 px
- 推奨表示：正方形カード、透明背景
- トリミング：キャラ全身を残し、上下左右に一定の余白を確保
- 背景除去：元画像にアルファがあることを確認してから利用する。マゼンタを色置換で消す処理は、衣装や光の色を壊す可能性があるため最後の手段にする。

## 8. キャラクターの声・セリフ設定

セリフは診断結果やキャラ図鑑、画像生成後の紹介文に使う。基本は「短く、キャラの判断基準が伝わる」ことを優先する。

| No. | キャラ | 一人称・口調 | 声の印象 | 代表セリフ |
|---|---|---|---|---|
| 01 | 騎士型 | 私／まっすぐで丁寧。理想を断言する | 正義感、凛々しさ、仲間を鼓舞 | 「本来あるべき形から、逆算しよう」 |
| 02 | 戦士型 | 俺／短く即断。勢いのある話し方 | 熱量、前進、勝負勘 | 「まず一件、取りに行こう！」 |
| 03 | 武闘家型 | 俺／無駄がなく現場語り | 実直、粘り強さ、背中で示す | 「現場を見れば、答えはわかる」 |
| 04 | 僧侶型 | 私／相手を包む柔らかな敬語 | 共感、安心、傾聴 | 「大丈夫。一緒に整理していこう」 |
| 05 | 魔法使い型 | ボク／疑問形とたとえが多い | 好奇心、奇抜さ、遊び心 | 「もし全部逆にしたら、面白くない？」 |
| 06 | 賢者型 | 私／簡潔で論理的 | 冷静、知性、構造化 | 「まず、事実と仮説を分けよう」 |
| 07 | 盗賊型 | 俺／軽快で距離が近い | 機敏、要領、情報通 | 「一番コスパのいい道、見つけたよ」 |
| 08 | 忍者型 | 私／必要なことだけ静かに話す | 効率、気配り、裏方力 | 「それなら、もう終わらせておきました」 |
| 09 | 弓使い型 | 私／短文で静か。結論が鋭い | 集中、精密、静かな自信 | 「一点に絞れば、外さない」 |
| 10 | 商人型 | 私／数字と条件を確認する | 交渉、価値判断、現実感 | 「その価値、きちんと値段に変えよう」 |
| 11 | 鍛冶屋型 | 俺／職人らしく具体的 | 品質、改善、妥協しない | 「もう一度、使う人の手元まで磨こう」 |
| 12 | 吟遊詩人型 | 私／比喩と感情表現が豊か | 発信、表現、場を明るくする | 「その話、みんなに届く物語にしよう」 |
| 13 | 航海士型 | 私／地図や時間軸で話す | 俯瞰、設計、未来志向 | 「目的地を決めれば、次の一手が見える」 |
| 14 | 王様型 | 俺／決断を引き受ける断定口調 | 責任、求心力、胆力 | 「俺が決める。責任は俺が取る」 |
| 15 | 召喚士型 | 私／人の名前や役割をよく出す | 巻き込み、接続、プロデュース | 「あの人と組めば、できることが増える」 |
| 16 | 錬金術師型 | 私／独り言のように仮説を話す | 探究、実験、深掘り | 「一度、試してみよう。失敗もデータだ」 |
| 17 | 竜騎士型 | 俺／大胆で挑発的 | 挑戦、独立、野心 | 「誰も行っていないなら、俺が行く」 |
| 18 | 聖騎士型 | 私／穏やかだが信念は強い | 守護、育成、長期視点 | 「守るだけじゃない。できるまで育てよう」 |
| 19 | 道化師型 | ボク／ツッコミと逆転発想 | ユーモア、自由、柔軟性 | 「真面目か！ 逆にしたら面白そう」 |
| 20 | 番人型 | 私／落ち着いた断定。約束を守る | 安定、責任、継続 | 「最後まで見届ける。ここは譲らない」 |

### キャラ別の台詞セット

各キャラは、最低限この5種類の台詞を持つ。`intro` は図鑑や結果画面の冒頭、`action` は仕事中、`praise` は強み、`caution` は弱点への注意、`ending` は診断結果の締めに使う。

#### 01. 騎士型

- **intro：** 「理想を語るだけじゃない。旗を立てて、そこへ進もう」
- **action：** 「本来あるべき形から、逆算しよう」
- **praise：** 「あなたの一歩が、みんなの進む方向を示している」
- **caution：** 「理想は曲げなくていい。現実との道筋は、仲間と調整しよう」
- **ending：** 「あなたがいると、チームに『正しさ』が戻る」

#### 02. 戦士型

- **intro：** 「考えすぎる前に、まず一件取りに行こう！」
- **action：** 「悩むのは走りながらでいい。今できる一手を打とう」
- **praise：** 「その行動が数字を動かした。次も勝ちに行こう！」
- **caution：** 「速さは武器だ。大事な確認だけは、一回入れよう」
- **ending：** 「あなたのその一歩が、売上と流れをつくる」

#### 03. 武闘家型

- **intro：** 「まず現場を見よう。答えは手を動かした先にある」
- **action：** 「俺がやる。終わるまで一緒に見る」
- **praise：** 「口より先に動ける。その背中が信頼をつくっている」
- **caution：** 「抱え込む前に、やったことを言葉にして渡そう」
- **ending：** 「あなたの背中を見て、みんなが安心している」

#### 04. 僧侶型

- **intro：** 「急がなくて大丈夫。まず、困っていることを聞かせて」
- **action：** 「一緒に整理しよう。今できることからでいいよ」
- **praise：** 「あなたがいるだけで、チームの空気が柔らかくなる」
- **caution：** 「支える人にも休む時間が必要だよ。無理なときは断っていい」
- **ending：** 「あなたの安心感が、チームの力を長く保つ」

#### 05. 魔法使い型

- **intro：** 「普通の答えは一回置いて、別の入口を探してみよう」
- **action：** 「もし全部逆にしたら？ そこから考えると面白そう！」
- **praise：** 「誰も見ていなかった可能性を、最初に見つけたね」
- **caution：** 「ひらめきを一つ選んだら、最後まで形にする魔法も覚えよう」
- **ending：** 「あなたのアホみたいなアイデアが、未来の定番になる」

#### 06. 賢者型

- **intro：** 「まず、事実と仮説を分けよう。そこからなら迷わない」
- **action：** 「構造で考えれば、勝ち筋は見つけられる」
- **praise：** 「あなたの分析が、複雑な問題を解ける形に変えた」
- **caution：** 「正しい答えを急ぐ前に、相手が受け取れる言葉へ翻訳しよう」
- **ending：** 「感情に流されない分析が、会社の判断を救う」

#### 07. 盗賊型

- **intro：** 「情報は集めた。あとは、一番おいしいところを取ろう」
- **action：** 「裏ワザはあるよ。最短ルートで行こう」
- **praise：** 「その要領のよさは、サボりじゃない。立派な才能だよ」
- **caution：** 「次の面白い情報へ行く前に、今の成果を仕上げよう」
- **ending：** 「あなたは、みんなが見落とす価値を拾い上げる」

#### 08. 忍者型

- **intro：** 「表に出る必要はありません。仕組みで終わらせます」
- **action：** 「終わらせておきました。次からは自動で回ります」
- **praise：** 「気づかれないほど自然に、チームを前へ進めている」
- **caution：** 「見えない仕事ほど、完了と成果を言葉で残そう」
- **ending：** 「あなたがいないと、会社は一週間で回らなくなる」

#### 09. 弓使い型

- **intro：** 「狙いを一つに絞ろう。静かに、確実に」
- **action：** 「一点に集中する。外さない準備はできている」
- **praise：** 「あなたの精度が、プロダクトの品質を決めている」
- **caution：** 「集中を守るためにも、必要な共有だけは先に済ませよう」
- **ending：** 「あなたの一射が、チームの品質基準になる」

#### 10. 商人型

- **intro：** 「価値があるなら、届く形と正しい値段に変えよう」
- **action：** 「条件をそろえれば、どちらにも得がある」
- **praise：** 「あなたは、人の願いを数字に変換できる」
- **caution：** 「損得だけでなく、長く続く信頼も取引に含めよう」
- **ending：** 「価値を値段に変えることが、あなたの魔法だ」

#### 11. 鍛冶屋型

- **intro：** 「一度作って終わりじゃない。使う人の手元まで磨こう」
- **action：** 「もう一回、0.1ミリ詰めよう」
- **praise：** 「あなたが妥協しないから、仕事がブランドになる」
- **caution：** 「完成度と締切、どちらも守るために磨く場所を選ぼう」
- **ending：** 「積み重ねた改善が、誰にもまねできない品質になる」

#### 12. 吟遊詩人型

- **intro：** 「いい仕事には、届く物語が必要だよ」
- **action：** 「その話、みんなの心が動くストーリーにしよう」
- **praise：** 「あなたの言葉が、まだ見えていない仲間を連れてくる」
- **caution：** 「発信の勢いを、最後の確認と継続にも分けてあげよう」
- **ending：** 「あなたの言葉で、人と仕事の間に橋がかかる」

#### 13. 航海士型

- **intro：** 「目的地と現在地がわかれば、次の航路を選べる」
- **action：** 「5年後の地図から、今日の一手を決めよう」
- **praise：** 「あなたの地図があるから、みんなが迷わず進める」
- **caution：** 「遠い未来だけでなく、今日の波も一度確認しよう」
- **ending：** 「あなたは、まだ見えない未来に道筋を引ける」

#### 14. 王様型

- **intro：** 「決めないことが一番のリスクだ。ここは俺が決める」
- **action：** 「行くぞ。責任は俺が取る」
- **praise：** 「迷う場面で引き受ける力が、チームに安心を与えた」
- **caution：** 「王座から一度降りて、現場の声を聞く時間も持とう」
- **ending：** 「あなたが決めるから、みんなは前へ進める」

#### 15. 召喚士型

- **intro：** 「一人で全部やらなくていい。力を持つ人をつなごう」
- **action：** 「あの人に聞いてみよう。きっと次の力を呼べる」
- **praise：** 「あなたは、組み合わせで一人では届かない成果を生む」
- **caution：** 「人を動かすだけでなく、自分の担当も最後まで握ろう」
- **ending：** 「一人では無理なことも、あなたがいれば可能になる」

#### 16. 錬金術師型

- **intro：** 「まだ答えがないなら、実験して確かめよう」
- **action：** 「なんでだろう？ その違和感を、もう少し掘ってみたい」
- **praise：** 「誰も見向きしない違和感から、金脈を見つけたね」
- **caution：** 「研究の途中でも、仮説と現在地を周りに共有しよう」
- **ending：** 「あなたの探究心が、無から新しい価値を生み出す」

#### 17. 竜騎士型

- **intro：** 「誰も行っていないなら、そこに行く理由がある」
- **action：** 「リスク？ 上等。準備して、空へ出よう」
- **praise：** 「未知へ踏み出す勇気が、チームの可能性を広げた」
- **caution：** 「挑戦を続けるために、撤退条件と帰る場所も決めておこう」
- **ending：** 「安定より、まだ誰も見ていない景色を選ぶ人だ」

#### 18. 聖騎士型

- **intro：** 「守ることは、できるようになるまで育てることでもある」
- **action：** 「君ならできる。必要なところは、私が支える」
- **praise：** 「あなたに育てられた人が、次のリーダーになる」
- **caution：** 「優しさと同じくらい、成長のための厳しい判断も大切にしよう」
- **ending：** 「あなたの信念は、人を守りながら強くする」

#### 19. 道化師型

- **intro：** 「真面目か！ いったん逆さまにして考えてみよう」
- **action：** 「その常識、笑い飛ばしたら次のアイデアが出てくるよ」
- **praise：** 「あなたの一言で、重かった会議が動き出した」
- **caution：** 「自由な発想ほど、最後は約束と成果で信頼に変えよう」
- **ending：** 「あなたは、空気を変えて新しい選択肢を開く」

#### 20. 番人型

- **intro：** 「派手さはなくていい。最後まで守り抜く」
- **action：** 「ここは譲れない。安全と品質を確認しよう」
- **praise：** 「変わらない基準を守ることが、チームの土台になっている」
- **caution：** 「守るものを見失わないために、変えるべきところは小さく試そう」
- **ending：** 「派手なヒーローより、あなたのような番人が会社を守る」

## 9. 診断結果カードの構成

### 9-1. 固定する表示項目

1. **結果タイトル：** `騎士型のアイデアメーカー` のようにキャラとロールを表示
2. **一言キャッチ：** キャラの価値観とロールの仕事を一文で接続
3. **本文：** 3〜5文。強み、行動、注意点、活躍条件を含める
4. **強み：** キャラ設定の `strength`
5. **注意点：** キャラ設定の `weak`
6. **向いている働き方：** キャラ設定の環境条件
7. **向いている職種：** ロールの `best` と職業例を組み合わせる
8. **相性のよい相棒：** 弱点を補うキャラを1体提示
9. **代表セリフ：** キャラ別台詞セットの `ending` または `action`
10. **イラスト：** キャラ固有の画像。ロールによって小物や背景を変えすぎない

### 9-2. 文章テンプレート

```text
あなたは「{character}」の、{role}タイプ。

{trait}という軸を持ち、{role_action}でチームに価値を生み出します。
{strength}が武器で、{work_behavior}の場面で特に力を発揮します。
一方で、{weak}には注意。{companion}型の相棒や、{support_condition}があると、持ち味がさらに伸びます。

向いている働き方：{work_style}
向いている職種：{job_examples}
代表セリフ：「{ending_or_action_line}」
```

### 9-3. 例：騎士型 × アイデアメーカー

> あなたは「騎士型」の、アイデアメーカータイプ。理想を掲げて突き進む力で、チームがまだ言葉にできていない未来へ旗を立てます。ぶれない軸と人を鼓舞する力が武器で、企画や新規事業の立ち上げで特に輝きます。一方で、理想が高すぎて現実調整が苦手になりやすいので、形にしてくれる職人型や参謀役の相棒がいると最強です。
>
> 代表セリフ：「本来あるべき形から、逆算しよう」

### 9-4. 例：僧侶型 × サポーター

> あなたは「僧侶型」の、サポータータイプ。相手の困りごとを聞き、チームを整えることで、みんなが力を出せる状態をつくります。共感力と傾聴力が武器で、人事、事務、看護、カスタマーサポートなど、安心感が価値になる仕事で輝きます。一方で自分の意見を後回しにしやすいので、定期的に境界線を確認できる環境があると長く活躍できます。
>
> 代表セリフ：「大丈夫。一緒に整理していこう」

## 10. 画像生成の進行ルール

1. まず騎士型と僧侶型を基準画像として固定する。
2. 顔の比率、目の大きさ、線の太さ、全身の余白、透明背景を確認する。
3. 問題がなければ同じ骨格で残り18体を生成する。
4. 生成画像ごとに、キャラ名・英語名・色・プロンプト・生成日・採用／差し戻しをローカル台帳へ記録する。
5. 画像の採用基準は、シルエットの判別性、設定小物の一致、表情、透過、全身の欠けがないこと。
6. 色味や小物の調整は1回につき1項目だけ変え、どの修正で改善したかを追えるようにする。

推奨ファイル名：

```text
character-assets/{id}-{slug}-v01.png
character-assets/{id}-{slug}-v02.png
character-assets/manifest.md
```

## 11. 今回の保存範囲

このメモで保存したもの：

- 20体のキャラ設定
- 20体の画像生成プロンプト
- 共通画風、透過、ネガティブプロンプトのルール
- 20体の話し方、代表セリフ、強み・注意・締めの台詞
- 7つの職能ロールと140通りの組み合わせ方
- 診断結果カードの表示項目と文章構成
- 騎士型・僧侶型の参考画像仕様

この段階では行っていないもの：

- アプリ本体への組み込み
- 診断ロジックの変更
- サイトへの再デプロイ
- 20体の画像生成・採用確定

次の作業は、台詞と構成をこの資料で確認したうえで、騎士型・僧侶型の基準画像から画像生成を開始する。

## 12. 本職 / 裏モード設定

20体それぞれの本職と、Neo Tokyoで発動する裏モードは [dual-mode-character-settings.md](./dual-mode-character-settings.md) にまとめた。変身版では、顔・髪の基本シルエット・目のロール差分・固有の性格・象徴アイテムを維持する。一方、身長・体格・頭身・髪色・衣装色・性別表現はキャラごとに変えてよい。

## 13. 男性VERSION / 女性VERSION

20体の男性版・女性版のビジュアル差分、裏モードへの適用、ファイル命名、生成順序は [gender-variant-character-settings.md](./gender-variant-character-settings.md) にまとめた。性別版は人格を分けるものではなく、同じキャラコアを保ったビジュアル表現の差分とする。
