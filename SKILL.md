---
name: magic-prompt-skill
description: "The complete autonomous project kickoff & engineering pipeline. Integrates token hygiene (agent-stack-optimizer / TokenEconomizer), discovery & OKR alignment (Chief of Staff), brainstorming (superpowers), decision mapping (wayfinder), deep grilling (grill-me), multi-perspective validation (llm-council for architecture, roast-room for product/business), project governance (intent.md, claude-code-setup), high-performance build tooling (rstackjs: Rsbuild, Rspress, Rslib, Rsdoctor), TDD deep-module implementation (implement, gstack), and independent cross-family review (claudex-loop). Governed by 3 hard approval gates. Self-heals by checking and installing missing skills via doctor.py. Triggers: /magic-prompt-skill, /superpowers, /kickoff."
---

# Magic Prompt Skill: The Autonomous Project Kickoff & Engineering Pipeline

The universal orchestration pipeline for new initiatives, features, and complex engineering across Claude Code, Codex, Antigravity, and OpenClaw/Jev.

Instead of writing a complex 20-line kickoff prompt at every session launch, `/magic-prompt-skill` (aliased as `/superpowers` and `/kickoff`) runs a hardened 4-phase pipeline governed by **Layer 0 token hygiene**, **high-performance Rust build toolchains (`rstackjs`)**, **3 non-negotiable human approval gates**, and **cross-family independent verification**.

---

## Pre-Flight Check: Self-Healing Skill Dependencies

Before executing the pipeline, the skill automatically verifies that all dependencies exist across your environment:

```bash
python3 scripts/doctor.py --fix
```

If any core skill (`brainstorming`, `wayfinder`, `grill-me`, `llm-council`, `roast-room`, `claudex-loop`, etc.) is missing, the doctor script automatically locates it in local caches/registries and symlinks or installs it into your active skills directory (`~/.agents/skills/`, `~/.claude/skills/`, `~/.codex/skills/`, or OneDrive).

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Layer 0: Context Hygiene & Token Economizer (Passive Background Engine)    │
│  • agent-stack-optimizer (MarkItDown Office/PDF to text + 50% Handoff Guard)│
│  • TokenEconomizer (Dynamic tool pruning + 3-strike circuit breaker on loop)│
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  Phase 1: Discovery, OKRs & Brainstorming                                   │
│  1. Chief of Staff OKR check ──▶ 2. /find-skills ──▶ 3. brainstorming       │
│  4. /wayfinder (Map frontier & tickets) ──▶ 5. /grill-me (Relentless Q&A)   │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
                       [⛔ HARD-GATE 1: Plan & Map Approval]
                                       │
┌──────────────────────────────────────┴──────────────────────────────────────┐
│  Phase 2: Dual-Validation Council (Business vs Architecture)                │
│  • Commercial / Product / Go-to-Market ──▶ /roast-room (Bezos, Hormozi, PG) │
│  • Technical / Engineering Architecture ─▶ /llm-council (Haiku / Flash / V3)│
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
                     [⛔ HARD-GATE 2: Council Verdict Approval]
                                       │
┌──────────────────────────────────────┴──────────────────────────────────────┐
│  Phase 3: Governance, Documentation & Project Contract                      │
│  6. intent.md (Root, verbatim words) ──▶ 7. claude-code-setup / Pocock Docs │
│  • Documentation Engine: Rspress (rstackjs) for docs sites & specs          │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
                     [⛔ HARD-GATE 3: Pre-Implementation Approval]
                                       │
┌──────────────────────────────────────┴──────────────────────────────────────┐
│  Phase 4: Implementation, Build Toolchain & Cross-Family Review             │
│  8. Toolchain: Rsbuild / Rslib (sub-second builds, zero token lag)          │
│  9. /implement (Pocock Deep Modules + strict TDD) ──▶ 10. /gstack (Rsdoctor)│
│  11. /claudex-loop (Cross-Family Peer Inspection: Claude ⇆ Codex/Antigravity│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Detailed Execution Protocol

### Layer 0: Context Hygiene & Token Economizer
*Runs silently in the background across all phases.*
1. **Document Ingestion (MarkItDown Hook):**
   - Whenever specs, briefs, PDFs, or Office files (`.docx`, `.xlsx`, `.pptx`) are inspected, they are parsed as clean Markdown text via `agent-stack-optimizer`, eliminating massive vision/binary token waste.
2. **Handoff Guard:**
   - Warns at 50% context usage. If a phase approaches 60%, automatically writes an atomic `handoff` ticket so a clean session can resume without context rot.
3. **Loop Circuit Breaker:**
   - If `/implement` or test executions fail 3 times on the same error, execution halts and triggers `systematic-debugging` instead of spinning tokens.

---

### Phase 1: Discovery, OKR Alignment & Brainstorming
*Model tier: Fast interactive reasoning (Sonnet, Gemini Flash, GPT-4o).*

1. **Strategic Intent (Chief of Staff check):**
   - Check user priorities (`profile/USER.md` or OKRs): *Does this initiative directly serve current strategic goals?*
2. **Context & Skill Recon:**
   - Run `/find-skills` and `/ponytail` to scan repository conventions, existing architecture, and applicable tools.
3. **Intent Classification:**
   - Invoke `superpowers:brainstorming` and declare classification out loud: **Spike**, **Bounded**, or **Architectural**.
4. **Wayfinding:**
   - Invoke `/wayfinder` to chart the map:
     - Name the **Destination** in 1-2 lines.
     - Divide open decisions into child decision tickets on the issue tracker.
     - Sketch the **Frontier** and isolate **Fog of war**.
5. **Interactive Grilling:**
   - Invoke `/grill-me`: interview the human partner one question at a time down each branch of the design tree, providing recommended answers until the frontier is settled.

> [!CAUTION]
> ### ⛔ HARD-GATE 1: Destination & Map Sign-Off
> The agent MUST STOP and present the Destination, Scope, and Decision Map. Do NOT convene councils or write code until the user gives explicit affirmative approval.

---

### Phase 2: Dual-Validation Council (Business vs Architecture)
*Model tier: Low-cost high-divergence models (Claude Haiku, Gemini Flash Lite, DeepSeek V3).*

Select the council lens based on the nature of the decision:
- **Commercial / Product / Pricing / Positioning:**
  - Convene **`/roast-room`**: a 7-seat founder board meeting (Bezos, Paul Graham, Hormozi, Gary V, Dan Martell, Gino Wickman, Buffett) debating commercial viability and leverage over 3 rounds.
- **Technical Architecture / Scaling / Systems:**
  - Convene **`/llm-council`**: Karpathy-style 5 independent advisors (Contrarian, First Principles, Expansionist, Outsider, Executor) evaluating edge-cases, failure modes, and structural soundness with peer review and Chairman synthesis.

> [!CAUTION]
> ### ⛔ HARD-GATE 2: Council Verdict Approval
> The agent MUST STOP and present the Council's synthesis, highlighting agreements, clashes, and blind spots. Wait for user confirmation on the chosen path.

---

### Phase 3: Project Governance, Documentation & Contracts
*Model tier: Host coordinator model.*

1. **Write `intent.md`**:
   - Save at the repository root.
   - Contains: user's verbatim requirements, non-negotiable constraints, out-of-scope boundaries, and measurable acceptance criteria.
2. **Adaptive Spec Checklist (sizes the spec to the work):**
   - For a full app build, cover all six aspects before the gate: product requirements (PRD: what the app does and for whom), technical requirements (TRD: which components it is assembled from), app flow (every screen, every click), design brief (the design system), backend schema, and an incremental implementation plan.
   - For a small change, cover only the aspects the change actually touches. Never force six documents for a small edit.
   - These aspects extend `intent.md` into a spec pack. This is a checklist, not a new phase and not a fixed document set.
3. **Scaffold Context & Docs**:
   - Run `/claude-code-setup` or `setup-matt-pocock-skills`.
   - Update `CLAUDE.md` / `AGENTS.md` with issue-tracker location, triage labels, and domain glossaries (`GLOSSARY.md`, `docs/adr/`).
   - If an interactive documentation portal is required, use **`Rspress`** (`rstackjs`) for instant static generation and minimal build overhead.
   - **Workspace Isolation Scaffolding (Optional)**: If the repository leverages worktree isolation for concurrent AI agents, copy `templates/wt.toml` to repo root to automate `.env` hydration and post-checkout dependency installation via `worktrunk` (`wt`).

> [!CAUTION]
> ### ⛔ HARD-GATE 3: Pre-Implementation Approval
> The agent MUST present `intent.md` and the proposed TDD test battery. No production code is modified before the user confirms.

---

### Phase 4: Implementation, High-Speed Build & Cross-Family Review
*Model tier: Premier Coding Engine (Claude 3.7 Sonnet / Opus, OpenAI Codex / o3) + Independent Inspector.*

1. **High-Performance Build Standard (`rstackjs`):**
   - **For new web projects (greenfield):** Default to **`Rsbuild`** for sub-second development server startup and lightning-fast HMR (<100ms), eliminating agent idle wait time.
   - **For packages and libraries:** Standardize on **`Rslib`**.
   - **For existing projects (brownfield):** Preserve existing bundlers (Vite/Next/Webpack); do not force migrations.
2. **Workspace Isolation & TDD Deep Modules Implementation:**
   - **Isolation Seam (`/new-feature`)**: Before editing, ensure branch isolation to prevent cross-agent workspace collisions. Use progressive enhancement:
     - If `wt` (`worktrunk`) is detected: run `wt switch -c "$BRANCH"` (executes `wt.toml` lifecycle hooks for automated `.env` hydration).
     - Otherwise: fallback to standard `git worktree add "../$BRANCH" -b "$BRANCH" origin/main`.
   - Run `/implement` strictly applying Matt Pocock's Deep Module design:
     - Simple interface surface, deep and robust internal capability.
     - **Dynamic-First, Coordinate-Fallback** for all UI/automation elements.
     - Strict **TDD**: write failing test (Red), implement minimum code (Green), refactor clean (Refactor).
3. **Full-Stack QA & Bundle Audit:**
   - Run `/gstack` to verify build targets, integration sanity, and smoke tests.
   - Run **`Rsdoctor`** when bundle bloat, duplicate dependencies, or build speed regressions need diagnosis.
4. **Cross-Family Independent Review (`/claudex-loop`):**
   - The final inspection MUST be run through `/claudex-loop` using an independent peer provider:
     - If **Claude Code** built the code ➡️ **Codex** or **Antigravity** inspects in a fresh session.
     - If **Codex** built the code ➡️ **Claude Code** or **Antigravity** inspects.
   - Verification tests explicitly against every acceptance criterion in `intent.md`.
5. **Completion Receipt & Worktree Teardown:**
   - Output diff summary, proof command results, and close resolved wayfinder tickets.
   - **Worktree Garbage Collection**: Prune merged or abandoned ephemeral worktrees (`wt remove "$BRANCH"` or `git worktree remove "../$BRANCH"`) to eliminate disk amplification and avoid `.git/index.lock` collisions.

---

## Trigger Commands & Aliases
- Primary Slash Command: `/magic-prompt-skill`
- Aliases: `/superpowers`, `/kickoff`
