---
name: magic-prompt-skill
description: "Kickoff e pipeline di ingegneria per iniziative, feature e lavori complessi, con routing proporzionato al task. Instrada tra intervento diretto, scoperta/grilling, council tecnico (llm-council), Roast Room commerciale, governance (intent.md), implementazione TDD con deep modules e review cross-family (claudex-loop). Preflight read-only delle dipendenze (doctor.py), registro prove per ogni passaggio, gate di approvazione proporzionati. Integra selettivamente le skill rstack (new-feature, code-structure, evidence-driven-testing, before-and-after, greploop, unslop). Triggers: /magic-prompt-skill, /kickoff."
---

# Magic Prompt Skill: kickoff e pipeline di ingegneria

Guida di orchestrazione, non un sistema che forza l'esecuzione. Serve a non riscrivere ogni volta il prompt di avvio, ma ogni passaggio vale solo se eseguito e provato (vedi Registro).

Non e' un secondo framework: usa i metodi gia' presenti (Pocock: `grill-me`, `tdd`, `implement`, `diagnosing-bugs`; Claudex; Roast Room) e aggiunge solo routing, registro e gate.

## Regole fisse

- Modello ed effort della sessione restano quelli in uso. Niente cambi a meta' lavoro.
- Leggere questo file non equivale a eseguirlo. Ogni passaggio dichiarato completato richiede un artefatto o un comando/prova nel Registro.
- Le soglie di contesto (50%/60%) richiedono telemetria reale. Se il runtime non la espone, dichiaralo e applica solo azioni che il coordinatore puo' eseguire (es. `handoff` a fine task o a contesto lungo).
- Verifica hook e strumenti attivi nel runtime. Se assenti: "non disponibile", niente finzione.
- Nessuna interfaccia grafica senza schizzo ASCII approvato.
- Approvazioni gia' espresse dall'utente nel messaggio valgono: non richiederle.

## Preflight (sola lettura)

```bash
python3 "<cartella-della-skill>/scripts/doctor.py"
```

Percorso relativo alla skill, non al cwd del progetto. Controlla solo la presenza delle dipendenze, non caricamento ne' esecuzione. Se manca qualcosa: `doctor.py --fix --only <nome>` per un rimedio mirato dalla fonte canonica `~/Progetti/magic-prompt-skill`; mai distribuzione automatica su tutti i runtime.

## Routing per task

Scegli il percorso piu' corto che regge il rischio, dichiaralo in una riga.

| Task | Percorso |
|---|---|
| Piccolo intervento, bug limitato, modifica documentale | Diretto. `diagnosing-bugs` se bug. Nessun council. |
| Requisiti ambigui | `brainstorming` + `/wayfinder` + `/grill-me` (una domanda alla volta, con risposta consigliata). |
| Decisione architetturale significativa | `/llm-council` sulla decisione. |
| Decisione commerciale concreta (prezzo, offerta, posizionamento) | `/roast-room`, modalita' scelta per reversibilita' e costo; leggere roster e brain. |
| Due decisioni distinte, una tecnica e una commerciale | Entrambi i council, uno per decisione. |

Classifica a voce: Spike, Bounded o Architectural. Strategia: controlla se l'iniziativa serve le priorita' in `brain read profile/USER.md`.

## Gate (proporzionati)

- **Gate 1**: Destinazione, scope e mappa decisioni, per lavori non banali. Niente council o codice prima del via.
- **Gate 2**: sintesi del council (accordi, scontri, punti ciechi). Solo se un council e' stato convocato.
- **Gate 3**: `intent.md` e batteria di test TDD proposta, prima di toccare codice di produzione.

Task piccoli: un solo gate o nessuno, se l'utente ha gia' dato l'ok.

## Governance

`intent.md` in radice: requisiti verbatim, vincoli non negoziabili, fuori scope, criteri di accettazione misurabili.

Checklist spec adattiva (estende `intent.md`, non e' una fase ne' un set fisso di documenti): per un'app completa copri PRD (cosa fa e per chi), TRD (da quali componenti e' fatta), flusso app (ogni schermata, ogni click), design brief, schema backend e piano incrementale. Per una modifica piccola solo gli aspetti che tocca. Aggiorna `CLAUDE.md`/`AGENTS.md` (issue tracker, glossario, ADR) con `/claude-code-setup` o i metodi Pocock disponibili, verificando i nomi reali delle skill nel runtime.

## Implementazione

1. Isolamento branch quando serve: `wt switch -c "$BRANCH"` se `wt` e' presente, altrimenti `git worktree add "../$BRANCH" -b "$BRANCH" origin/main`. Template `templates/wt.toml` opzionale.
2. `/implement` con deep modules (interfaccia semplice, interno robusto) e TDD proporzionato al rischio: Red, Green, Refactor. Dynamic-First, Coordinate-Fallback solo per UI/automazione.
3. 3 fallimenti sullo stesso errore: stop e `diagnosing-bugs`, non altri giri.
4. Toolchain: conserva quella esistente. Rsbuild/Rslib/Rspress/Rsdoctor solo per un bisogno tecnico dimostrato (progetto nuovo senza bundler, libreria da pubblicare, regressione di bundle misurata). Nessuna promessa di startup o HMR: si misura.
5. `/gstack` per build e smoke test.
6. Review indipendente `/claudex-loop` (Claude costruisce, Codex o Antigravity ispeziona in sessione nuova, e viceversa) contro ogni criterio di `intent.md`.

## Fonti rstack (selettive, solo se disponibili nel runtime)

`michaelshimeles/rstack` e' un workflow per agenti, distinto dalla toolchain Rust rstackjs. Usa solo cio' che serve:

- `new-feature`: isolamento, quando adatto al repo.
- `code-structure`: subordinata all'architettura esistente.
- `evidence-driven-testing`: prove pertinenti al cambiamento.
- `before-and-after`: se il cambiamento e' visivo.
- `greploop`: solo con integrazione disponibile, autorizzazione PR e limiti espliciti.
- `unslop`: per testi.

## Registro prove (obbligatorio)

Una riga per passaggio, in `kickoff-log.md` del progetto o nel messaggio finale:

`skill | percorso risolto | motivo | stato (eseguita / saltata + motivo / bloccata) | artefatto | comando o prova`

Nessun passaggio "completato" senza prova. Per enforcement rigido serve un runner che valida lo stato, non Markdown.

## Chiusura

Riepilogo diff, risultati dei comandi di prova, ticket wayfinder chiusi, pulizia worktree effimeri (`wt remove` o `git worktree remove`). Poi `/handoff` se il contesto e' lungo.

## Trigger

`/magic-prompt-skill`, `/kickoff`. L'alias `/superpowers` e' rimosso (Superpowers non e' piu' il metodo del setup).
