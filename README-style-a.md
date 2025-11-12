# Snowflake Automation Suite

> Unified GitHub Actions, reusable TypeScript libraries, and Go-powered dashboards for Snowflake DevOps.

## 🚀 Pillars

| Pillar | Highlights |
| --- | --- |
| **Reusable Actions** | `Snowflake.CortexAI.AgentAction`, `Snowflake.CortexAI.AnalystAction`, `Snowflake.CortexAI.SearchAction`, `Snowflake.RunSQLAction`, `Snowflake.AISQLAction` *(WIP)* – publish-ready harnesses + Marketplace releases. |
| **Shared Libraries** | `@marcelinojackson-org/snowflake-common` wraps Snowflake SDK + Cortex REST APIs (connection health, runSql, Analyst, Search, Agent helpers). |
| **Testing & CI** | `Snowflake.Testing` repo orchestrates local scripts + GitHub workflows, validating both source actions and published Marketplace tags for every change. |
| **Observability** | `Snowflake.FrostCTL` *(WIP, Go + Bubble Tea)* delivers a k9s-style TUI for warehouses, queries, tasks, and AI runs. |

## 🛠️ GitHub Action Catalog

| Action | Purpose | Extras |
| --- | --- | --- |
| `Snowflake.CortexAI.AgentAction` | Calls Cortex Agents with tool-choice, thread support, SSE parsing. | Quiet persistence (`persist-results`), timestamped artifacts, auto-cleanup. |
| `Snowflake.CortexAI.AnalystAction` | Semantic-model analytics with `include-sql`, result-formatting, SQL extraction. | Linked to `snowflake-common` for consistent connection + logging. |
| `Snowflake.CortexAI.SearchAction` | Search indices, filters, rerankers, field selection. | Integration tests ensure deterministic responses. |
| `Snowflake.RunSQLAction` | General Snowflake SQL execution with row limits + CSV/JSON outputs. | Powers follow-up steps when AI returns SQL-only responses. |

## ✅ Testing Strategy

1. **Local scripts** (e.g., `scripts/local-cortex-agent.sh`)  
   - Build `snowflake-common` + action.  
   - Run basic + advanced scenarios with persistence enabled.  
2. **`snowflake-connect-ci.yml`**  
   - Executes every local harness.  
   - Runs the published Marketplace tag to detect drift.  
3. **Dedicated Marketplace checks** (`snowflake-cortex-agent-marketplace.yml`, etc.)  
   - Ensure secrets + org variables wire correctly before public releases.

## 🧱 Shared Library (`snowflake-common`)

- Connection orchestration (`getSnowflakeConnection`, `runSql`).
- Cortex surfaces:
  - `runCortexSearch`
  - `runCortexAnalyst`
  - `runCortexAgent` (SSE parser, tool-choice validation, normalized thread IDs).
- Jest coverage for all helpers (mocked SDK + SSE streams).

## 🧊 FrostCTL (Go TUI)

| Feature | Details |
| --- | --- |
| Warehouses View | Live concurrency, credit burn, auto-suspend countdowns. |
| Queries View | Active/failed queries with SQL previews + cancellation hotkeys. |
| Cortex Tab | Streams latest Analyst/Search/Agent runs alongside GitHub workflow links. |
| Config | Cobra CLI + Viper profiles; Bubble Tea + Lip Gloss styling. |

## 📦 Release Cadence

1. Implement feature in action + `snowflake-common`.  
2. Update local harness + README usage examples.  
3. Run `Snowflake.Testing` CI (local + published).  
4. Tag (`vX.Y.Z`), craft release notes, publish to Marketplace.  
5. Reference the new tag in testing workflows.

## 📅 Roadmap / WIP

- `Snowflake.AISQLAction`: action scaffolding done; marketplace release scheduled after advanced prompt coverage.
- `Snowflake.FrostCTL`: warehouse/query panes live; adding AI + DevOps panels before GA.
- `Snowflake.Terraform` & `Snowflake.Ansible`: infrastructure-as-code modules planned (design stage).

---

_Maintained by Marcelino Jackson • Building reliable Snowflake automation one action at a time._
