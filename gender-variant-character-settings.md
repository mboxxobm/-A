# 20体キャラクター 男性VERSION / 女性VERSION設定

> 実装前のビジュアル設定。男性版と女性版は別人格ではなく、同じキャラクターコアを持つ2つの表現バリエーション。

## 1. 基本ルール

- キャラ名、性格、強み、弱み、本職、裏モード、象徴カラー、象徴アイテムは男性版・女性版で共通。
- 目のロール差分も共通。アイデア、参謀、仕掛け人、実行、職人、サポーター、ムードの目を男女どちらにも適用できる。
- 男性版・女性版で変えるのは、顔の輪郭、髪型、体のシルエット、声の表現、衣装のフィット感。
- 男性版だから強く、女性版だから優しい、という性格分けはしない。性格と職能は20体の元設定を維持する。
- 女性版は過度な露出や性的な強調を避け、ゲームアイコンとしての動きやすさ・可愛さ・職業性を優先する。
- 男性版も筋肉や体格だけで差別化せず、表情、髪、姿勢、装備の持ち方で個性を出す。
- 裏モードでは、男性版・女性版それぞれの髪型と顔の印象を保持したまま、衣装と小物をNeo Tokyoテックウェアへ変換する。
- 人間型の男性版・女性版は、どちらも日本人の成人として設計する。輪郭、まぶた、目、眉、鼻、肌のトーンは個体差を持たせ、同じ顔の男女差分にはしない。
- 髪型は現代日本の人物として自然な範囲でキャラごとに変え、髪色は衣装色から独立させる。日本人らしさを髪色だけで表現せず、顔立ち・表情・体格・所作の総合で表現する。
- 角・鱗・牙・獣耳などのモンスター要素は、人間の日本人らしい顔立ちを残したまま、役割や裏モードを示すアクセントとして扱う。
- 身長・体格・頭身はキャラごとに変えてよい。成人変身後は小柄、標準、高身長を混在させ、男女版でも同じ身長に固定しない。
- 髪色と衣装色は独立させる。黒髪に白緑、紫髪に黒、青緑髪に濃紺など、役割と視認性に合う組み合わせを優先する。
- 参考画像からは表情の豊かさ、優雅さ、冒険感、モンスター質感を約20%だけ抽象化し、固有キャラクターの再現は行わない。

## 2. バリエーション数

- キャラクターコア：20体
- 性別表現：男性VERSION / 女性VERSION
- モード：本職モード / 裏モード
- 目の役割差分：7種類
- 画面上の組み合わせ数：20 × 2 × 2 × 7 = 560通り
- 文章診断の基本結果は、性別や目の差分で人格を分けず、従来の20キャラ × 7ロール = 140通りを正本とする。

## 3. 共通の画像生成指定

```text
Create a masculine-presenting or feminine-presenting version of the same fixed chibi character. For human or humanoid characters, the person is Japanese, with natural individual variation in Japanese facial features; do not default to a Western or vaguely generic fantasy face.
Keep the exact character identity, personality, signature prop, eye-role variant, occupation motif, and recognizable silhouette.
Allow character-specific height, body build, head-to-body proportion, hair color, hairstyle, glasses, and creature-inspired texture. Do not force hair color to match costume color. Change the face shape, hairstyle, body silhouette, voice impression, and clothing fit appropriate to the requested gender presentation without creating a different personality.
Do not create a different personality, do not sexualize the character, do not add text, logo, watermark, or extra characters.
```

男性VERSION指定：

```text
masculine-presenting chibi character, slightly broader shoulder silhouette, practical hairstyle, confident or gentle expression according to the original character, non-adult cute proportions, modest functional costume
```

女性VERSION指定：

```text
feminine-presenting chibi character, slightly softer face silhouette, practical hairstyle with tied or layered hair, confident or gentle expression according to the original character, non-adult cute proportions, modest functional costume, no sexualized pose
```

## 4. 20体の男性 / 女性ビジュアル差分

| No. | キャラ | 男性VERSION | 女性VERSION | 共通して残す要素 |
|---:|---|---|---|---|
| 01 | 騎士型 | 短めの金髪、片側に流した前髪、肩幅のある銀鎧 | 金髪のハーフアップまたは短い編み込み、軽快な銀鎧 | 青いマント、木剣、正面を向く勇敢さ |
| 02 | 戦士型 | 茶色の無造作ショート、力強い踏み込み | 茶色の高いポニーテール、動きのある踏み込み | 赤いはちまき、戦斧、情熱的な目 |
| 03 | 武闘家型 | 短いスパイキーヘア、低い構え | 編み込みポニーまたは短いツイン編み、低い構え | オレンジ道着、拳の包帯、現場感 |
| 04 | 僧侶型 | 柔らかい茶色のショートレイヤー、落ち着いた輪郭 | 茶色のボブまたは低い三つ編み、柔らかな輪郭 | 白緑ローブ、葉のヘッドバンド、杖と光 |
| 05 | 魔法使い型 | 銀または淡い金の短髪、帽子から前髪が見える | 長めの髪を片側に束ねる、帽子のリボンを追加 | 星柄の紫帽子、魔導書、好奇心の表情 |
| 06 | 賢者型 | 青紫のショート、丸眼鏡、端正な輪郭 | 青紫の低い三つ編みまたはボブ、丸眼鏡 | 青いローブ、巻物、冷静な目 |
| 07 | 盗賊型 | 淡い金髪の無造作ショート、フードから片目を覗かせる | 淡い金髪の短いポニー、フードとサイドの毛束 | 灰色フード、短剣、コイン袋、軽い身のこなし |
| 08 | 忍者型 | 黒髪ショート、後ろに細い結び目 | 黒髪の高いポニー、短い前髪、動きやすい輪郭 | 黒い忍装束、手裏剣、静かな目 |
| 09 | 弓使い型 | 茶または緑の短髪、帽子から前髪を出す | 茶または緑の長めのポニー、葉の髪飾り | 緑の衣装、弓、集中した視線 |
| 10 | 商人型 | 茶色の短髪、帽子とコートで商人らしい輪郭 | 茶色のボブまたは低いポニー、コートとスカーフ | 帳簿、硬貨、天秤、交渉の笑顔 |
| 11 | 鍛冶屋型 | 茶色の短髪、バンダナ、力強い腕のシルエット | 茶色の編み込みポニー、袖をまくったエプロン | ハンマー、煤、エプロン、職人の集中 |
| 12 | 吟遊詩人型 | 柔らかな中短髪、帽子と羽根、軽いステップ | 明るい三つ編みまたはツインテール、羽根飾り | リュート、音符、ピンクの衣装、発信力 |
| 13 | 航海士型 | 金髪ショート、船長帽、広い視野を感じる立ち姿 | 金髪ボブまたは低いポニー、船長帽とスカーフ | 地図、コンパス、青い船長服、未来を見る目 |
| 14 | 王様型 | 金髪ショート、王冠、胸を張った立ち姿 | 金髪の編み込みまたはボブ、王冠、堂々とした立ち姿 | 王冠、王笏、赤いマント、決断の表情 |
| 15 | 召喚士型 | 明るい茶または紫のショート、ローブのフード | 明るい茶または紫の長い髪、ローブのフードと細いリボン | 魔法陣、通信する小さな精霊、人をつなぐ手 |
| 16 | 錬金術師型 | 淡い金髪の乱れたショート、ゴーグルを額に置く | 淡い金髪のボブ、ゴーグルと実験用ヘアクリップ | 薬瓶、研究ノート、実験の好奇心 |
| 17 | 竜騎士型 | 赤いスパイキーヘア、角のあるヘルメット、跳躍姿勢 | 赤いロングポニーまたは編み込み、角のあるヘルメット | 竜翼モチーフ、槍、赤い鎧、挑戦の笑顔 |
| 18 | 聖騎士型 | 金髪ショート、金白の鎧、盾を前へ出す | 金髪の編み込みまたはハーフアップ、金白の鎧 | ハートの盾、守護の光、育てる目線 |
| 19 | 道化師型 | 明るい短髪、二股帽子、軽いジャンプ | 明るいツインテール、二股帽子、リボンの動き | 赤桃の衣装、鈴、ボール、笑いで空気を変える表情 |
| 20 | 番人型 | 茶または黒の短髪、重装ヘルメット、安定した足元 | 茶または黒のボブ、重装ヘルメット、安定した足元 | 濃灰の鎧、大盾、鍵穴の紋章、責任感 |

## 5. 本職 / 裏モードへの適用

男性版・女性版の両方で、以下の対応を維持する。

| 項目 | 本職モード | 裏モード |
|---|---|---|
| 衣装 | RPG職業の衣装 | 本職カラーを残したNeo Tokyoテックウェア |
| 髪型 | 男性版・女性版の基本髪型 | 同じ髪型を維持し、ヘッドセットや発光ピンだけ追加 |
| 目 | 7ロールの目差分 | 同じ目差分。光量と反射だけ少し強くする |
| アイテム | 剣、杖、弓、帳簿など | データバトン、光ファイバー杖、スキャナー、タブレットなどへ変換 |
| 表情 | 日中の職能が伝わる表情 | 秘密の専門性が起動した表情 |
| 背景 | 透明素材または通常の図鑑背景 | 透明素材、または別途Neo Tokyoポスター背景 |
| セリフ | 既存の20体の本職セリフ | 裏モード台詞を使用 |

## 6. ファイル命名

本職と裏モード、男性版と女性版を上書きせずに保存する。

```text
character-assets/main/male/01-knight-m-v01.png
character-assets/main/female/01-knight-f-v01.png
character-assets/hidden-mode/male/01-flag-protocol-m-v01.png
character-assets/hidden-mode/female/01-flag-protocol-f-v01.png
```

目の差分を組み合わせる場合：

```text
eye-variants/idea.png
eye-variants/strategist.png
eye-variants/producer.png
eye-variants/executor.png
eye-variants/craftsman.png
eye-variants/supporter.png
eye-variants/mood.png
```

## 7. 生成順序

1. 騎士型の男性版・女性版を本職モードで作る
2. 騎士型の男性版・女性版をFLAG//PROTOCOLで作る
3. 僧侶型の男性版・女性版を本職モードで作る
4. 僧侶型の男性版・女性版をSOFT RESETで作る
5. 顔、身長、頭身、髪型、髪色、衣装色、装備の差分が意図どおりか確認する
6. 問題がなければ残り18体へ展開する

いきなり80枚を確定版にせず、騎士型と僧侶型の男女・本職／裏モードの8枚を基準にする。基準が固まったあとで残りを生成する。
