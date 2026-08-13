from datetime import date

from pydantic import HttpUrl

from cv.models import Company, Position

# Description prose synthesized from local Cogram repos and Cadu's merged PRs.
# Internal product / project / tool names are intentionally generalized.
# `cadurso` is kept by name because it's Cadu's own public OSS library.

COGRAM = Company(
    name="Cogram",
    one_liner="LLM-powered platform for the AECO industry",
    url=HttpUrl("https://www.cogram.com"),
    positions=(
        Position(
            title="Staff Software Engineer",
            start=date(2026, 2, 1),
            end=None,
            location="Berlin, Germany",
            remote=True,
            description="""
Owning initiatives end-to-end across infra, backend, and customer engagements.

- **Drove a production performance and reliability program.** Diagnosed a multi-week prod memory leak (botocore S3 client leak in a high-traffic webhook) and shipped the combined fix across OTLP transport, the memory allocator, and worker recycling. Replaced a 1 req/s polling loop with SSE backed by per-worker Redis pubsub. Cut the batch-PDF upload pipeline from 12 min to 2 min and the CI/CD deploy pipeline from 13:20 to 10:00 wall clock.

- **Authored the ADR and shipped the backend for the custom-fields system for inspection-style records.** Owned the backend (FastAPI routes, SQLAlchemy models, Alembic migration with custom-field-group tables, authz policies) and the infra rollout, with smaller touch-ups on the frontend admin and report-detail UI; landed in time for the live customer onboarding release.

- **Replaced Meilisearch with Postgres full-text search across the entire stack.** Removed the service end-to-end (sync layer, eventual-consistency bugs, no native multi-tenancy) in favour of Postgres FTS with row-level-security tenant isolation, dropping a full service from production.

- **Acted as the team's senior reviewer and engineering-process driver.** Carried the senior-reviewer load on peer PRs at significant volume. Co-shaped a code-review-process redesign with a peer before bringing it to the wider team. Carved a dedicated learning track to coach a teammate on Claude-Code-driven issue grooming and Linear-as-shared-brain workflows; recurring "thought-partner" calls from peers across hiring, infra, and customer-scope decisions.

Ongoing scope: the production K3s platform, the self-hosted observability stack, the company's internal AI-developer-tooling track, and team-wide Claude Code skills (K3s deploys, Grafana operations, data-warehouse access, Sentry triage).""",
        ),
        Position(
            title="Senior Software Engineer",
            start=date(2023, 8, 1),
            end=date(2026, 2, 1),
            location="Berlin, Germany",
            remote=True,
            description="""
                Software engineer with a strong backend focus across the company's three core services. Also takes on substantial infrastructure / platform-engineering work and authors a large share of the company's AI tooling. Day-to-day impact:

                - **Migrated the company from ECS to Kubernetes (K3s).** Drove the full platform arc end-to-end: AWS ECS/Fargate → docker-compose on Azure VM → single-VM K3s clusters in dev, staging, and prod. Authored the Helm charts, hostPort networking, Tailscale + socat proxies for RDS, GitHub Actions deploy pipelines, and RBAC for shared read-only observability. Sunset thousands of lines of dead ECS infra after migration.
                - **Created the company's speech-to-text service from scratch.** FastAPI + SQLAlchemy + Alembic backend, pluggable transcriber interface (Whisper, self-hosted Deepgram, NVIDIA Parakeet), job-queue worker, GPU/system telemetry, and the full Terraform / Ansible / GitHub Actions pipeline. Operated through three deployment generations (AWS EC2, AWS RDS-backed multi-region, Azure VM production) while keeping a Deepgram-compatible public API stable.
                - **Drove backend hiring and onboarding.** Interviewed dozens of candidates, and acted as the dedicated onboarding mentor ("big brother") for 4+ new engineers across the backend and platform-engineering tracks. Mentored team members on FastAPI service design, K3s operations, and the LLM agent stack.
                - **Owned the search platform.** Redesigned Meilisearch synchronization three times: ad-hoc → SQLAlchemy hooks → buffered bucket sync → final PostgreSQL-trigger + outbox pattern that survives direct DB writes. Centralized Meilisearch on a dedicated VM with AWS PrivateLink to every environment.
                - **Built the LLM agent stack** powering the product's AI assistant. PydanticAI, LangGraph, langchain-anthropic, langchain-openai, and the OpenAI / Anthropic SDKs, with durable threads, SSE streaming, and agentic tool development.
                - **Stood up the company's self-hosted observability stack** on Loki, Tempo, Mimir, Alloy, and fluent-bit, with shared read-only K3s access via RBAC. Tuned OpenTelemetry sampling and OTLP transports; added FastAPI span-status middleware.
                - **Authored the internal CLI used by every engineer** for environment, secrets, K3s, and observability operations.
                - **Wired in *cadurso* (open-source authorization library I authored) as the company's policy backbone.** Refactored permissions across the core domain (reports, observations, emails, and tutorial surfaces); added asset-visibility tiers and JWT/Meilisearch decoupling to prevent total auth outages.

                Other multi-quarter projects: an agentic RFP-drafting product and a custom-report export pipeline with an in-house HTML-to-DOCX templating library.
            """,
            keywords=(
                "Python 3.14",
                "Rust",
                "TypeScript",
                "FastAPI",
                "uvicorn",
                "Pydantic v2",
                "SQLAlchemy 2.x",
                "Alembic",
                "PostgreSQL",
                "Redis",
                "Meilisearch",
                "PydanticAI",
                "LangGraph",
                "OpenAI/Anthropic SDKs",
                "OpenTelemetry",
                "Grafana (Loki / Tempo / Mimir / Alloy)",
                "Terraform",
                "Ansible",
                "K3s",
                "Helm",
                "Docker",
                "AWS",
                "Azure",
                "GitHub Actions",
                "Tailscale",
            ),
        ),
    ),
)
