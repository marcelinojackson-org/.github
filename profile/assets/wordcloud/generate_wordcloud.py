#!/usr/bin/env python3
"""Generate the OSS tech wordcloud image (v1)."""
import random
from pathlib import Path

from wordcloud import WordCloud

FREQUENCIES = {
    "GitHub-Actions": 90,
    "DevSecOps": 80,
    "Snyk": 75,
    "SAST": 70,
    "SCA": 60,
    "DAST": 55,
    "Azure": 65,
    "AKS": 55,
    "Kubernetes": 60,
    "Terraform": 60,
    "Helm": 50,
    "Argo-CD": 50,
    "Ansible": 40,
    "Prometheus": 40,
    "Grafana": 40,
    "k6": 30,
    "Kafka": 45,
    "Debezium": 35,
    "Postgres": 35,
    "MySQL": 30,
    "Docker": 45,
    "GitOps": 35,
    "CI/CD": 35,
    "Snowflake": 65,
    "Snowpark": 45,
    "SPCS": 40,
    "Cortex-AI": 50,
    "Cortex-Search": 35,
    "Cortex-Analyst": 35,
    "Cortex-Agent": 35,
    "AISQL": 35,
    "Snow-CLI": 25,
    "IaC": 30,
    "Python": 40,
    "TypeScript": 40,
    "Go": 35,
    "SQL": 45,
    "ASP.NET-Core": 35,
    "C#": 30,
    "SQLite": 25,
    "OWASP": 30,
    "SARIF": 35,
    "Code-Scanning": 35,
    "LLM": 25,
    "Snowflake-Common": 25,
    "RunSQL": 25,
    "Cortex-Actions": 25,
    "Observability": 30,
    "Security": 40,
}

PALETTE = ["#ffffff", "#e6f0ff", "#9ecbff", "#58a6ff", "#1f6feb"]


def _color_func(*_args, **_kwargs):
    return random.choice(PALETTE)


OUTPUT_PATH = Path(__file__).resolve().parent / "oss-tech-wordcloud-v1.png"

wc = WordCloud(
    width=1600,
    height=900,
    background_color="#0b0f14",
    prefer_horizontal=0.9,
    max_words=120,
    relative_scaling=0.4,
    random_state=42,
    color_func=_color_func,
    collocations=False,
)

wc.generate_from_frequencies(FREQUENCIES)
wc.to_file(str(OUTPUT_PATH))
print(f"Wrote {OUTPUT_PATH}")
