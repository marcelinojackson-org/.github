# Marcelino Jackson · Snowflake Automation Portfolio

![CI](https://github.com/marcelinojackson-org/Snowflake/actions/workflows/snowflake-connect-ci.yml/badge.svg)

## Table of Contents
1. [Mission](#mission)
2. [Repositories](#repositories)
3. [Action Matrix](#action-matrix)
4. [Testing & Release Workflow](#testing--release-workflow)
5. [Tooling Highlights](#tooling-highlights)
6. [Contact](#contact)

## Mission

Deliver production-grade Snowflake automation: reusable GitHub Actions, shared TypeScript libraries, Go-based observability, and rigorous CI pipelines.

## Repositories

| Repo | Role | Tech |
| --- | --- | --- |
| `Snowflake.Common` | Core TypeScript helpers (connection, runSql, Cortex Analyst/Search/Agent). | TypeScript + Jest |
| `Snowflake.CortexAI.AgentAction` | Marketplace-ready action for Cortex Agents with persistence + SSE parsing. | TypeScript + NCC |
| `Snowflake.CortexAI.AnalystAction` | Semantic view analytics with SQL extraction outputs. | TypeScript |
| `Snowflake.CortexAI.SearchAction` | Full-text / metadata search action. | TypeScript |
| `Snowflake.RunSQLAction` | Generic Snowflake query execution. | TypeScript |
| `Snowflake.AISQLAction` | AI SQL helpers for advanced workloads. | TypeScript |
| `Snowflake.Testing` | Integration scripts + workflows for local + published verifications. | Bash + GitHub Actions |
| `Snowflake.FrostCTL` | Bubble Tea TUI for live Snowflake monitoring (warehouses, queries, tasks, AI). | Go |

## Action Matrix

| Action | Inputs | Outputs | Notable Features |
| --- | --- | --- | --- |
| `CortexAI.AgentAction` | `agent-name`, `message/messages`, `tool-choice`, `persist-results`. | `result-json`, `result-file`, `answer-text`, `events-json`. | Tool-choice validation, thread-aware, timestamped persistence, 24h cleanup, SSE parsing. |
| `CortexAI.AnalystAction` | `semantic-model-path` / `semantic-view-path`, `include-sql`, `result-format`. | `result-json`, `generated-sql`. | SQL extraction, verbose logging, deterministic tests. |
| `CortexAI.SearchAction` | `service-name`, `query`, `limit`, filters, rerankers. | `response-json`. | JSON filter parsing, reranker support, strict validation. |
| `RunSQLAction` | `sql`, row limits, CSV/JSON toggles. | Rows + metadata, optional artifacts. | Enforces row caps, supports artifact uploads. |
| `AISQLAction` | AI prompt/LLM selections. | JSON responses. | Streams Snowflake AI SQL functions. |

## Testing & Release Workflow

1. **Local harnesses** (`scripts/local-*.sh`): build `snowflake-common`, link action, run basic + advanced cases with persistence and env-driven prompts.
2. **`snowflake-connect-ci`**: executes every local harness, then runs the published Marketplace tag for each action.
3. **Marketplace workflows** (e.g., `snowflake-cortex-agent-marketplace.yml`): on-demand verification with org secrets.
4. **Release flow**:
   - Commit changes in `Snowflake.Common` + action repo.
   - Tag `vX.Y.Z`, draft release notes (title + feature bullets).
   - Publish action to Marketplace.
   - Update testing workflows to pin the new tag.

## Tooling Highlights

- **Persistence**: `persist-results` writes large payloads to timestamped files (`agent-result-YYYYMMDD-HHMMSS-epoch.json`) and auto-cleans files older than 24h.
- **Quiet Outputs**: Local runs suppress `setOutput` noise; GitHub Actions still receive full outputs.
- **FrostCTL**: Go CLI with Cobra + Bubble Tea for real-time Snowflake visibility (warehouses, queries, AI activity).
- **Shared Library**: `snowflake-common` now includes `runCortexAgent` with strict validation + SSE event parsing.

## Contact

- Maintainer: **Marcelino Jackson**
- GitHub: [@marcelinojackson-org](https://github.com/marcelinojackson-org)
- Marketplace: Search for “Snowflake.*Action” to view published actions.
