# Chart intent map

## 1. Purpose

This file maps **what a slide needs to say** (intent) to **which layout to build**. It covers Chart Pool (CP, 330 slides, 1-based), BC Chart Library (BC, 271 slides) and the AntV templates. Choose the intent first and the pattern second. This keeps decks from defaulting to cards-grid and keeps the visual form matched to the message.

Build everything on the Bayer master with native shapes or AntV, using the Color Guide 12 hues. Body text is Dark Blue `#10384F`.

Use only the indices listed in this file. If an index isn't listed here, inspect the slide (section 6) before using it.

## 2. Per-slide procedure

1. **Write one sentence** stating the slide's message (a claim, not a topic).
2. **Classify the intent** from the signal words in the table (EN + 中文). If two intents match, take the one the verb of your sentence points to.
3. **Pick 1-2 candidates** from the CP / BC / AntV columns. Prefer the one that fits the content count (steps, items, series).
4. **Assemble on the master** with native shapes or AntV, in the Bayer palette. Don't paste pool slides unedited.
5. **Record the choice in the speaker notes** as:
   `INTENT: <id> | PATTERN: CP##/BC##/antv`
   For AntV, write `antv:<template>`. Example: `INTENT: timeline-roadmap | PATTERN: BC150`.

## 3. Intent taxonomy

| intent id | signal words | CP indices | BC indices | AntV | data-chart option | avoid when |
|---|---|---|---|---|---|---|
| progression-sequence | step, stage, process, then, workflow, 步骤, 流程, 阶段, 依次 | 78-94 (N-steps, triangle process, options, road to success) | 129-137 (process 1-9), 138-139 (increasing/decreasing), 140 (mapping), 63 (increasing list), 183 (ADKAR), 182 (value chain) | sequence-steps-horizontal, sequence-steps-vertical, sequence-ascending | column for stepwise values (CP 10-21) | steps have no order, or there are more than 9 |
| hierarchy | level, layer, reports to, top-down, 层级, 架构, 组织, 上下级 | 27-40 (organigrams, spheres tree), 57-65 (pyramids, toolbox) | 114-118 (pyramids), 113 (temple), 105 (bottom-up/top-down) | hierarchy-tree-basic, hierarchy-org-tree, hierarchy-pyramid, hierarchy-mindmap | none | items are peers, or the "levels" are only visual decoration |
| classification | type, category, group, segment, bucket, 分类, 类别, 分组, 归类 | 139-165 (circular shapes, 3-6 pieces, toolkits) | 74-90 (elements/categories), 60-62 (buckets), 170 (clustering), 180 (ABC), 15-16 (scope in/out), 64 (multi-dim list) | list-column-vertical, list-row-simple, list-grid-card | none | items form a sequence or hierarchy |
| comparison | vs, compare, differ, versus, option A/B, 对比, 比较, 差异, 方案 | 41-48 (butterfly), 22-26 (tables) | 45-47 (decision matrix), 43 (pros/cons) | compare-binary-horizontal, compare-table, compare-vs | clustered column or bar (CP 10-21) | there are more than 4 options with more than 5 criteria (use a table) |
| cause-effect | because, leads to, driver, root cause, impact, 因果, 原因, 导致, 影响, 驱动 | 78-94 (factor results) | 123-127 (consequences), 91-93 (factors), 100-104 (influencing factors), 171 (iceberg) | relation-flow, hierarchy-iceberg | waterfall for contribution to an effect (CP 10-21) | correlation is shown without a causal claim |
| cycle-loop | cycle, loop, iterate, continuous, feedback, 循环, 闭环, 迭代, 持续 | 139-165 (circular shapes, arrows) | 66-72 (circles/cycle) | sequence-circle-process | none | the process has a clear start and end |
| matrix-2x2 | quadrant, prioritize, high/low, portfolio, 象限, 矩阵, 优先级, 二维 | 95-138 (PM toolbox: matrices, SWOT) | 142-143 (target matrix), 179 (BCG 2x2), 184 (SWOT), 45-47 (decision matrix) | compare-quadrant, chart-quadrant | none native in pool; use chart-quadrant for plotted items | the axes are not independent or the items are not scored |
| funnel | conversion, filter, drop-off, narrowing, pipeline, 漏斗, 转化, 筛选, 层层递减 | none verified | 57-59 (funnels) | sequence-funnel | bar for stage counts (CP 10-21) | stage values don't decrease |
| timeline-roadmap | timeline, milestone, phase, schedule, roadmap, 时间线, 里程碑, 路线图, 阶段计划 | 166-173 (timelines, arrows, trend chart) | 25-31 (gantt), 32-34 (phases), 150 (strategy roadmap) | sequence-timeline-horizontal | line for trend over time (CP 10-21, 166-173) | there are no dates or ordered phases |
| relationship-network | interact, depend, connect, ecosystem, 关系, 关联, 网络, 相互作用 | 27-40 (connected spheres), 239-243 (puzzle, cubes, gears) | 159-162 (interrelation), 96-97 (puzzle), 98 (gears), 172 (cubes) | relation-network, relation-flow, relation-circle | none | there are more than about 8 nodes, or the links carry no meaning |
| part-to-whole | share, proportion, composition, %, 占比, 构成, 份额, 比例 | 10-21 (pie, doughnut, stacked), 139-165 (circular pieces) | 74-90 (elements) | relation-circle | pie or doughnut (up to 6 slices); stacked column for time | slices exceed 6, or the parts don't sum to a whole |
| before-after | from-to, today vs future, shift, transform, 现状, 转变, 从…到…, 前后 | 78-94 (status quo) | 122 (From-To) | sequence-from-to, compare-binary-horizontal | paired column; waterfall for the change | no real change is claimed |
| kpi-highlight | key number, headline figure, fact, 关键数据, 核心指标, 一图看懂 | 22-26 (key-fact tables), 95-138 (key facts) | 53 (key facts), 151-157 (summary) | list-row-simple, list-grid-card | single column or big number | there are more than 4 numbers (use a table or chart) |
| evidence-cited-figure | figure, Fig., paper, study shows, source, 论文图, 原图, 文献, 引用, 来源 | 71-77 (photo usage), 66-70 (text boxes for takeaway) | 50-52 (photo + text) | none (never redraw) | **No.** Use a source crop; see the evidence rule below | the source image is unavailable or the resolution is too low (then use kpi-highlight with a citation) |
| overlap-venn | overlap, intersection, common ground, 交集, 重叠, 共同点, 韦恩 | 49-56 (Venn 2-6) | 94-95 (intersection) | relation-venn | none | the sets are not truly overlapping or there are more than 4 sets |
| tension-tradeoff | trade-off, conflict, balance, dilemma, risk vs chance, 权衡, 矛盾, 两难, 取舍 | 41-48 (butterfly) | 108 (time-cost-quality), 109-111 (tension/conflict), 164 (chances/risks), 43 (pros/cons) | compare-vs, compare-binary-horizontal | none | one side clearly dominates (use comparison) |
| decomposition-logic-tree | break down, MECE, sub-problem, drivers of, 拆解, 分解, 逻辑树, 要素 | 27-40 (spheres tree) | 186-187 (logic tree), 55-56 (best-fit tree), 163 (logical dimensions) | hierarchy-tree-basic, hierarchy-mindmap | none | the branches overlap or are not exhaustive |

**Evidence rule (evidence-cited-figure).** Use a crop of the original figure from the source, never a redrawn or re-plotted version. Keep axes, labels and colors as published. Add a citation line under the crop (author, year, figure number) and a one-sentence takeaway in a native text box. Don't recolor the figure to the Bayer palette.

## 4. Diversity rules

- **Family cap:** no single pattern family may exceed **30% of content slides**. Families are the CP index group, the BC index group, or the AntV prefix (`list-`, `sequence-`, `hierarchy-`, `compare-`, `relation-`, `chart-`).
- **No adjacent repeats:** consecutive slides must not use the same pattern. Avoid the same family too, unless the content demands it.
- **Intent variety:** a deck with **10 or more content slides** needs at least **4 distinct intents**.
- **Cards-grid is the fallback, not the default.** Use `list-grid-card` only when no other intent fits after step 2 of the procedure. Record the reason in the speaker notes.
- Check these rules once over the finished deck by reading the INTENT / PATTERN lines in the notes in slide order.

## 5. Worked example: academic-promotion deck

| # | slide | one-sentence message | intent | pattern |
|---|---|---|---|---|
| 1 | why-now | Adoption has tripled in five years, so the window to act is now. | kpi-highlight | BC53, or CP 95-138 key facts; AntV `list-row-simple` as alternative |
| 2 | method | Our approach runs in four ordered stages from sample to readout. | progression-sequence | BC129-137, or `antv:sequence-steps-horizontal` |
| 3 | results | The published figure shows a clear effect versus control. | evidence-cited-figure | BC50-52 with a source crop and citation line |
| 4 | comparison | Option B beats A and C on the three criteria that matter. | comparison | BC45-47, or `antv:compare-table` |
| 5 | proposal design | The proposal breaks into three work packages, each with sub-deliverables. | decomposition-logic-tree | BC186-187, or `antv:hierarchy-tree-basic` |
| 6 | roadmap | Delivery runs in three phases over 18 months. | timeline-roadmap | BC150, or CP 166-173 |

Check: six distinct intents and six distinct families, with no adjacent repeats.

Notes example for slide 6:
`INTENT: timeline-roadmap | PATTERN: BC150`

## 6. Inspecting a pool slide

Before using a CP slide, look at it:

```bash
python scripts/chart_pool_index.py --grep timeline   # find slides by keyword
python scripts/chart_pool_index.py --show 168        # show slide 168 (1-based)
python scripts/chart_pool_index.py --lib bc --grep funnel   # BC Chart Library (default --lib cp = Chart Pool)
```

- Search with the English keyword first (`funnel`, `venn`, `waterfall`), then try the intent's signal words.
- Confirm that the item count, text volume and shape type fit your content before committing.
- If a slide is outside the ranges in section 3, treat its index as unverified and don't record it in `PATTERN:` until checked.