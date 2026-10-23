# Academic-Promotion Mode (Bayer Radiology)

Reference for building **academic-exchange / research-proposal decks** for physicians, e.g. PCCT × MEDRAD® Centargo × P3T®/PAT.

This mode is a narrative and copy layer **on top of** `SKILL.md`. All brand rules still apply unchanged:

- Icon Library POTX master chrome.
- Color Guide 12 + white.
- Body text `#10384F` on `#FFFFFF`.
- Arial / Arial Unicode MS.
- Outline icons.
- 16:9 at `12190413 × 6858000` EMU.
- MEDRAD `#E46C0A` only as the product accent.

**Worked example (good):** `/workspace/pcct-centargo-proposal/build/PCCT_Centargo_P3T_研究Proposals_v4.pptx`
**Anti-example:** v3 of the same deck. See §10.

---

## 1. When to use

| Use this mode when… | Do not use this mode for… |
|---|---|
| The audience is physicians, researchers or department heads who want frontier research | Sales / tender / pricing decks |
| The goal is to show the evidence landscape, pose open questions and offer adoptable study protocols | Product training or operator SOPs. Use Operation Manual (OM) content plainly instead |
| The product is positioned as a **research platform** (dose individualisation, reproducibility, data traceability) | Promotional claims of efficacy beyond the label |
| The deliverable ends with a collaboration or IIT invitation | Internal strategy decks. Use the Chart Pool / BC frameworks instead |

**Tone:** a peer scientific talk. Assertive about evidence, precise about product scope, invitational about research.

---

## 2. Narrative arc and page-by-page template

**Arc:**

1. Frontier question
2. Evidence landscape
3. Unresolved clinical questions
4. Product as research platform
5. Adoptable proposals (×N)
6. Rollout roadmap + collaboration invitation
7. References

**Layouts:**

- Title slide: `MEDRAD Centargo Title Slide 3`.
- All content slides: `MEDRAD Centargo Text Slide with logo`.
- Optional section breaks: `MEDRAD Centargo Text Color Background Logo`.

### Page-by-page template

v4 slide numbers are given as reference. "Max text" means substantive text boxes / CJK characters on the slide face. Footer, date and slide-number placeholders are excluded.

| # | Page role | Assertion-title pattern (zh example) | Hero visual | Max text |
|---|---|---|---|---|
| 1 | Cover (v4 S1) | `{技术}时代的{主题}：证据、开放问题与可落地的研究方案` | Concept visual, captioned `概念视觉（AI 生成，示意）` | 4 / 80 |
| 2 | Route map (S2) | `从{前沿}到可落地的研究：今天的 N 站` | N icon tiles or a journey line (AntV `sequence-*`) | 7 / 140 |
| 3 | Frontier physics (S3) | `{技术}：{一句机制结论}` | Native schematic contrasting old vs new (EID vs PCD) | 8 / 180 |
| 4 | Frontier rule / key number (S4) | `{操作}，{结果}：每{X}约可{Y}` | Literature figure + one big number | 8 / 150 |
| 5 | Evidence landscape (S5) | `证据全景：{领域}研究激增，{变量}正成为焦点` | Timeline/bar chart of study counts, drawn in matplotlib with the Bayer palette | 8 / 140 |
| 6 | Evidence synthesis (S6) | `多部位、多设计：{结论}方向一致` | Forest-style or bar chart of reported reductions, labelled `原文报告` | 8 / 150 |
| 7 | Visual proof (S7) | `看得见的证据：{干预}后图像仍保持诊断质量` | 1–2 literature figures, each ≥35% of the slide | 6 / 150 |
| 8 | Open questions (S8) | `N 个开放问题：{领域}的下一步需要前瞻研究回答` | 2×2 question cards, each with an outline icon | 8 / 180 |
| 9 | Product as platform (S9) | `{产品} + {功能}：把注射变成可设计、可复现的研究变量` | Product photo/concept + 3–4 capability tiles | 8 / 160 |
| 10 | Parameter coverage (S10) | `从 gI/kg 到 gI/s：{功能}覆盖主流个体化参数` | Range chart (product range bars vs literature points), captioned `自制` | 8 / 160 |
| 11 | Data traceability (S11) | `每一针都可追溯：{模块}让注射数据进入研究数据库` | AntV/native data-flow chain: patient → injection → image → outcome | 7 / 150 |
| 12 | Proposal overview (S12) | `N 个可落地的研究提案：覆盖{部位}` | N proposal cards (letter, region, one-line question) | 8 / 160 |
| 13+ | Proposal X design (S13/S15/S17/S19) | `提案 X｜{部位}：探索{方案}能否{终点}` | Study-design schematic (arms → reading → endpoints) | 7 / 180 |
| 13+1 | Proposal X evidence anchor (S14/S16/S18) | `提案 X｜证据锚点：{结论}已在{场景}中初见成效` | 1–2 CC BY literature figures + one "论文产出" strip | 7 / 160 |
| n-1 | Roadmap + invitation (S20) | `在您的中心启动研究：N 步路线与合作方式` | 5-step chevron/sequence + collaboration panel | 8 / 200 |
| n | References (S21) | `参考文献` | (exempt from the image rule; split across two slides if more than 12 refs) | — / — |

**Rules for using the template:**

- Proposals are **two pages each**: a design page and an evidence-anchor page.
- A proposal may be design-only (v4 S19) when its evidence was already shown in §4–§7.
- Every proposal maps back to one open question (Q1–Q4). State the mapping on the evidence-anchor page, e.g. `填补 Q1 证据空白`.

---

## 3. Proposal page anatomy

### Design page

| Zone | Content | Copy pattern |
|---|---|---|
| Title | Assertion phrased as an exploration | `提案 A｜CCTA：探索按碘流率个体化能否让冠脉强化更稳定` |
| Subtitle (design line) | Modality · arms · design type | `PCCT CCTA · P3T Cardiac 体重因子 vs 碘流率目标方案 · 前瞻随机` |
| Hero: design schematic | Native shapes: population → randomisation → Arm 1 / Arm 2 (product setting) → VMI reading → endpoints | Arm labels use exact product names, e.g. `P3T® Cardiac · 体重因子` |
| Hypothesis card | One sentence, testable, cites its source | `以 Busselot 类碘流率目标给药，个体间冠脉强化离散度低于按体重因子给药` |
| Endpoints card | Primary: one measurable endpoint. Secondary: ≤3 | `主要终点：55 keV 近端冠脉 HU 落入目标窗的比例 / 变异系数` |
| Value strip (bottom) | Value to the department | `论文产出 · 科室方案标准化 · 碘用量数据` |

### Evidence-anchor page

| Zone | Content |
|---|---|
| Title | `提案 X｜证据锚点：…` |
| Subtitle | Author Year + key result, e.g. `Higashigaito 2023 −25% 非劣 · Hennes 2026 低碘 / 超低碘` |
| Hero | 1–2 literature figures, each with a source/licence caption (§6) |
| Value strip | `论文产出 / {这项研究回答的问题}` |

**Constraints:**

- Sample size is always `待统计设计`. Non-inferiority margins are always `阈值由统计设计确定`.
- Never print a promised result.
- Protocol settings are the **investigator's choice** (`研究者定义方案`). The product only *enables* setting and recording them.

---

## 4. Copy rules

1. **Assertion titles.**
   - Every title is a full-sentence claim that the slide's visual proves.
   - Topic labels (`证据概览`) appear only as small subtitles or kickers.
2. **Confident and exact product names.**
   - Use registered names exactly: MEDRAD® Centargo, P3T® Cardiac / P3T® PA / P3T® Abdomen, PAT, DualFlow, Data Manager.
   - Use ® on first mention per slide.
   - **Never invent feature names** such as "Smart Protocol", "智能方案" or "AI 剂量".
3. **No compliance vocabulary on the slide face.**
   - `红线 / 合规 / 规避 / 超说明书 / red line / compliance / off-label` must not appear.
   - Constraints live **only in speaker notes** (§5).
4. **Phrase factual boundaries positively.**
   - Use exploration framing: `探索…能否…`, `研究者定义方案`, `在研究方案中设定并记录`, `investigator-defined protocol`.
5. **Numbers.**
   - Use only locked or cited numbers: literature results (`原文报告`) and OM parameter ranges.
   - No projected percentages for the product. No "可减少 X%" attributed to Centargo.
6. **Accurate facts.**
   - Results achieved on PCCT belong to the **study**, not to the injector.
   - Off-label doses, populations or indications are never presented as product features. Present them only as research questions under an investigator-defined protocol.
7. **Language.**
   - Chinese body text, with English for technical terms (keV, IDR, CNR, VMI, gI/kg).
   - One idea per text box. Avoid full stops in titles.

### Do / don't rewrites

| ✗ Don't (v3-style) | ✓ Do (v4-style) | Why |
|---|---|---|
| `红线：不得宣称 Centargo 降低碘量` | `已发表研究证明了低碘的可行性；下一步是让剂量随患者与 keV 精确匹配，并可复现、可追溯` | Boundary moved to notes; slide states what the platform does |
| `合规提示：超低剂量属超说明书使用` | `提案 B｜主动脉 CTA：探索低 keV 下的低总碘个体化方案` | Positive exploration framing |
| `规避：不得承诺减量比例` | `主要终点：主动脉强化达标率（非劣，阈值由统计设计确定）` | The number is left to statistics, not promised |
| `Smart Protocol 自动算出最佳剂量` | `P3T® Cardiac：按体重因子与扫描时长个体化剂量，碘负荷上下限可设` | Registered name + factual OM function |
| `使用 Centargo 可减少 25% 对比剂` | `Higashigaito 2023：PCCT 主动脉 CTA 50 keV 下碘量 −25% 非劣（原文报告）` | Number attributed to the study, not the product |
| `P3T 支持 0.05 gI/kg 超低剂量 CCTA` | `体重因子 0.05–1.0 gI/kg 可设（OM §9）；具体取值由研究方案确定` | OM range is a fact; the clinical choice belongs to the investigator |
| `Red line: research use only` | `Investigator-defined protocol · parameters set and logged on Centargo` | Positive English equivalent |
| `合作研究保证发表` | `从可行性评估到发表，Bayer Radiology 与您共同推进` | Invitation, not a guarantee |

---

## 5. Speaker-notes compliance block template

Paste this at the **end** of each content slide's notes. The lint does not scan notes for banned words, so the explicit vocabulary belongs here.

```text
【讲者要点】
- <2–4 bullets: what to say, in what order>

【合规说明 / Compliance (notes only — not for slide face)】
- 数据来源：<Author Year, Journal, Fig./Table; PMID/DOI>；数字为原文报告，未外推。
- 产品范围：<产品/功能名> 参数范围依据 Operation Manual §<x>；仅陈述注册/说明书内功能。
- 研究边界：所示剂量/流速/人群为研究者定义方案中的研究变量，不构成产品推荐用法；
  超说明书用法不得作为产品功能介绍，仅在 IIT/伦理批准框架内讨论。
- 不承诺：不宣称减量比例或临床获益归因于注射器；样本量与非劣界值待统计设计。
- 图片：<CC BY 4.0, 原图未修改 | 自制 | AI 生成示意>。
- 不良事件：如听众提及 AE，按公司 PV 流程 24h 内上报。
- 审批：<MLR/医学审核编号 placeholder>
```

---

## 6. Visual taste rules

1. **Image + text on every slide.**
   - Each slide has ≥1 picture, chart or native diagram. Only the references page is exempt.
2. **One hero per slide.**
   - The hero visual covers ≥40% of the content area.
   - Text supports the hero; it does not compete with it.
3. **Few boxes.**
   - ≤8 substantive text boxes, ≤220 CJK characters, ≤90 Latin words per slide.
   - Merge label + value into one box with line breaks instead of using two boxes.
4. **Charts.**
   - Use matplotlib, setting colours from `THEME.json` (Dark Blue `#10384F` first, then `#0091DF`, `#00BCFF`, `#66B512`).
   - Prefer native PPT charts when the data must stay editable.
   - No gridline clutter. Label data directly.
5. **Infographics.**
   - Use AntV via infographic-creator with `antv_theme.palette` for flows, sequences and roadmaps.
   - Use native shapes for study schematics.
6. **Literature figures.**
   - Crop to the relevant panel. Never redraw data inside a cropped figure.
   - Caption sits directly under the figure (§7).
7. **Big numbers.**
   - At most one per slide, 40–54 pt, in `#0091DF` or `#10384F`.
   - Always paired with a source line.
8. **AI imagery.**
   - Only on the cover and concept pages, captioned `概念示意（AI 生成）`.
   - Use flat or photographic Bayer-palette mood. No 3D people, no fake clinical images.
9. **Accent colour.**
   - Use one accent per slide: MEDRAD `#E46C0A` **or** Fuchsia `#FF3162`, not both.
   - Do not use red or raspberry "warning" frames. The visual language is never alarm-coded.
10. **Icons.**
    - Outline Radiology icons, `#10384F`, from `icons/`.
    - Icons support titles; they never replace them.

---

## 7. Figure sourcing and licence captions

| Source | Allowed? | Caption / action |
|---|---|---|
| Open-access, CC BY 4.0 | ✓ Preferred | `{描述}。{Author} et al., {Journal} {Year}, Fig. {N} · CC BY 4.0` |
| CC BY-NC / NC-ND | Internal or academic exchange only after Medical Affairs check; no cropping for ND | Add `CC BY-NC-ND 4.0, 原图未修改` |
| Publisher © (no OA licence) | ✗ Do not screenshot | Redraw from reported numbers as a matplotlib chart, captioned `自制：数据取自 {Author Year}` |
| Product / OM content | ✓ | `自制：产品参数范围取自 Operation Manual §{x}` |
| AI-generated | Cover/concept only | `概念示意（AI 生成）` |

**Checklist:**

- [ ] Every figure caption is complete and not truncated. v4 S4 was cut off at `· CC`; widen the box or shorten the description.
- [ ] Every cropped figure caption says `局部` if a panel was cut out. Otherwise say `原图未修改` on the references page.
- [ ] Every figure source appears on the references slide with its PMID/DOI.
- [ ] Licence status is recorded in the notes block (§5).
- [ ] Caption style: 9–10 pt, `#10384F` at ~70% tint or Mid Blue `#00617F`, left-aligned to the figure edge.

---

## 8. Example layout specs (from v4)

**About the geometry.** Values are % of a 16:9 slide, measured from the top-left corner (x = left edge, y = top edge, then w, h).

- Master chrome occupies roughly y 0–15% for the title and y 93–100% for the footer.
- The content area is about x 4–96%, y 17–91%.
- Re-measure the actual deck with:
  `python -c "from pptx import Presentation as P;[print(i+1,s.name,round(s.left/121904,1),round(s.top/68580,1),round(s.width/121904,1),round(s.height/68580,1)) for i,sl in enumerate(P('deck.pptx').slides) for s in sl.shapes]"`

### Spec A — Proposal design page (v4 S13, lint: 6 boxes, 179 CJK, OK)

**Layout:** `MEDRAD Centargo Text Slide with logo`

| Element | x / y / w / h (%) | Style | Copy |
|---|---|---|---|
| Title (placeholder) | master | 24–28 pt, `#10384F` | `提案 A｜CCTA：探索按碘流率个体化能否让冠脉强化更稳定` |
| Subtitle / design line | 4 / 15 / 92 / 5 | 14 pt, `#00617F` | `PCCT CCTA · P3T Cardiac 体重因子 vs 碘流率目标方案 · 前瞻随机` |
| **Hero: design schematic** (native shapes, 1 group) | 4 / 22 / 54 / 52 | Population pill → randomisation diamond → two arm bars (`#10384F` / `#0091DF`) → reading box (`55 keV VMI`) → endpoint target icon | Arm 1 `P3T® Cardiac · 体重因子 (gI/kg)`; Arm 2 `碘流率目标 (gI/s)` |
| Hypothesis card | 61 / 22 / 35 / 18 | White card, 1 pt `#0091DF` left bar, 13 pt | `研究假设 / 以 Busselot 类碘流率目标给药，个体间冠脉强化离散度低于按体重因子给药；低 keV 档可进一步下调碘量。` |
| Endpoints card | 61 / 43 / 35 / 31 | Same style; primary in bold | `主要终点 / 55 keV 近端冠脉 HU 落入目标窗的比例 / 变异系数` + `次要终点 / 总碘量 · 主观图像质量 · 碘流率实测值` |
| Value strip | 4 / 78 / 92 / 9 | `#10384F` fill, white 13 pt, one outline icon | `科室价值 / 首个 PCCT 上 IDR vs 体重因子前瞻比较 · 方案标准化 · 可追溯注射数据` |
| Source line | 4 / 88 / 92 / 3 | 9 pt | `Busselot 2026; Lin 2026 · 样本量待统计设计` |

**Notes:** §5 block naming the OM §9 range, stating that the IDR target is investigator-defined and that no reduction is promised.

### Spec B — Hero literature figure + key number (v4 S4, lint: 8 boxes, 147 CJK, OK)

**Layout:** `MEDRAD Centargo Text Slide with logo`

| Element | x / y / w / h (%) | Style | Copy |
|---|---|---|---|
| Title | master | 24–28 pt | `降低 keV，碘更亮：每降 5 keV 约可减 10% 对比剂` |
| Subtitle | 4 / 15 / 92 / 5 | 14 pt, `#00617F` | `Jeukens 2026「10-to-5 规则」——体模推导、患者回顾验证；为低碘方案提供可计算的起点` |
| **Hero: literature figure** | 4 / 22 / 58 / 62 | Cropped panel, no border | Jeukens et al., Fig. 6 (55 vs 45 keV; abdomen + CTA) |
| Figure caption | 4 / 85 / 58 / 5 | 9 pt, **full licence, no truncation** | `同一检查 55 keV（左）vs 45 keV（右）：上排门脉期腹部、下排 CTA。Jeukens et al., Invest Radiol 2026, Fig. 6 · CC BY 4.0` |
| Big number | 66 / 24 / 30 / 16 | 48 pt, `#0091DF` | `≈10%` |
| Number label | 66 / 41 / 30 / 10 | 13 pt | `每降 5 keV 可减少的对比剂（临床规则） / 体模结果 11.7–14.5%` |
| Rule card | 66 / 54 / 30 / 22 | White card, `#10384F` left bar | `研究意义 / keV 与碘量可联合设计 → 提案 C 的出发点` |
| Icon | 66 / 78 / 6 / 8 | Outline, `#10384F` | (keV / spectrum icon) |

**Notes:** the rule was phantom-derived and validated retrospectively; it is not a product claim; the figure is CC BY 4.0 and cropped.

**Also good in v4:**

- **S7:** two figures, 6 boxes, a positive bridge sentence replacing the v3 red-line box.
- **S11:** data-chain hero, 7 boxes.
- **S17 / S18:** proposal C design + evidence pair, both within limits.

---

## 9. Self-check checklist

Run before every export:

```bash
/home/box/tools/ppt-master/.venv/bin/python scripts/lint_slide_face.py build/<deck>.pptx
```

**What the lint checks (slide face only; notes are skipped for banned words):**

| Check | Threshold | Result |
|---|---|---|
| Banned words: `红线 合规 规避 red line compliance Smart Protocol` | any occurrence | **BANNED → exit 1** |
| Substantive text boxes | > 8 | warn |
| CJK characters | > 220 | warn |
| Latin words | > 90 | warn |
| No picture / chart | 0 | warn |

**Release targets:**

- Exit 0 and `banned_slides=0`.
- Warnings are allowed only for:
  - the references slide (`no image/chart`, words);
  - at most 2 overview pages, with a justification in the notes.

**Manual checklist:**

- [ ] The arc follows §2. Every proposal has hypothesis · schematic · endpoints · literature figure · department value.
- [ ] Every title is an assertion. Every proposal title uses `探索…能否…`.
- [ ] Product names are registered and exact. No invented features.
- [ ] Every number traces to a cited paper (`原文报告`) or an OM section. No product-attributed percentages.
- [ ] No off-label use is shown as a feature. Research settings are marked `研究者定义方案`.
- [ ] Sample sizes and margins read `待统计设计`.
- [ ] Every slide has a hero visual. Captions are complete with licence.
- [ ] The §5 notes block is present on every content slide.
- [ ] Brand checks pass: POTX layouts with logo intact, Color Guide hues only, Arial, one accent, outline icons.
- [ ] The references slide lists PMID/DOI plus the figure licence list.
- [ ] Classification ribbon reminder is given if the deck is internal.

---

## 10. v3 → v4 lessons

| v3 problem (lint / review) | v4 fix | Rule going forward |
|---|---|---|
| "Red-line" boxes on the slide face. Banned words on S7, S8, S14 (红线, Smart Protocol) and S21 (合规) | Constraints moved into the notes block; S7 became a positive bridge sentence (`从「能减」到「怎样个体化」`) | §4.3, §5 |
| Invented name "Smart Protocol" | Registered P3T® Cardiac / PA / Abdomen, PAT, DualFlow, Data Manager | §4.2 |
| Dense proposal pages S16–S18 (12–14 boxes, 231–273 CJK, 100–134 words) | Each proposal split into a design page and an evidence-anchor page; S17/S18 now OK | §3 two-page anatomy |
| S22 had 29 boxes; S21 had 21 boxes | References consolidated as one text frame per column (4 boxes) | One frame per list, never one box per line |
| S06 had no image and 15 boxes | Synthesis charted. Still 16 boxes in v4 S6 → next pass: one chart + one takeaway | Chart replaces stat tiles |
| Product credited with literature reductions | Numbers attributed to Author Year (`原文报告`); product described via OM ranges | §4.5–4.6 |
| Truncated licence caption (v4 S4 `· CC`) | Full `CC BY 4.0` caption | §7 checklist |
| Remaining v4 warnings: box counts on S5, S6, S8–S10, S12, S14, S16, S19, S20 | Group tile label + value into single boxes; use AntV/native groups for overview grids | Target ≤2 warn slides besides references |