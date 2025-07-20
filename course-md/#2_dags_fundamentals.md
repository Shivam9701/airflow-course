# 📘 Apache Airflow Course - Module 2

## 📂 Module Overview: Exploring Different Types of DAGs

This module explores various DAG patterns, each demonstrating unique features of Airflow. We'll go through each DAG script that you've implemented, explaining its purpose, structure, scheduling, and execution logic in detail. Additionally, we'll include helpful code snippets and real-world use cases to deepen your understanding.

---

## 📄 1. `my_first_proper_dag.py`

### ✅ Purpose:

This is your first working DAG. It helps validate that your Airflow installation is functioning correctly and that DAGs are being picked up by the scheduler.

### ⚙️ Features:

* Basic Python DAG structure
* Uses the `@dag` decorator and `PythonOperator`

### 🧠 Key Concepts:

* Importing the required modules: `from airflow import DAG`
* Minimum required arguments for a DAG: `dag_id`, `start_date`, `schedule`, `catchup`
* Use of the `@task` decorator or `PythonOperator` for defining tasks

### 🔧 Code Snippet:

```python
from airflow.decorators import dag, task
from datetime import datetime

@dag(dag_id="my_first_proper_dag", start_date=datetime(2024, 1, 1), schedule="@daily", catchup=False)
def my_first_dag():
    @task
    def say_hello():
        print("Hello, Airflow!")

    say_hello()

my_first_dag()
```

---

## 🔗 2. `linear_tasks.py`

### ✅ Purpose:

Demonstrates a simple linear flow between multiple tasks, where each task depends on the successful completion of the previous one.

### ⚙️ Features:

* Task 1 → Task 2 → Task 3 (executed sequentially)
* Explicit task dependencies using `>>` or `<<`

### 🧠 Key Concepts:

* Linear dependency chains
* Task functions should return or log useful information for better observability

### 🔧 Code Snippet:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def task_1():
    print("Task 1 executed")

def task_2():
    print("Task 2 executed")

def task_3():
    print("Task 3 executed")

with DAG(
    dag_id="linear_tasks",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    t1 = PythonOperator(task_id="task_1", python_callable=task_1)
    t2 = PythonOperator(task_id="task_2", python_callable=task_2)
    t3 = PythonOperator(task_id="task_3", python_callable=task_3)

    t1 >> t2 >> t3
```

---

## ⏱️ 3. `schedule_5_mins.py`

### ✅ Purpose:

Illustrates how to set up a DAG that runs every 5 minutes using cron-based scheduling.

### ⚙️ Features:

* `schedule="*/5 * * * *"` (cron-based scheduling)
* Minimal tasks to observe scheduled triggers

### 🧠 Key Concepts:

* Cron scheduling in Airflow 3.0 using `schedule` instead of `schedule_interval`
* Use of `start_date` in the past to allow immediate triggering

### 🔧 Code Snippet:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_message():
    print("This DAG runs every 5 minutes!")

with DAG(
    dag_id="schedule_5_mins",
    start_date=datetime(2024, 1, 1),
    schedule="*/5 * * * *",
    catchup=False,
) as dag:
    task = PythonOperator(task_id="print_message", python_callable=print_message)
```

---

## 🌿 4. `branch_dag.py`

### ✅ Purpose:

Demonstrates conditional branching of DAG execution using `BranchPythonOperator`.

### ⚙️ Features:

* One task decides which path to follow at runtime
* Followed by conditional downstream tasks

### 🧠 Key Concepts:

* `BranchPythonOperator` returns the `task_id` of the task to execute
* All downstream tasks must be listed to ensure correct dependency resolution
* Skipped tasks don’t run (status = skipped)

### 🔧 Code Snippet:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime

def decide_branch():
    return "task_a" if datetime.now().minute % 2 == 0 else "task_b"

def task_a():
    print("Task A executed")

def task_b():
    print("Task B executed")

with DAG(
    dag_id="branch_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    branch = BranchPythonOperator(task_id="branch_task", python_callable=decide_branch)
    task_a = PythonOperator(task_id="task_a", python_callable=task_a)
    task_b = PythonOperator(task_id="task_b", python_callable=task_b)

    branch >> [task_a, task_b]
```

---

## 🔁 5. `basic_retry_dag.py`

### ✅ Purpose:

Showcases automatic retry on task failure.

### ⚙️ Features:

* PythonOperator simulating a failure
* DAG-level and task-level retry configurations

### 🧠 Key Concepts:

* `retries`, `retry_delay`, `max_active_runs`
* Useful for handling transient issues (e.g., network failures)

### 🔧 Code Snippet:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def fail_task():
    raise Exception("Simulated failure")

with DAG(
    dag_id="basic_retry_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={"retries": 3, "retry_delay": timedelta(minutes=5)},
) as dag:
    task = PythonOperator(task_id="fail_task", python_callable=fail_task)
```

---

## 🧪 6. `parameterized_dag.py`

### ✅ Purpose:

Illustrates how to make a DAG dynamic using parameters.

### ⚙️ Features:

* Uses `params={}` to pass values at runtime
* Uses `dag_run.conf.get()` to retrieve these values in task functions

### 🧠 Key Concepts:

* Dynamic configuration at trigger time
* Enables creation of more generic DAGs reusable across inputs (e.g., client-specific processing)

### 🔧 Code Snippet:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

with DAG(
    dag_id="parameterized_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    greet_task = PythonOperator(
        task_id="greet_person",
        python_callable=greet,
        op_kwargs={"name": "{{ dag_run.conf.get('name', 'Guest') }}", "age": "{{ dag_run.conf.get('age', 0) }}"},
    )
```

---

## ✅ Summary Table

| DAG Name            | Key Feature                   | Operator Type        |
| ------------------- | ----------------------------- | -------------------- |
| `my_first_proper_dag` | Basic DAG Structure           | PythonOperator       |
| `linear_tasks`      | Sequential Dependency Flow    | PythonOperator       |
| `schedule_5_mins`   | Cron-based scheduling         | PythonOperator       |
| `branch_dag`        | Conditional Path Execution    | BranchPythonOperator |
| `basic_retry_dag`   | Retry on Failure              | PythonOperator       |
| `parameterized_dag` | Parameterized Manual Triggers | PythonOperator       |

---

## 🧭 Next Module Preview: Operators & Hooks Deep Dive

In the next module, we will explore different Airflow operators (e.g., BashOperator, EmailOperator, PythonOperator), understand hooks and their role in connecting external systems, and learn how to design robust tasks using these building blocks.