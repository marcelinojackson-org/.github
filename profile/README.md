# Marcelino’s OSS Public Portfolio

This workspace curates Marcelino’s published OSS projects across Azure infrastructure, Snowflake GitHub Actions, and Snowflake-native apps/CLIs—with room for additional stacks as they go public.

Current highlights:

- **Azure** – a complete AKS GitOps reference implementation that spans Terraform, Helm, Argo CD, Ansible, Prometheus/Grafana, and k6.
- **Snowflake GitHub Actions** – a family of GitHub Actions, helper libraries, testing harnesses, and internal apps that showcase Cortex AI integrations plus day‑to‑day operational tooling.
- **Snowflake apps, CLI, and labs** – Streamlit dashboards (`Snowflake.FrostyStatus`), a Go-based operations CLI (`Snowflake.SnowCTL`), Snowpark Container Services demos (`Snowflake.SPCS.Lab`), and a reserved IaC track ready to house future Terraform/native assets.

This README is the top-level atlas. Each repository underneath ships with its own README for installation or usage details.

## Portfolio map

### Azure

| Path | Focus | Highlights / Notes |
| --- | --- | --- |
| [Azure.AKS.GitOps.Lab](https://github.com/marcelinojackson-org/Azure.AKS.GitOps.Lab) | Azure Kubernetes Service GitOps lab | Terraform-based cluster bring-up, Helm workloads, Argo CD continuous sync, Ansible automation, observability stack, CLI playbooks, teardown tooling. |

### Snowflake apps, labs, and CLI

| Path | Focus | Highlights / Notes |
| --- | --- | --- |
| [Snowflake.FrostyStatus](https://github.com/marcelinojackson-org/Snowflake.FrostyStatus) | Streamlit dashboard | Snowsight-inspired status board for warehouses, tasks, and jobs with keyboard-friendly exploration. |
| [Snowflake.SPCS.Lab](https://github.com/marcelinojackson-org/Snowflake.SPCS.Lab) | Snowpark Container Services lab | Containerized ETL demo (`spcs-etl-job/`) with Python loader, Dockerfile, staged sample CSVs, and a job spec wired for Snow CLI + compute pools. |
| [Snowflake.SnowCTL](https://github.com/marcelinojackson-org/Snowflake.SnowCTL) | Operations CLI | Go-based `snowctl` binary with connection lifecycle mgmt, SQL runners, JSON/YAML/CSV/TSV output modes, shell completions, and secure local config. |
| [Snowflake.IAC](https://github.com/marcelinojackson-org/Snowflake.IAC) | Future infrastructure | Empty placeholder for eventual Snowflake IaC assets. |

### Snowflake GitHub Actions ([Medium Article](https://medium.com/@mjmarc.common/shipping-ai-powered-snowflake-workflows-with-github-actions-eeb3fe07a354))

| Path | Focus | Highlights / Notes |
| --- | --- | --- |
| [Snowflake.Common](https://github.com/marcelinojackson-org/Snowflake.Common) | Shared TypeScript library | Centralizes `SNOWFLAKE_*` validation, logging controls, and helper APIs (`getSnowflakeConnection`, `runSql`) consumed by every action. |
| [Snowflake.Testing](https://github.com/marcelinojackson-org/Snowflake.Testing) | Validation scripts | Cross-repo build/test harnesses that rebuild shared libraries, package actions, and run local Cortex smoke tests. |
| [Snowflake.RunSQLAction](https://github.com/marcelinojackson-org/Snowflake.RunSQLAction) | GitHub Action | Executes SQL end-to-end, applies safe limits, emits CSV/metadata artifacts for large result sets, and leans on the shared library for connectivity. |
| [Snowflake.CortexAI.AgentAction](https://github.com/marcelinojackson-org/Snowflake.CortexAI.AgentAction) | GitHub Action | Bridges GitHub Actions with Cortex Agents, streaming every event plus a final summary for downstream workflow steps. |
| [Snowflake.CortexAI.AnalystAction](https://github.com/marcelinojackson-org/Snowflake.CortexAI.AnalystAction) | GitHub Action | Connects to Cortex Analyst semantic models/views, exposes optional SQL echoing, and returns structured responses for analytics automation. |
| [Snowflake.CortexAI.SearchAction](https://github.com/marcelinojackson-org/Snowflake.CortexAI.SearchAction) | GitHub Action | Wraps the Cortex Search REST API with filters, pagination, rerankers, and scoring controls. |
| [Snowflake.AISQLAction](https://github.com/marcelinojackson-org/Snowflake.AISQLAction) | GitHub Action (WIP) | Reserved space for upcoming AISQL automation; currently only scaffolding is checked in. |

## [Azure.AKS.GitOps.Lab](https://github.com/marcelinojackson-org/Azure.AKS.GitOps.Lab)

This lab is designed for repeatable cluster builds, controlled experiments, and demos:

- **Provisioning workflow** – Terraform modules carve out the resource group, networking, and AKS cluster. Targeted apply sequences are documented (and scripted) so recreating infra is deterministic.
- **Application layers** – Helm charts deploy nginx, a Flask sample app, Prometheus, and Grafana. Argo CD watches the repo for drift and reconciles the Helm releases automatically.
- **Automation & Runbooks** – Makefile targets, `cli-steps.txt`, and Ansible playbooks encode the exact bootstrap steps, secret hydration, and post-deploy scale adjustments.
- **Observability & Testing** – Prometheus and Grafana arrive pre-wired with datasources/dashboards; k6 scripts deliver programmable load; docs walk through port-forwarding and CI triggers.
- **Operations tooling** – Python scripts under `scripts/` summarize Azure inventory and cost, while `decommission.sh` handles graceful teardown and local cleanup.

See `Azure.AKS.GitOps.Lab/docs/README.md` for diagrams, command references, and troubleshooting guides.

## Snowflake GitHub Actions & Tools

The Snowflake side of the workspace is organized around a few themes.

### 1. Shared foundation

- **`Snowflake.Common`** – guards against misconfigured environments, standardizes connection telemetry, and exposes reusable helpers for SQL execution. Actions depend on the published package and bundle it locally for Marketplace releases.

### 2. Cortex AI automation

- **`Snowflake.CortexAI.AgentAction`** – drives Cortex Agents conversations from CI/CD, capturing both the answer text and every streamed event so workflows can branch on intermediate reasoning or tool invocations.
- **`Snowflake.CortexAI.AnalystAction`** – fronts Cortex Analyst semantic models and semantic views, making it easy to wire natural-language analytics questions into CI pipelines or scheduled jobs.
- **`Snowflake.CortexAI.SearchAction`** – exposes Cortex Search with optional filters, pagination, reranking, score thresholds, and field selection for targeted retrieval use cases.
- **`Snowflake.AISQLAction`** – upcoming AISQL-first action (currently a placeholder). Tracking lives here so downstream repos can reference the path ahead of implementation.

### 3. Core SQL execution

- **`Snowflake.RunSQLAction`** – the baseline action for running SQL inside GitHub workflows. It enforces sensible `LIMIT`s, supports artifact persistence (CSV + metadata), and prints compact run summaries for small queries.

### 4. Operational dashboards & validation tooling

- **`Snowflake.FrostyStatus`** – a Streamlit interface inspired by Snowsight that surfaces the state of warehouses, tasks, and jobs. It emphasizes high-density tables with keyboard navigation and modal detail panes.
- **`Snowflake.Testing`** – bash-based harnesses that rebuild `Snowflake.Common`, package each action locally, and execute representative smoke tests (RunSQL, Cortex Search, Cortex Analyst, Cortex Agent) against a developer’s Snowflake account to catch regressions before publishing.

### 5. Future expansion

- **`Snowflake.IAC`** – intentionally blank for now so new infrastructure-as-code modules can land without reworking repo layout later.

Each sub-repo’s README dives into installation steps, environment requirements, inputs/outputs, and examples. This overview keeps the spotlight on how the pieces fit together across Azure and Snowflake without duplicating usage content.

## [Snowflake.SnowCTL](https://github.com/marcelinojackson-org/Snowflake.SnowCTL)

[Snowflake.SnowCTL](https://github.com/marcelinojackson-org/Snowflake.SnowCTL) houses `snowctl`, a Go 1.25.4+ CLI whose root command lives in `cmd/snowctl` and whose shared packages reside under `pkg/`. It wraps the daily workflow of Snowflake operators so scripts, CI jobs, and humans can share the same tooling.

**Key capabilities**

- Connection lifecycle management via `connection set|list|use|set-default|remove|test`, each persisting metadata under `~/.snowctl/config`.
- SQL execution using `snowctl sql --query` with structured output; global `--output` switches between JSON (default), YAML, CSV, and TSV for shell pipelines.
- Runtime overrides such as `--connection` for one-off context switches and `connection test --set-current` for validating credentials while rotating sessions.
- Shell extras including `snowctl completion <shell>`, `make completions`, and `snowctl version --output short|json` so the binary fits neatly alongside kubectl- or docker-style CLIs.

**Usage highlights**

- Build and install locally with `go build -o snowctl ./cmd/snowctl` or `go install ./cmd/snowctl`, then run `snowctl connection set MyConnection` to hydrate the first profile using existing `SNOWFLAKE_*` env vars as defaults.
- Every connection stores its own password or PAT (no runtime env lookups), enabling non-interactive automation through `--secret` and `--no-prompt`.
- SQL invocations emit metadata (`connection`, `statement`) before row sets, making it trivial to parse JSON or stream CSV/TSV rows straight into other CLIs.

**Configuration, security & development**

- Config lives at `${HOME}/.snowctl/config` (TOML with `currentContext`, `defaultContext`, and one `[contexts.<name>]` block per connection). The file is created with `0600` permissions so the stored secrets remain local.
- Tests run with `go test ./...`, covering configuration migrations, context enforcement, connection workflows, SQL formatting, and Snowflake mocking.
- Formatting relies on `gofmt` while release builds inject `Version`, `Commit`, and `Date` via `-ldflags` (see the example command in the repo README).

## [Snowflake.SPCS.Lab](https://github.com/marcelinojackson-org/Snowflake.SPCS.Lab)

[Snowflake.SPCS.Lab](https://github.com/marcelinojackson-org/Snowflake.SPCS.Lab) currently ships the `spcs-etl-job/` sample, a containerized ETL workload for Snowpark Container Services (SPCS). It demonstrates how to package a Python loader, publish it via Snow CLI, and execute it on a compute pool.

**What’s inside**

- `app/etl.py` – reads staged CSV files via `snowflake.connector`, authenticates with the OAuth session token at `/snowflake/session/token`, creates a temp staging table (`ORDERS_STG`), `COPY INTO`s from `@RAW_STAGE` (configurable), and inserts into a target table before committing.
- `data/orders_01.csv` – seed data you can upload to a stage while testing the flow end to end.
- `Dockerfile` – bundles the Python app alongside its dependencies so `snow spcs image push` can version the container.
- `job_spec.yaml` – declares the runtime container (`etl-main`), registry path, and environment variables (`SNOWFLAKE_ACCOUNT`, `SNOWFLAKE_HOST`, `SNOWFLAKE_DATABASE`, `SNOWFLAKE_SCHEMA`, `SNOWFLAKE_WAREHOUSE`, `INPUT_STAGE`, `TARGET_TABLE`) consumed by the script.

Use Snow CLI to stage the CSV sample, build/push the container, and create or run the job spec against your compute pool; the README inside `spcs-etl-job/` documents the scope and Snow CLI-driven workflow. The pattern leaves room for additional labs inside this repo as new SPCS experiments grow past prototype stage.
