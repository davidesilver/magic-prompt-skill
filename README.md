# Magic Prompt Skill (magic-prompt-skill)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Toolchain: Rstack](https://img.shields.io/badge/toolchain-Rsbuild%20%7C%20Rspress-purple.svg)](https://github.com/rstackjs)
[![Agents: Claude | Codex | Antigravity](https://img.shields.io/badge/agents-Claude%20%7C%20Codex%20%7C%20Antigravity-orange.svg)](#)

> **The complete, self-healing project kickoff & autonomous engineering pipeline for AI agents.**  
> Built for Claude Code, OpenAI Codex, Antigravity, and OpenClaw.

Stop copy-pasting 20 lines of repetitive setup prompts every time you start a new coding session. `/magic-prompt-skill` (also available via `/superpowers` or `/kickoff`) runs a structured 4-phase orchestration pipeline backed by **background token optimization**, **sub-second Rust build toolchains (`rstackjs`)**, **3 strict human approval gates**, and **independent cross-family peer reviews**.

---

## ⚡ What It Solves

| Problem in Typical Agent Workflows | How `magic-prompt-skill` Solves It |
|---|---|
| **Context bloat & token waste** | Integrates **Layer 0** with [`agent-stack-optimizer`](https://github.com/davidesilver/agent-stack-optimizer) (MarkItDown text extraction + 50% handoff guard) and `TokenEconomizer` loop breakers. |
| **Premature coding without alignment** | Enforces **Phase 1** brainstorming (`superpowers`) + decision mapping (`wayfinder`) + relentless grilling (`grill-me`). |
| **Tunnel vision & fragile architecture** | Dual-validation in **Phase 2**: business stress-testing via `/roast-room` and technical validation via `/llm-council`. |
| **Slow agent ReAct loops & long builds** | Standardizes on **`rstackjs`** (Rsbuild, Rspress, Rslib, Rsdoctor) for instant compilation and sub-second feedback loops. |
| **Missing skills & setup drift** | Built-in **Pre-flight Doctor** (`scripts/doctor.py --fix`) that auto-detects and installs missing skills across all your client folders. |
| **Coding on unclear specs** | **Phase 3** adaptive spec checklist: PRD, TRD, app flow, design brief, backend schema, incremental plan. All six for a full app; only what the change touches for small edits. |
| **Self-review bias in code generation** | Mandatory **Phase 4** independent cross-family inspection via `/claudex-loop` (e.g., Codex checks Claude's code against `intent.md`). |

---

## 🏗️ Architecture

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
│  Phase 4: Implementation, High-Speed Build & Cross-Family Review             │
│  8. Toolchain: Rsbuild / Rslib (sub-second builds, zero token lag)          │
│  9. /implement (Pocock Deep Modules + strict TDD) ──▶ 10. /gstack (Rsdoctor)│
│  11. /claudex-loop (Cross-Family Peer Inspection: Claude ⇆ Codex/Antigravity│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### 1. Installation
Clone the repository into your projects directory and run the doctor:

```bash
git clone https://github.com/davidesilver/magic-prompt-skill.git
cd magic-prompt-skill
python3 scripts/doctor.py --fix
```

To symlink into your agent skills directory:
```bash
# Claude Code
ln -s "$(pwd)" ~/.claude/skills/magic-prompt-skill

# Codex
ln -s "$(pwd)" ~/.agents/skills/magic-prompt-skill

# Convenience aliases
ln -s ~/.agents/skills/magic-prompt-skill ~/.agents/skills/superpowers
ln -s ~/.agents/skills/magic-prompt-skill ~/.agents/skills/kickoff
```

### 2. Usage
Open any coding assistant session in your target project and type:

```text
/magic-prompt-skill
```
*(or `/superpowers` / `/kickoff`)*

The agent will automatically verify its environment, run discovery, interview you through the design tree, summon the council, draft `intent.md`, implement via TDD with Rsbuild/Rslib, and run cross-model review.

---

## 🛠️ Doctor & Dependency Auto-Installer

`magic-prompt-skill` ships with a standalone diagnostic engine (`scripts/doctor.py`) that audits your environment:

```text
$ python3 scripts/doctor.py
=====================================================
 🪄 Magic-Prompt-Skill: Pre-flight Doctor Check
=====================================================

[✓] brainstorming                (4/4 locations)    - Superpowers native brainstorming module
[✓] writing-plans                (4/4 locations)    - Superpowers native planning module
[✓] systematic-debugging         (4/4 locations)    - Superpowers native debugging module
[✓] using-superpowers            (4/4 locations)    - Superpowers rule enforcement
[✓] find-skills                  (4/4 locations)    - Context and available skill discovery
[✓] ponytail                     (4/4 locations)    - Repository and context analyzer
[✓] wayfinder                    (4/4 locations)    - Goal mapping, decision tickets, and frontier tracking
[✓] grill-me                     (4/4 locations)    - Relentless interactive design interview
[✓] llm-council                  (4/4 locations)    - Karpathy-style 5-advisor low-cost architecture validation
[✓] roast-room                   (4/4 locations)    - Founder board debate for commercial/product viability
[✓] claude-code-setup            (4/4 locations)    - CLAUDE.md and project governance scaffolding
[✓] implement                    (4/4 locations)    - Engineering build workflow
[✓] gstack                       (4/4 locations)    - Full-stack quality and integration verification
[✓] claudex-loop                 (4/4 locations)    - Independent cross-family plan review and build inspection

Layer 0 Optimization Engines:
[✓] agent-stack-optimizer        Available

Optional Execution & Isolation Accelerators:
[i] worktrunk (wt)               Optional (Not installed) - High-concurrency Git worktree isolation & lifecycle hooks (optional accelerator)
    └─ Recommendation: brew install max-sixty/worktrunk/wt or cargo install worktrunk

🎉 All required skills and tools are properly installed and ready!
```

### 🌿 Workspace Isolation & Worktrunk Acceleration (Optional)

`magic-prompt-skill` natively supports sub-second worktree isolation for parallel agent swarms. While standard `git worktree` is used by default with zero extra setup, installing [worktrunk (`wt`)](https://github.com/max-sixty/worktrunk) provides:
* **Zero-Friction Switching**: Instant branch navigation via `wt switch -c <branch>`.
* **Automated Environment Hydration**: Uses `wt.toml` (sample provided in `templates/wt.toml`) to automatically copy `.env` files and run dependency installation post-checkout.
* **Safe Garbage Collection**: Clean teardown via `wt remove` to avoid lingering `.git/index.lock` collisions.

---

## 📄 License
MIT © [Davide Silvestri](https://github.com/davidesilver)
