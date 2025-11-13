# Marcelino’s OSS Public Portfolio

This workspace curates Marcelino’s published OSS projects, with Azure and Snowflake tracks today and room for additional stacks as they go public.

Current highlights:

- **Azure** – a complete AKS GitOps reference implementation that spans Terraform, Helm, Argo CD, Ansible, Prometheus/Grafana, and k6.
- **Snowflake** – a family of GitHub Actions, helper libraries, testing harnesses, and internal apps that showcase Cortex AI integrations plus day‑to‑day operational tooling.

This README is the top-level atlas. Each repository underneath ships with its own README for installation or usage details.

## Portfolio map

### Azure

| Path | Focus | Highlights / Notes |
| --- | --- | --- |
| Azure.AKS.Gitops.Lab | Azure Kubernetes Service GitOps lab | Terraform-based cluster bring-up, Helm workloads, Argo CD continuous sync, Ansible automation, observability stack, CLI playbooks, teardown tooling. |

### Snowflake

| Path | Focus | Highlights / Notes |
| --- | --- | --- |
| Snowflake.FrostyStatus | Streamlit dashboard | Snowsight-inspired status board for warehouses, tasks, and jobs with keyboard-friendly exploration. |
| Snowflake.IAC | Future infrastructure | Empty placeholder for eventual Snowflake IaC assets. |

#### Snowflake GitHub Actions

| Path | Focus | Highlights / Notes |
| --- | --- | --- |
| Snowflake.Common | Shared TypeScript library | Centralizes `SNOWFLAKE_*` validation, logging controls, and helper APIs (`getSnowflakeConnection`, `runSql`) consumed by every action. |
| Snowflake.Testing | Validation scripts | Cross-repo build/test harnesses that rebuild shared libraries, package actions, and run local Cortex smoke tests. |
| Snowflake.RunSQLAction | GitHub Action | Executes SQL end-to-end, applies safe limits, emits CSV/metadata artifacts for large result sets, and leans on the shared library for connectivity. |
| Snowflake.CortexAI.AgentAction | GitHub Action | Bridges GitHub Actions with Cortex Agents, streaming every event plus a final summary for downstream workflow steps. |
| Snowflake.CortexAI.AnalystAction | GitHub Action | Connects to Cortex Analyst semantic models/views, exposes optional SQL echoing, and returns structured responses for analytics automation. |
| Snowflake.CortexAI.SearchAction | GitHub Action | Wraps the Cortex Search REST API with filters, pagination, rerankers, and scoring controls. |
| Snowflake.AISQLAction | GitHub Action (WIP) | Reserved space for upcoming AISQL automation; currently only scaffolding is checked in. |

## Azure.AKS.Gitops.Lab

This lab is designed for repeatable cluster builds, controlled experiments, and demos:

- **Provisioning workflow** – Terraform modules carve out the resource group, networking, and AKS cluster. Targeted apply sequences are documented (and scripted) so recreating infra is deterministic.
- **Application layers** – Helm charts deploy nginx, a Flask sample app, Prometheus, and Grafana. Argo CD watches the repo for drift and reconciles the Helm releases automatically.
- **Automation & Runbooks** – Makefile targets, `cli-steps.txt`, and Ansible playbooks encode the exact bootstrap steps, secret hydration, and post-deploy scale adjustments.
- **Observability & Testing** – Prometheus and Grafana arrive pre-wired with datasources/dashboards; k6 scripts deliver programmable load; docs walk through port-forwarding and CI triggers.
- **Operations tooling** – Python scripts under `scripts/` summarize Azure inventory and cost, while `decommission.sh` handles graceful teardown and local cleanup.

See `Azure.AKS.Gitops.Lab/docs/README.md` for diagrams, command references, and troubleshooting guides.

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
