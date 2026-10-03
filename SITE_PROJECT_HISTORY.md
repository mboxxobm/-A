# SITE project history summary

This file is a concise, public-safe record of the decisions represented in the local project. It is not a raw chat export.

## Project direction

- Build the character setting locally before creating an application.
- Start from a fixed base character system and create adult-mode, male, female, transformation, hidden-mode, eye, hair, and costume variations.
- Maintain a 20-archetype roster, with a main profession and a hidden/裏 mode for each character. The male/female expansion is intended to reach 40 character variants.
- Use the adult full-body character as the canonical setting asset. Add the background later as a separate layer.

## Visual language

- Original NEO TOKYO / Y2K cyber-casual / techwear archive atmosphere.
- Dark navy technical clothing, cyan circuit-like signals, lime status accents, gold hardware, and controlled pink/purple variations.
- Quiet, slightly introverted mood: low-temperature expressions, night scenes, idle/reconnecting/error motifs, and personal distance without turning every character into a villain or a gothic stereotype.
- Character identity comes from hair, face, body proportions, shoulder armor, tools/weapons, and role-specific equipment rather than gender-coded colors.

## Roster and color system

- 01-05: ADA navy, approximately `#0B1F38`.
- 06-10: blue slate, approximately `#122A46`.
- 11-15: graphite blue, approximately `#1C2838`.
- 16-20: deep teal, approximately `#123E44`.
- Signal colors are rotated across cyan, lime, gold, pink, and purple. The goal is for all 40 male/female combinations to be non-duplicating while keeping the ADA world identity and pair feeling.
- Female ADA and male BYRON share the navy/cyan/lime/gold design language; gender is not represented by a separate color palette.

## Image/layout decisions

- The earlier four-cut character boards used titles such as `MAP // ROUTE`, `COMMAND // CORE`, `LINK // CAST`, and `LAB // MIX`.
- Repeated corner widgets such as `STATUS`, `LOG`, and `STORAGE`, as well as black corner boxes, were removed so each panel can later receive a lucky item or other optional insert.
- Hand anatomy is checked deliberately: exactly two arms and two hands, with no duplicate wrists, phantom limbs, or extra fingers.
- The archer uses a clearly readable bow with gold accenting.
- The full-body workflow now saves clean character cutouts as transparent PNGs so environments can be added later.

## Current local visual assets

- `character-assets/`: base roles, main/hidden modes, transformation demos, manifests, and prompt logs.
- `character-roster-4cut-final/`: the corrected ten-panel male/female four-cut set.
- `character-roster-fullbody-v1/`: female ADA, male BYRON, and LAB MIX full-body concept images.
- `character-setting-cutouts/`: transparent character setting images.
- `face-cards/` and `face-crops/`: face variation assets.
- `blender_ada_prototype.py` and `blender_prototype_ada.blend`: early Blender material/character prototype files.

## Next intended steps

- Freeze the character setting sheets and color IDs before mass generation.
- Generate the remaining full-body characters with unique color combinations.
- Add backgrounds independently for NEO TOKYO streets, labs, convenience stores, forests, and other scenes.
- Convert approved characters into Blender-ready parameterized assets.
