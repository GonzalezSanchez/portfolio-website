"""Project cards for the homepage — rendered by the loop in templates/index.html.

Card fields:
    label        "Project 1a" chip above the title
    title        card title
    subtitle     optional grey suffix next to the title
    description  plain text, no HTML
    tags         stack chips, in display order
    image        optional {"src": "/static/img/...", "alt": "..."} shown below the tags
    live         True → "Live →" link to the platform dashboard in the card footer
    linkedin     optional URL → "LinkedIn post →" link in the card footer
    note         optional grey footer note (e.g. deployment model)
"""

PROJECTS = [
    {
        "label": "Project 1a",
        "title": "Serverless Ingestion",
        "description": (
            "Serverless REST API for real-time sensor event ingestion with threshold-based "
            "anomaly detection. Clean layered architecture (models → services → repositories). "
            "Full infrastructure as code with CloudFormation. Deployed to AWS via CI/CD."
        ),
        "tags": ["Python", "AWS Lambda", "API Gateway", "DynamoDB", "CloudFormation"],
    },
    {
        "label": "Project 1b",
        "title": "Containerised Ingestion",
        "description": (
            "Same domain logic as 1a, redeployed as a containerised FastAPI app. End-to-end "
            "observability with OpenTelemetry auto-instrumentation → OTel Collector → Datadog APM: "
            "distributed traces with automatic DynamoDB child span detection, log-trace correlation, "
            "and Watchdog anomaly detection — zero manual instrumentation."
        ),
        "tags": ["Python", "FastAPI", "Docker", "nginx", "React", "OpenTelemetry", "Datadog"],
        "image": {
            "src": "/static/img/datadog-flame-graph.png",
            "alt": "Datadog APM — POST /events flame graph with automatic DynamoDB child span detection",
        },
        "live": True,
        "linkedin": "https://www.linkedin.com/posts/activity-7455558039853645824-reu9",
    },
    {
        "label": "Project 2a",
        "title": "Behavior Analyzer",
        "subtitle": "AWS Serverless",
        "description": (
            "Serverless ETL pipeline: extracts historical sensor data from DynamoDB, detects "
            "occupancy schedules, temperature trends and anomalies, stores results in Aurora "
            "Serverless v2 (PostgreSQL). Full Terraform infrastructure. Runs on-demand to minimise costs."
        ),
        "tags": ["Python", "Step Functions", "Aurora Serverless", "Terraform", "EventBridge"],
        "image": {
            "src": "/static/img/step-functions-project2a.png",
            "alt": "Step Functions execution graph — Extract → Transform → Analyze",
        },
        "note": "On-demand · AWS",
        "linkedin": "https://www.linkedin.com/posts/activity-7450582273697026049-aOCE",
    },
    {
        "label": "Project 2b",
        "title": "Behavior Analyzer",
        "subtitle": "Data Engineering",
        "description": (
            "Same analytics goal as 2a, re-implemented with a data engineering stack. Medallion "
            "architecture (Bronze → Silver → Gold): raw Parquet → processed Parquet → PostgreSQL via "
            "dbt. PySpark analytics: occupancy schedules, temperature trend regression (regr_slope), "
            "z-score anomaly detection, spatial hotspots (GeoPandas). Observability via OTel → "
            "Grafana Cloud. Power BI dashboard live in the frontend. Deployed via a 9-stage Jenkins "
            "CD pipeline."
        ),
        "tags": ["Python", "Apache Airflow", "PySpark", "dbt", "AWS S3", "GeoPandas", "Power BI", "Grafana Cloud", "Jenkins"],
        "live": True,
        "linkedin": "https://www.linkedin.com/posts/activity-7460192379891855360-47j7",
    },
    {
        "label": "Project 2c",
        "title": "Behavior Analyzer",
        "subtitle": "Azure Databricks Lakehouse",
        "description": (
            "Same analytics domain as 2b, rebuilt on a fully managed Azure stack. Bronze ingestion "
            "via Auto Loader, Silver transformation with the Write-Audit-Publish pattern (good "
            "records MERGEd idempotent, invalid records to quarantine — never deleted), Gold layer "
            "with dbt-databricks incremental models: z-score anomaly detection, hourly aggregations, "
            "dimensional models. Full IaC via Terraform. Monthly job on the 1st at 06:00 Brussels "
            "time via Databricks Asset Bundles. Gold data served live via FastAPI /lakehouse/* endpoints."
        ),
        "tags": ["Python", "Azure Databricks", "Delta Lake", "Unity Catalog", "dbt", "ADLS Gen2", "Terraform", "DABs"],
        "live": True,
    },
    {
        "label": "Project 4",
        "title": "AI Assistant",
        "subtitle": "Claude + MCP",
        "description": (
            "Conversational AI layer over the live platform: Claude answers questions about the real "
            "sensor data by calling the platform's own REST APIs, exposed as 7 read-only MCP tools. "
            "Bounded agent loop on the streaming Claude API, answers streamed token-by-token via SSE "
            "into a chat tab. Security by design: least-privilege container, read-only tool "
            "allowlist, per-IP rate limiting."
        ),
        "tags": ["Python", "Claude API", "MCP", "FastAPI", "SSE", "Docker", "React"],
        "image": {
            "src": "/static/img/project4-ai-chat.png",
            "alt": "AI Assistant chat — Claude answers from the live data via the get_rooms MCP tool",
        },
        "live": True,
    },
]
