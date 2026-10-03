# Higgsfield Soul 2 / 8体パイロット用プロンプト

> 実装前の画像生成用メモ。20体の既存キャラクターから、男女・身長・髪色・衣装色・種族感の幅を確認できる8体を先行候補にした。Higgsfield側での生成はログイン後に行う。

## 先行する8体

| No. | キャラ | 版 | 裏モード | ねらい |
|---:|---|---|---|---|
| 01 | 騎士型 | 男性 | FLAG//PROTOCOL | 高身長・人間寄り・旗と計画のシルエット |
| 02 | 戦士型 | 女性 | REDLINE RUNNER | 高身長・筋肉・約20%のクリーチャー質感 |
| 04 | 僧侶型 | 女性 | SOFT RESET | 小柄・癒やし・白緑とは異なる髪色 |
| 06 | 賢者型 | 男性 | DATA ORACLE | 細身・氷雪系の透明感・眼鏡なし版 |
| 08 | 忍者型 | 女性 | GHOST OPS | 中身長・黒系・静かな裏方シルエット |
| 12 | 吟遊詩人型 | 男性 | SIGNAL DJ | 中身長・音楽・シアンとピンクの光 |
| 16 | 錬金術師型 | 女性 | LAB//MIX | 中身長・実験道具・髪色と衣装色を分離 |
| 20 | 番人型 | 男性 | FIREWALL KEEPER | 最も高身長・重い守護シルエット |

## 共通設定

以下を各プロンプトの先頭に付ける。

```text
Create one original Japanese adult character for a character-diagnosis project, transformed from a friendly fantasy RPG archetype into a Neo Tokyo night-shift hidden mode. For human or humanoid characters, use natural Japanese facial features and a contemporary Japanese character-design sensibility; do not default to a Western or generic fantasy face. Keep the face distinct from other characters, with natural variation in jaw, eyelids, eyes, brows, nose, skin tone, and expression. Use Higgsfield Soul 2's polished editorial 2D animation character quality: expressive readable face, elegant but practical techwear, clean silhouette, controlled cel shading, subtle Y2K digital atmosphere, premium concept-art finish. Full-body single character, centered, front three-quarter standing pose, generous space around the entire figure, no text, no logo, no watermark, no background, no extra characters.

Keep the original archetype's personality, signature prop, role, and recognizable silhouette. Adult proportions are character-specific; do not force identical height, body build, head-to-body ratio, gender expression, hairstyle, hair color, or costume color across the set. Hair color and clothing color must be intentionally independent. Carry over only about twenty percent of the abstract reference mood: expressive animated readability, adventurous warmth, elegant cool light, and restrained creature texture. Do not copy any named character, face, hairstyle, costume, weapon, pose, logo, title, UI layout, or scene from any reference.

Vary height, body build, and muscle definition by character rather than by ethnicity or gender. Hairstyles should be plausible contemporary Japanese styles while remaining character-specific. Creature details such as horns, scales, fangs, claws, animal ears, or dragon texture are optional accents only and must not erase the Japanese human or humanoid facial base.
```

## 01 騎士型 / 男性 / FLAG//PROTOCOL

```text
One tall Japanese adult male Knight, approximately 182 cm, upright posture and broad but elegant shoulders. Give him a clearly Japanese contemporary male face with natural individual features, not a Western prince face. Preserve the knight's friendly determined expression and the idea of a small flag or banner. Hidden mode code name: FLAG//PROTOCOL. Midnight navy technical coat with a short cobalt light-cape, silver hardware, thin cyan route lines, and a compact data baton shaped like a folded flag. Warm blond tousled Japanese-inspired layered hair, amber-brown eyes, hair color deliberately contrasting with the navy outfit. He looks like an idealistic night planner who turns scattered information into a route everyone can follow. Calm heroic smile, one hand holding the data banner upright. Clean full-body silhouette.
```

## 02 戦士型 / 女性 / REDLINE RUNNER

```text
One tall adult female Warrior, approximately 186 cm, athletic build, low forward-leaning stance and powerful legs. Hidden mode code name: REDLINE RUNNER. Deep charcoal and burnt-orange utility armor with a red emergency communication line glowing across the jacket, compact runner harness, reinforced boots, and a short impact tool instead of a traditional weapon. Hair color is independent from the outfit: long silver-white hair with a dark red underlayer, tied back for movement. Add only subtle human-compatible creature texture: a small horn-like contour in the headgear, scale texture on one shoulder guard, claw-shaped fasteners, slightly wild determined eyes. Keep a human face; do not make her a full monster or animal. Energetic grin, ready to run toward a stalled connection.
```

## 04 僧侶型 / 女性 / SOFT RESET

```text
One petite adult female Priest, approximately 160 cm, gentle compact silhouette and open reassuring posture. Hidden mode code name: SOFT RESET. White and moss-green recovery techwear layered like a soft hooded jacket, flexible utility pockets, pale green fiber-optic staff, and a small circular recovery light. Choose a hair color independent from the outfit: short dark violet bob with a few warm copper strands, clear kind eyes, relaxed expression. Keep the original healer's empathy and listening presence. She is a night recovery specialist, not a fantasy nun; subtle leaf-like circuit embroidery, soft glow, minimal sparkles, no religious logo. One hand offers a calm reset signal.
```

## 06 賢者型 / 男性 / DATA ORACLE

```text
One tall slender adult male Sage, approximately 175 cm, long vertical silhouette, composed shoulders and quiet analytical presence. Hidden mode code name: DATA ORACLE. Long graphite and muted violet technical coat with transparent icy cyan panels, holographic data scrolls, crystalline log fragments and a small slate tablet. Hair color independent from clothing: black hair with a silver-blue sheen, neatly layered and slightly long around the neck. No glasses; use a very subtle transparent analysis HUD near one eye. Add a restrained ice-like glow, frosted geometry, and calm translucent light as an abstract twenty-percent influence only. Do not copy any famous ice character, braid, crown, gown, castle, or pose. Intelligent calm expression, one hand tracing a solution through floating data.
```

## 08 忍者型 / 女性 / GHOST OPS

```text
One adult female Ninja, approximately 171 cm, slim flexible build and quiet side-facing posture. Hidden mode code name: GHOST OPS. Matte black and smoky teal technical wear, modular hood, silent shoes, compact sensor discs and a folded terminal scroll. Hair color independent from the black outfit: deep blue-black hair with a single muted lime streak, tied low and partly hidden under the hood. No visible traditional costume copying; reinterpret the ninja through practical urban utility layers. Her expression is observant and almost unreadable, but not hostile. One hand finishes a silent automation gesture, suggesting that a repetitive task has already been removed from the workflow. Clean stealth silhouette, restrained cyan edge light.
```

## 12 吟遊詩人型 / 男性 / SIGNAL DJ

```text
One adult male Bard, approximately 170 cm, relaxed lean build and diagonal musician silhouette. Hidden mode code name: SIGNAL DJ. Dark navy techwear jacket with independent accents of electric cyan, magenta and warm cream, compact audio harness, luminous waveform panels, and a small original electronic string instrument. Hair color independent from clothing: medium chestnut hair with a pale mint streak, softly tousled. Preserve the bard's ability to change the atmosphere and bring people together. Friendly confident expression, one hand adjusting a signal dial while the other holds the instrument. Editorial music-night mood, no text or logos, subtle floating waveform light only.
```

## 16 錬金術師型 / 女性 / LAB//MIX

```text
One adult female Alchemist, approximately 172 cm, practical medium build, slightly forward-leaning experimental posture. Hidden mode code name: LAB//MIX. Warm rust-orange utility coat over a cool teal inner layer, modular belt, transparent sample capsules, small portable lab device and protective gloves. Hair color must contrast with the clothes: pale lavender hair with a short asymmetrical cut and one bright yellow clip. Round protective goggles rest on her head, not covering the eyes. Preserve the curious researcher personality, hands-on experimentation and delight in making something new from unused materials. A tiny controlled glow from a sample vial, no dangerous explosion, no text, no logo.
```

## 20 番人型 / 男性 / FIREWALL KEEPER

```text
One very tall adult male Guardian, approximately 190 cm, broad stable build, grounded stance like a protective wall. Hidden mode code name: FIREWALL KEEPER. Heavy slate-gray and deep olive technical armor, layered protective coat, broad translucent firewall shield with a simple original keyhole-like seal, reinforced gloves and boots. Hair color independent from the armor: short pale gold hair with a dark ash undercut. Preserve the dependable quiet guardian personality; he is calm, not aggressive. One shield planted on the ground, shoulders angled to protect an unseen team. Subtle cyan warning light along the shield edge, no text, no logo, no background.
```

## Higgsfield側の推奨設定

- モデル：`Soul 2.0`
- 用途：今回のコンセプト確認では、まずGUI／アーカイブポスター版を1枚作る。キャラクター原本の切り抜き版は別プロンプトで後から作る。
- 比率：縦長 2:3 または 3:4。8体を並べる用途なら全員同じ比率にする。
- 背景：コンセプトポスター版は薄いグリッド、濃紺GUI、ステータス／ログ／ファイル窓を入れる。切り抜き版だけ背景なし／単色にする。
- 生成単位：1体ずつ。複数枚を一度に出さず、まず各キャラの代表1枚を確定する。
- 参考画像：同じキャラの顔・シルエットを固定したい場合だけ、既存の原本PNGをHiggsfieldへアップロードする。アップロード前にユーザー確認を取る。

## 現行コンセプト用の追加指示

これまでの「no background / no text / isolated full-body character」という指示は、切り抜き原本には適しているが、今回のNEO TOKYOコンセプトから離れるため、ポスター版では使わない。ポスター版では次を共通で追加する。

```text
Do not make an isolated character sheet. Make a Neo Tokyo after-school archive concept poster: vertical 3:4, the original Japanese adult character centered inside a retro computer GUI, pale grid or deep navy archive background, dark navy window frames, thin black outlines, cyan blue and lime green accents, small status bars, readme/log/storage/message panels, file and system labels, subtle Y2K digital archive mood. The character should occupy about 45–65% of the composition and remain the clear focal point. Use crisp 2D cel shading and flat graphic shapes, not a photorealistic 3D render. Keep all UI copy short and abstract; do not copy any logo, title, named character, or exact reference layout. Keep the occupation, personality, hidden-mode code name, signature prop, Japanese facial features, and recognizable silhouette readable.
```

## 生成後の確認項目

1. 本職の性格と裏モード名が見た目から伝わるか。
2. 8体を並べたとき、身長・体格・髪色・衣装色が重複しすぎていないか。
3. 戦士は人間の顔を保ったまま、クリーチャー質感が約20%に収まっているか。
4. 賢者は氷雪系の透明感だけを借り、特定作品の再現になっていないか。
5. 全身、手、足、象徴アイテムが欠けていないか。
6. キャラクターがGUI／アーカイブ／レトロPCの画面内に存在し、無地背景の立ち絵になっていないか。
7. 文字、ロゴ、透かし、余分な人物が入っていないか。UI文字は短い抽象ラベルに収まっているか。

## 状態

- 8体の候補とSoul 2用プロンプト：作成済み
- Higgsfieldログイン：ユーザー操作待ち
- 既存のローカルサイト／アプリ：変更なし
- 既存の20体原本：上書きなし
