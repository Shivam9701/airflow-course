# 🚀 Module 1: Basic Apache Airflow (Windows + WSL, no Docker)

## ✅ Objectives

* Install Apache Airflow using `pip` inside a Python `venv`
* Understand Airflow's directory structure and metadata database
* Learn the purpose of Airflow's core components (webserver, scheduler)
* Use the Airflow CLI to manage and interact with your environment
* Explore the Airflow UI in detail
* Write, trigger, and monitor your first DAG (Directed Acyclic Graph)
* Understand DAG objects and PythonOperator deeply
* Use Branching with examples to control flow of tasks conditionally

---

## 📦 Step 1: Install Airflow (WSL + venv + pip)

Ensure your virtual environment is activated (from Module 0):

```bash
cd ~/airflow-course
source .airflow-venv/bin/activate
```

> This isolates all Airflow dependencies from your system Python.

### 🛠️ Installing Apache Airflow v3.0.2

Apache Airflow has many dependencies and must be installed with a constraint file.

Install the latest stable version (3.0.2) with Celery extras:

```bash
pip install "apache-airflow[celery]==3.0.2" \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.2/constraints-3.9.txt"
```

Explanation:

* `apache-airflow[celery]`: Installs the core Airflow plus optional Celery executor dependencies (not required now, but useful later).
* Constraint URL: Ensures compatible versions for all packages.

> ⚠️ Without constraints, Airflow will likely fail to install correctly.

---

## 📂 Step 2: Initialize Airflow Home Directory

Airflow requires a working directory defined by the `AIRFLOW_HOME` environment variable. By default, it uses `~/airflow`, but it's good practice to set it explicitly.

```bash
export AIRFLOW_HOME=~/airflow
```

Then, initialize the metadata database:

```bash
airflow db migrate
```

This command:

* Creates the `airflow.cfg` configuration file
* Creates `logs/` and initializes `airflow.db`
* Sets up all necessary metadata tables

> `airflow db init` was deprecated in Airflow 3.x. Use `airflow db migrate` going forward.

If example DAGs cause import errors due to test-related modules:

```bash
export AIRFLOW__CORE__LOAD_EXAMPLES=False
airflow db clean --drop-archived
```

---

## 🔐 Step 3: UI Access (Airflow v3 Changes)

As of Airflow 3.x:

* The `airflow users create` command has been **removed**.
* Authentication is **disabled by default** in development setups.
* You can open the Airflow UI directly without login.

Simply start the webserver and access the UI at `http://localhost:8080`.

---

## 🌐 Step 4: Start Webserver & Scheduler

Open two separate terminal windows:

**Terminal 1: Start Webserver**

```bash
airflow webserver --port 8080
```

**Terminal 2: Start Scheduler**

```bash
airflow scheduler
```

Now open [http://localhost:8080](http://localhost:8080).

> No login required for default setup in Airflow 3.x

**Optional: Run using standalone command**
```bash
airflow standalone
```
This command starts both the webserver and scheduler in one go, but it's not recommended for production. Great for quick testing and local development!

---

## 📁 Step 5: Create First DAG

All DAG files are placed inside the `dags/` folder. Create a new Python file:

```bash
touch ~/airflow-course/dags/hello_world_dag.py
```

Paste:

```python
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from datetime import timedelta

def say_hello():
    print("Hello, Apache Airflow!")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule='@daily',
    start_date=days_ago(1),
    catchup=False
)

hello_task = PythonOperator(
    task_id='say_hello',
    python_callable=say_hello,
    dag=dag
)
```

---

## 🧰 DAG Object Deep Dive

### ✅ **Required Parameters of DAG Object**

* `dag_id`: Unique identifier for your DAG in the Airflow system.
* `start_date`: The logical start date of the DAG. It tells Airflow when to start scheduling the DAG.

### ⚖️ **Other Key Parameters**

* `schedule`: Interval at which DAG should run (can be cron syntax or presets like `@daily`, `@hourly`, etc.)
* `catchup`: If `True`, Airflow runs all missed intervals since `start_date`. If `False`, runs only future schedules.
* `default_args`: Dictionary containing default settings for tasks (retries, owner, etc.)
* `description`: Text displayed in the UI to describe the DAG.
* `tags`: UI grouping and filtering.
* `max_active_runs`: Max concurrent DAG runs allowed.
* `params`: Custom parameters you can use within tasks via `{{ params.<name> }}`

> Every DAG is a Python object that defines how tasks relate to each other and when they execute.

### 🩠 DAG Lifecycle Concepts

* DAGs are **parsed** every few seconds by the scheduler.
* They are not executed like scripts; instead, Airflow loads the Python file and constructs the DAG object.
* Once parsed, the scheduler triggers tasks based on `schedule` and `start_date`.

---

## 🥡 Operator Overview

### ✨ What are Operators?

Operators are templates that define a single task in a DAG. Think of them as wrappers around the actual work.

### 📚 Common Operator Types:

* `PythonOperator`: Executes a Python function
* `BashOperator`: Runs shell/bash commands
* `EmailOperator`: Sends an email
* `EmptyOperator`: Useful for placeholder or branching logic
* `BranchPythonOperator`: Directs execution flow conditionally

### 🔍 PythonOperator Example Deep Dive

```python
PythonOperator(
    task_id='say_hello',
    python_callable=say_hello,
    dag=dag
)
```

* `task_id`: Must be unique within the DAG
* `python_callable`: Python function to execute
* `op_args` / `op_kwargs`: Used to pass args to the function

> The PythonOperator bridges DAG structure with dynamic Python logic.

---

## 🤠 BranchPythonOperator Essentials

Used to make DAGs **conditionally flow down different branches**.

```python
from airflow.operators.branch import BranchPythonOperator

def choose():
    return 'task_a'  # Return task_id or list of task_ids
```

Returned tasks run; all others are skipped unless `trigger_rule` is modified.

### 📚 Example: Coin Toss

```python
def flip():
    import random
    return 'heads' if random.random() > 0.5 else 'tails'

branch = BranchPythonOperator(task_id='flip_coin', python_callable=flip)
```

Use `EmptyOperator` for skipped or placeholder paths:

```python
from airflow.operators.empty import EmptyOperator
```

> Real-world uses include: validation branching, A/B testing, time-based logic, and optional task skipping.

---

## ▶️ Step 6: Trigger + Monitor DAG

* In UI, go to `DAGs` tab
* Toggle **hello\_world\_dag** to "on"
* Click ▶️ Trigger
* Use **Graph View** to see DAG flow
* Click task → View Log to see output

---

## 🔎 CLI Essentials

```bash
airflow dags list              # List all DAGs
airflow dags trigger hello_world_dag   # Manually trigger
airflow tasks list hello_world_dag     # List all tasks
airflow tasks test hello_world_dag say_hello 2024-01-01   # Run single task
```

---

## 📚 Summary Table

| Component          | Description                              | ✅ Done |
| ------------------ | ---------------------------------------- | ------ |
| Airflow Installed  | Via pip + venv + constraints             | ✅      |
| Metadata DB Setup  | With `airflow db migrate`                | ✅      |
| Webserver UI       | Running on port 8080                     | ✅      |
| Scheduler Running  | DAGs evaluated and triggered             | ✅      |
| DAG Created        | PythonOperator DAG created + working     | ✅      |
| CLI Usage          | Used to inspect, trigger, and test tasks | ✅      |
| DAG Internals      | Deep understanding of DAG structure      | ✅      |
| Operator Knowledge | PythonOperator & others explored         | ✅      |
| Branching Logic    | BranchPythonOperator with 5 examples     | ✅      |

> 🎉 You’ve built and launched your first Airflow project in WSL using a pure venv-based install.

---
