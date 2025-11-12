<div align="center">

# 🌨️ Snowflake Automation Toolkit
**GitHub Actions · Shared Libraries · Testing Harnesses · FrostCTL**

</div>

---

## 🧭 Overview

- **15+ GitHub Actions** spanning Cortex AI, SQL execution, and testing harnesses.
- **`@marcelinojackson-org/snowflake-common`** powers every action with consistent auth, logging, and Cortex API clients.
- **`Snowflake.Testing`** repository automates integration tests (local scripts + Marketplace tags).
- **`Snowflake.FrostCTL`** provides a Go TUI (Bubble Tea) to monitor warehouses, queries, and AI runs.

---

## 🧩 Components

### 1. GitHub Actions

| Scope | Actions |
| --- | --- |
| AI & Cortex | `Snowflake.CortexAI.AgentAction`, `AnalystAction`, `SearchAction`, `AISQLAction` |
| Core SQL | `Snowflake.RunSQLAction` |
| Utilities | `Snowflake.AISQLAction`, future additions |

Each action ships with:
- Usage examples (basic + advanced).
- Optional persistence + artifact upload.
- Marketplace-ready metadata + release notes.

### 2. Shared Library (`snowflake-common`)

- `getSnowflakeConnection`, `runSql`, `runCortexSearch`, `runCortexAnalyst`, `runCortexAgent`.
- SSE parser + validation for Agent runs.
- Jest suite mocking Snowflake SDK and HTTP calls.

### 3. Testing & Integration (`Snowflake.Testing`)

- `scripts/local-*.sh` harnesses (build/link/run basic + advanced scenarios).
- `snowflake-connect-ci.yml`: executes local harnesses **and** Marketplace tags.
- Dedicated workflows for each published action (manual `workflow_dispatch` for deeper validation).

### 4. Go TUI (`Snowflake.FrostCTL`)

- Cobra CLI + Bubble Tea UI.
- Tabs for warehouses, queries, sessions, and Cortex activity.
- Styled with Lip Gloss; supports multiple Snowflake profiles via Viper.

---

## ⚙️ Release Flow

1. Update `snowflake-common` + action source.
2. Run local harness (`scripts/local-…`) + `snowflake-connect-ci`.
3. Tag `vX.Y.Z`, draft release notes (title + feature list), publish to Marketplace.
4. Update testing workflows to pin new tag (ensuring published binary stays verified).

---

## 📈 Recent Highlights

- **Cortex Agent Action v1.0.0**
  - Tool-choice + thread support.
  - Quiet persistence with auto-cleanup.
  - SSE response parsing + `result-file` output.
- **Testing Enhancements**
  - CI now runs both local source and published actions.
  - Marketplace workflows default to production prompts + persistence.
- **FrostCTL MVP**
  - k9s-style dashboard for Snowflake operations.

---

_Maintained by Marcelino Jackson — Building dependable Snowflake automation end-to-end._
