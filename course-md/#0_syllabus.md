# 🧠 Apache Airflow Complete Learning Path (Beginner to Advanced) – Updated for Airflow 3.x

---

## 📌 Phase 0: Prerequisites

> **Goal:** Set up the right environment & tools to begin learning Airflow.

### ✅ System Requirements

* Windows 10/11 with WSL2 enabled
* Ubuntu installed via WSL
* Python 3.8–3.11 (via pyenv or system)
* VS Code (Python + Docker Extensions)
* Docker Desktop (optional)
* Git installed

### ✅ Python Basics

* `venv`, `pip`, `requirements.txt`
* Modules, imports, Python functions
* Shell scripting (basic Bash)

---

## 🗺️ Phase 1: Beginner – Local Apache Airflow (WSL - No Docker)

> **Goal:** Understand core Airflow concepts & workflow with local Python environment

### 📘 Section 1: Core Concepts

* What is orchestration & Apache Airflow?
* Scheduler, Webserver, Workers, Metadata DB
* DAGs, Operators, Tasks, TaskInstances

### 📘 Section 2: Installation (Airflow 3.x)

* Setup Python `venv`, install Airflow via `pip`
* Initialize DB: `airflow db migrate`
* Start Webserver & Scheduler
* Configure `airflow.cfg`, `dags_folder`, etc.

### 📘 Section 3: Airflow UI Walkthrough

* DAGs tab, Graph view, Tree view
* Task Instance logs & retry handling
* Toggle, trigger, clear DAGs

### 📘 Section 4: Airflow CLI Usage

* `airflow dags list`, `tasks test`, `db reset`
* Logs, task states, CLI debugging tools

---

## 🗺️ Phase 2: Building Foundational DAGs

### 📊 Section 5: Writing Basic DAGs

* Use `PythonOperator`, `BashOperator`, `EmptyOperator`
* DAG args: `dag_id`, `schedule`, `start_date`, `tags`, `catchup`
* Retry, depends\_on\_past, templates

### 🔹 DAGs Covered:

1. `first_dag`
2. `linear_tasks`
3. `schedule_5_mins`
4. `branch_dag` (BranchPythonOperator)
5. `basic_retry_dag`
6. `parameterized_dag`
7. `fan_out_fan_in_dag`

---

## 🕹️ Phase 3: Operators Mastery

> In-depth learning of Airflow’s standard and advanced operators

### 📘 Section 6: Operators Deep-Dive

* `PythonOperator` (done)
* `BashOperator` (done)
* `EmptyOperator` (done)
* `BranchPythonOperator` (done)
* `ShortCircuitOperator`
* `HttpOperator`
* `TriggerDagRunOperator`
* `EmailOperator` (skipped)
* `DockerOperator`
* `TaskGroup` & Dynamic Task Mapping
* `SubDagOperator` (deprecated but explored)

---

## 📖 Phase 4: Intermediate – Templates, Context, XCom

### 📘 Section 7: Jinja Templates

* `{{ ds }}`, `{{ execution_date }}`
* Using templates in BashOperator, filenames, logging

### 📘 Section 8: Task Context & Logging

* `context` parameter, `ti`, `run_id`, etc.
* View rendered template fields in UI

### 📘 Section 9: XCom

* Push/pull values across tasks
* Use cases: task coordination, configuration

---

## 📅 Phase 5: Advanced Scheduling & Error Handling

### 📘 Section 10: Scheduling

* Using `schedule="@hourly"`, `@daily`, cron syntax
* `catchup`, `max_active_runs`, `depends_on_past`

### 📘 Section 11: Error Handling

* Retry logic
* `on_failure_callback`, `on_success_callback`
* Email/Slack alert integration

---

## 💼 Phase 6: Real Projects (Hands-On)

### ✅ Project 1: Local CSV Ingestion Pipeline

* Use `PythonOperator`
* Extract from CSV URL
* Transform with Pandas
* Load to SQLite/PostgreSQL

### ✅ Project 2: API Data Pipeline

* Pull weather/crypto API using `HttpOperator` or Python
* Store in SQLite or Postgres
* Hourly schedule

### ✅ Project 3: S3 > Athena Reporting

* Use `S3Hook`, `AthenaHook`
* Query logs/data and email result
* Partition management

### 🔄 Project 4: Fan-Out & Fan-In Pattern

* Use `EmptyOperator`, task chaining
* Conditional downstream

### 📈 Project 5: Parametrized DAG Factory

* Use `params` to generate dynamic task paths
* Daily email of status

---

## 🎓 Phase 7: Production Patterns

### 📘 Section 12: Dynamic DAGs

* Loop-based task creation
* Task Mapping from datasets

### 📘 Section 13: Sensors

* `FileSensor`, `ExternalTaskSensor`, `S3KeySensor`
* `poke_interval`, `mode`, `timeout`

### 📘 Section 14: Task Groups & SubDAGs

* Use case: multi-stage pipelines
* Grouping related logic blocks

---

## 🚀 Phase 8: Deployment & Monitoring

### 📘 Section 15: Logging & Monitoring

* Task logs
* DAG stats, alerting
* Monitoring DAG runtimes

### 📘 Section 16: Git Integration

* DAG versioning with Git
* CI/CD (GitHub Actions)
* Folder structure best practices

### 📘 Section 17: Docker / Cloud (Optional)

* Astro CLI, Docker-based setup
* Airflow with Terraform / MWAA (optional)

---

## 🧰 Tools, Libraries, Integrations

* Pandas / Polars
* SQLite, PostgreSQL, MySQL
* S3, Athena, Redshift
* Docker
* dbt models as Airflow tasks

---

## 📚 Resources

* [Airflow Docs](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
* [Astronomer Academy](https://academy.astronomer.io/)
* GitHub: [apache/airflow/tree/main/airflow/example\_dags](https://github.com/apache/airflow/tree/main/airflow/example_dags)
* YouTube: MWAA Examples, Data With Dani
* Reddit / Discord / Slack channels
* Books: "Data Pipelines with Apache Airflow" by Bas P. Harenslak, "Airflow in Action" by Marc Lamberti