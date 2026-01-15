# Marcelino’s OSS Public Portfolio

This workspace curates my published OSS projects across Azure infrastructure, DevSecOps pipelines, Snowflake GitHub Actions, and Snowflake labs/tools—with room for additional stacks as they go public.

Current highlights:

- **Azure** – a complete AKS GitOps reference implementation that spans Terraform, Helm, Argo CD, Ansible, Prometheus/Grafana, and k6.
- **DevSecOps CDC demo** – a local MySQL → Kafka (Debezium) → Postgres pipeline with Docker Compose, Kafka UI visibility, and seed data for validation.
- **Snowflake GitHub Actions** – a family of GitHub Actions, helper libraries, and testing harnesses that showcase Cortex AI integrations plus day‑to‑day operational tooling.
- **Snowflake labs and tooling** – Snowpark Container Services demos (`Snowflake.SPCS.Lab`), the `snow9s` TUI, and a reserved IaC track ready to house future assets.

This README is the top-level atlas. Each repository underneath ships with its own README for installation or usage details.

## Portfolio map

### Azure

| Path | Focus | Highlights / Notes |
| --- | --- | --- |
| [Azure.AKS.GitOps.Lab](https://github.com/marcelinojackson-org/Azure.AKS.GitOps.Lab) | Azure Kubernetes Service GitOps lab | Terraform-based cluster bring-up, Helm workloads, Argo CD continuous sync, Ansible automation, observability stack, CLI playbooks, teardown tooling. |

### DevSecOps

| Path | Focus | Highlights / Notes |
| --- | --- | --- |
| [DevSecOps.CDCDemo](https://github.com/marcelinojackson-org/DevSecOps.CDCDemo) | CDC pipeline demo | MySQL source with Debezium CDC into Kafka, JDBC sink into Postgres, Kafka UI for visibility, seeded datasets for quick validation. |

### Snowflake labs and tooling

| Path | Focus | Highlights / Notes |
| --- | --- | --- |
| [Snowflake.SPCS.Lab](https://github.com/marcelinojackson-org/Snowflake.SPCS.Lab) | Snowpark Container Services lab | Containerized ETL demo (`spcs-etl-job/`) with Python loader, Dockerfile, staged sample CSVs, and a job spec wired for Snow CLI + compute pools. |
| [snow9s](https://github.com/marcelinojackson-org/snow9s) | SPCS terminal dashboard | k9s-style TUI for Snowpark Container Services with fast keyboard nav, live refresh, and config via `SNOWFLAKE_*` env vars or `~/.snow9s/config.yaml`. |
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
| [Snowflake.AISQLAction](https://github.com/marcelinojackson-org/Snowflake.AISQLAction) | GitHub Action | Runs Cortex AISQL functions like `AI_COMPLETE`, `AI_EXTRACT`, `AI_SENTIMENT`, `AI_CLASSIFY`, `AI_COUNT_TOKENS`, `AI_EMBED`, `AI_SIMILARITY`, `AI_SUMMARIZE`, `AI_TRANSLATE`, and `AI_PARSE_DOCUMENT`. |

## [Azure.AKS.GitOps.Lab](https://github.com/marcelinojackson-org/Azure.AKS.GitOps.Lab)

I built this lab for repeatable cluster builds, controlled experiments, and demos:

- **Provisioning workflow** – Terraform modules carve out the resource group, networking, and AKS cluster. Targeted apply sequences are documented (and scripted) so recreating infra is deterministic.
- **Application layers** – Helm charts deploy nginx, a Flask sample app, Prometheus, and Grafana. Argo CD watches the repo for drift and reconciles the Helm releases automatically.
- **Automation & Runbooks** – Makefile targets, `cli-steps.txt`, and Ansible playbooks encode the exact bootstrap steps, secret hydration, and post-deploy scale adjustments.
- **Observability & Testing** – Prometheus and Grafana arrive pre-wired with datasources/dashboards; k6 scripts deliver programmable load; docs walk through port-forwarding and CI triggers.
- **Operations tooling** – Python scripts under `scripts/` summarize Azure inventory and cost, while `decommission.sh` handles graceful teardown and local cleanup.

See `Azure.AKS.GitOps.Lab/README.md`, `Azure.AKS.GitOps.Lab/docs/diagrams/`, and `Azure.AKS.GitOps.Lab/docs/troubleshooting.md` for diagrams, command references, and troubleshooting guides.

## Snowflake GitHub Actions & Tools

The Snowflake side of the workspace is organized around a few themes.

### 1. Shared foundation

- **`Snowflake.Common`** – guards against misconfigured environments, standardizes connection telemetry, and exposes reusable helpers for SQL execution. Actions depend on the published package and bundle it locally for Marketplace releases.

### 2. Cortex AI automation

- **`Snowflake.CortexAI.AgentAction`** – drives Cortex Agents conversations from CI/CD, capturing both the answer text and every streamed event so workflows can branch on intermediate reasoning or tool invocations.
- **`Snowflake.CortexAI.AnalystAction`** – fronts Cortex Analyst semantic models and semantic views, making it easy to wire natural-language analytics questions into CI pipelines or scheduled jobs.
- **`Snowflake.CortexAI.SearchAction`** – exposes Cortex Search with optional filters, pagination, reranking, score thresholds, and field selection for targeted retrieval use cases.
- **`Snowflake.AISQLAction`** – AISQL-first action that executes Cortex AI SQL functions with JSON payloads and returns structured outputs for workflows.

### 3. Core SQL execution

- **`Snowflake.RunSQLAction`** – the baseline action for running SQL inside GitHub workflows. It enforces sensible `LIMIT`s, supports artifact persistence (CSV + metadata), and prints compact run summaries for small queries.

### 4. Operational dashboards & validation tooling

- **`Snowflake.Testing`** – bash-based harnesses that rebuild `Snowflake.Common`, package each action locally, and execute representative smoke tests (RunSQL, Cortex Search, Cortex Analyst, Cortex Agent) against a developer’s Snowflake account to catch regressions before publishing.

### 5. Future expansion

- **`Snowflake.IAC`** – intentionally blank for now so new infrastructure-as-code modules can land without reworking repo layout later.

Each sub-repo’s README dives into installation steps, environment requirements, inputs/outputs, and examples. This overview keeps the spotlight on how the pieces fit together across Azure and Snowflake without duplicating usage content.

## [Snowflake.SPCS.Lab](https://github.com/marcelinojackson-org/Snowflake.SPCS.Lab)

This repo currently ships the `spcs-etl-job/` sample, a containerized ETL workload for Snowpark Container Services (SPCS). It demonstrates how to package a Python loader, publish it via Snow CLI, and execute it on a compute pool.

**What’s inside**

- `app/etl.py` – reads staged CSV files via `snowflake.connector`, authenticates with the OAuth session token at `/snowflake/session/token`, creates a temp staging table (`ORDERS_STG`), `COPY INTO`s from `@RAW_STAGE` (configurable), and inserts into a target table before committing.
- `data/orders_01.csv` – seed data you can upload to a stage while testing the flow end to end.
- `Dockerfile` – bundles the Python app alongside its dependencies so `snow spcs image push` can version the container.
- `job_spec.yaml` – declares the runtime container (`etl-main`), registry path, and environment variables (`SNOWFLAKE_ACCOUNT`, `SNOWFLAKE_HOST`, `SNOWFLAKE_DATABASE`, `SNOWFLAKE_SCHEMA`, `SNOWFLAKE_WAREHOUSE`, `INPUT_STAGE`, `TARGET_TABLE`) consumed by the script.

Use Snow CLI to stage the CSV sample, build/push the container, and create or run the job spec against your compute pool; the README inside `spcs-etl-job/` documents the scope and Snow CLI-driven workflow. The pattern leaves room for additional labs inside this repo as new SPCS experiments grow past prototype stage.

## [snow9s](https://github.com/marcelinojackson-org/snow9s)

[snow9s](https://github.com/marcelinojackson-org/snow9s) is a k9s-style terminal UI focused on Snowpark Container Services. It refreshes service listings every few seconds, exposes `snow9s list services` for a non-TUI path, and keeps navigation keyboard-first (`j/k`, `/`, `Ctrl+r`, `?` for help).

- **Configuration** – Reads `SNOWFLAKE_*` env vars or `~/.snow9s/config.yaml` contexts; writes `~/.snow9s/env` on first run so you can fill in values without exporting globally.
- **Focus areas** – Surfaces services, compute pools, status, and resource age with contextual headers and a debug pane that shows executed Snowflake queries.
- **Build/test** – `make build` (drops `./bin/snow9s`) and `make test` (`go test ./...`) cover local validation; Go 1.22+ required.
