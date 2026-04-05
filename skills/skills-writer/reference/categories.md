# Skill Categories

9 categories from Anthropic's cataloging of hundreds of active skills.

## 1. Library & API Reference

Explains how to use a library, CLI, or SDK correctly. Contains reference code snippets and gotchas.

Examples: `billing-lib` (internal edge cases), `frontend-design` (design system).

## 2. Product Verification

Describes how to test or verify agent output. Paired with external tools (Playwright, tmux).

Examples: `signup-flow-driver` (headless browser + state assertions), `checkout-verifier` (Stripe test cards).

## 3. Data Fetching & Analysis

Connects to data stacks and monitoring. Contains credentials, dashboard IDs, query mappings.

Examples: `funnel-query` (event joins + canonical user_id), `grafana` (datasource UIDs + problem → dashboard).

## 4. Business Process & Team Automation

Automates repetitive workflows into one command. Uses log files for memory across executions.

Examples: `standup-post` (multi-source aggregation → formatted output), `weekly-recap` (PRs + tickets + deploys).

## 5. Code Scaffolding & Templates

Generates framework boilerplate. Encapsulates org architecture decisions into templates.

Examples: `new-migration` (template + gotchas), `create-app` (auth + logging + deploy pre-wired).

## 6. Code Quality & Review

Enforces code quality standards. Can be deterministic (scripts) or heuristic (subagent review). Often runs via hooks or CI.

Examples: `adversarial-review` (subagent critique → iterate), `code-style` (enforce styles agent defaults poorly on).

## 7. CI/CD & Deployment

Manages build, test, deploy pipelines. Most compositional category — often references other skills.

Examples: `babysit-pr` (monitor → retry CI → resolve conflicts → auto-merge), `deploy-<service>` (gradual rollout + auto-rollback).

## 8. Runbooks

Takes a symptom and runs multi-tool investigation to produce a structured report. Starts from symptoms, not instructions.

Examples: `oncall-runner` (alert → usual suspects → finding), `log-correlator` (request ID → cross-system logs).

## 9. Infrastructure Operations

Routine maintenance with guardrails. Only category that explicitly involves destructive actions — requires confirmation steps and soak periods.

Examples: `<resource>-orphans` (find → notify → soak → confirm → cleanup), `cost-investigation` (spike analysis).

## Three-Layer Model

| Layer | Categories | Role |
|-------|-----------|------|
| Information (Knowing) | 1, 2, 3 | Understand and verify |
| Creation (Making) | 4, 5, 6 | Build and maintain quality |
| Operations (Running) | 7, 8, 9 | Deploy and maintain |
