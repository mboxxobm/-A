# 画像生成プロンプト台帳（v01）

20体の初版画像を再生成できるよう、共通部分とキャラ固有部分を分けて記録する。

## 共通プロンプト

```text
Use case: stylized-concept
Asset type: square transparent character asset for a career-diagnosis game
Input images: Image 1 is the Knight style reference and Image 2 is the Priest style reference. Use them only for the shared friendly chibi language, face proportions, line weight, soft shading, and full-body spacing.
Style/medium: polished Japanese chibi SD game character illustration, two-head-tall proportions, oversized head and small body, clean dark outline, soft cel shading, rounded shapes, expressive face, collectible game icon quality.
Composition/framing: one character only, full body, centered, completely visible with generous transparent padding, readable silhouette at small size.
Constraints: genuine transparent alpha background, no colored backdrop, no magenta, no text, no logo, no watermark, non-adult proportions, no exact copying of the reference face or pose.
Avoid: realistic rendering, scary, ugly, nsfw, low quality, blurry, extra limbs, long body, adult anatomy, cropped feet, cropped props, text, logo, watermark.
```

参考画像の役割：

- Image 1：騎士型の全身シルエット、鎧、青マント、表情の基準
- Image 2：僧侶型の顔比率、線、光の扱い、衣装の細部、全身余白の基準

## キャラ固有プロンプト

共通プロンプトのあとに、各行の `Primary request` と `Subject` を接続して使う。

### 01. 騎士型

```text
Primary request: Generate one original cute chibi Knight character in the same friendly SD illustration language as the references.
Subject: one full-body Knight, two-head-tall proportions, oversized head and small body, blond slightly tousled hair, large warm brown eyes, silver plate armor, deep blue cape, small wooden sword held diagonally, tiny heroic stance, brave friendly smile, a subtle blue accent glow.
```

### 02. 戦士型

```text
Primary request: Generate one original cute chibi Warrior character.
Subject: red headband, sturdy battle outfit, small battle axe, compact muscular chibi build; visual theme of passion, action, and victory; charging forward with one fist raised; determined energetic grin; red accents.
```

### 03. 武闘家型

```text
Primary request: Generate one original cute chibi Martial Artist character.
Subject: orange martial arts gi, wrapped fists, sweatband, simple training gear; visual theme of fieldwork, embodiment, and discipline; grounded ready stance with one fist forward; focused stoic expression; orange accents.
```

### 04. 僧侶型

```text
Primary request: Generate one original cute chibi Priest character in the same friendly SD illustration language as the references.
Subject: one full-body Priest, two-head-tall proportions, oversized head and small body, soft brown bob haircut, green leaf headband with a small cross charm, white robe with green trim and leafy embroidery, wooden staff with a softly glowing pale-green orb, gentle closed-eye smile, calm healing aura made of a few small sparkles and leaves.
```

### 05. 魔法使い型

```text
Primary request: Generate one original cute chibi Wizard character.
Subject: pointed purple hat with stars, purple robe, glowing spellbook, tiny floating sparks; visual theme of invention, genius, and unconventional ideas; playfully presenting a new spell idea; mischievous curious grin; purple accents.
```

### 06. 賢者型

```text
Primary request: Generate one original cute chibi Sage character.
Subject: long indigo-blue robe, round glasses, ancient scroll, small geometric runes; visual theme of logic, analysis, and calm judgment; holding an open scroll and calmly explaining a solution; wise composed expression; indigo accents.
```

### 07. 盗賊型

```text
Primary request: Generate one original cute chibi Thief character.
Subject: hooded gray cloak, small safe-looking dagger, coin pouch, subtle map scrap; visual theme of agility, cleverness, and information; light-footed sideways step while pointing to a shortcut; cute sly smirk; gray accents.
```

### 08. 忍者型

```text
Primary request: Generate one original cute chibi Ninja character.
Subject: dark charcoal ninja outfit, small shuriken, utility scroll, tidy compact silhouette; visual theme of efficiency, behind-the-scenes support, and preparation; quietly completing a task with one hand raised in a sign; cool observant eyes; near-black accents.
```

### 09. 弓使い型

```text
Primary request: Generate one original cute chibi Archer character.
Subject: green ranger outfit, small elegant bow, one arrow ready, leaf-shaped accents; visual theme of focus, precision, and quiet concentration; steady aiming pose with the bow held to the side; quiet focused eyes; emerald green accents.
```

### 10. 商人型

```text
Primary request: Generate one original cute chibi Merchant character.
Subject: warm ochre merchant coat, small ledger, coin pouch, brass scale charm; visual theme of numbers, negotiation, and value creation; offering a coin and presenting a fair deal; confident business smile; gold and amber accents.
```

### 11. 鍛冶屋型

```text
Primary request: Generate one original cute chibi Blacksmith character.
Subject: dark brown smith apron, sturdy hammer, small anvil charm, soot mark on cheek; visual theme of craft, improvement, and quality; holding the hammer proudly after finishing a careful repair; earnest satisfied craftsman expression; deep brown and bronze accents.
```

### 12. 吟遊詩人型

```text
Primary request: Generate one original cute chibi Bard character.
Subject: bright pink and rose bard outfit, small lute, colorful scarf, sparkling musical notes; visual theme of expression, communication, and atmosphere; singing and inviting the viewer to join; joyful open smile; pink accents.
```

### 13. 航海士型

```text
Primary request: Generate one original cute chibi Navigator character.
Subject: sky-blue captain coat, map, compass, tiny telescope, neat gold trim; visual theme of big-picture planning, design, and future vision; pointing at a route on a map toward the horizon; adventurous confident expression; sky-blue accents.
```

### 14. 王様型

```text
Primary request: Generate one original cute chibi King character.
Subject: small warm-brown crown, rich amber royal cape, simple signet, compact regal outfit; visual theme of decision, responsibility, and gravity; standing firmly with one hand raised to make a decision; charismatic confident smile; amber and gold accents.
```

### 15. 召喚士型

```text
Primary request: Generate one original cute chibi Summoner character.
Subject: violet summoner robe, glowing magic circle, three tiny friendly elemental spirits, connector charm; visual theme of connection, networks, and producing; welcoming the little spirits and linking them together; warm confident smile; violet accents.
```

### 16. 錬金術師型

```text
Primary request: Generate one original cute chibi Alchemist character.
Subject: teal alchemist coat, round goggles, colorful potion bottles, tiny bubbling flask; visual theme of research, experiments, and curiosity; holding up a successful experiment with a curious lean; bright inquisitive expression; teal accents.
```

### 17. 竜騎士型

```text
Primary request: Generate one original cute chibi Dragoon character.
Subject: red dragoon armor with a small dragon-wing motif, lance, compact shoulder armor; visual theme of challenge, independence, and ambition; leaping upward with the lance angled toward the sky; daring fearless grin; crimson accents.
```

### 18. 聖騎士型

```text
Primary request: Generate one original cute chibi Paladin character.
Subject: gold-and-white paladin armor, small shield with a heart emblem, warm cloak, gentle holy sparkles; visual theme of conviction, growth, and protection; standing protectively with the shield forward and one hand encouraging a teammate; protective warm smile; gold accents.
```

### 19. 道化師型

```text
Primary request: Generate one original cute chibi Jester character.
Subject: colorful red-and-pink jester outfit, bell-tipped hat, two small juggling balls, playful ribbons; visual theme of humor, freedom, and reframing; mid-juggle with a lighthearted sideways tilt; laughing mischievous expression; rose and red accents.
```

### 20. 番人型

```text
Primary request: Generate one original cute chibi Guardian character.
Subject: charcoal heavy guardian armor, large sturdy shield, simple key or seal emblem, dependable cloak; visual theme of stability, maintenance, and responsibility; standing firmly with the shield planted and feet grounded; calm reliable expression; slate-gray accents.
```

