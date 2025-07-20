# 📘 Apache Airflow Course - Module 3

## 📂 Module Overview: Operators Deep Dive

This module provides a comprehensive explanation of all the operators used in the DAGs within the `operators` folder. Each operator is explained with its purpose, features, and code snippets to help you understand its usage in real-world scenarios.

---

## 🛠️ 1. `BashOperator`

### ✅ Purpose:

Executes shell commands within a DAG.

### ⚙️ Features:

* Executes a simple bash command
* Useful for running shell scripts or system commands

### 🔧 Code Snippet:

```python
from airflow.providers.standard.operators.bash import BashOperator

bash_task = BashOperator(
    task_id="print_hello", bash_command="echo 'Hello from BashOperator!'"
)
```

---

## 🧪 2. `PythonOperator`

### ✅ Purpose:

Executes Python callables as tasks within a DAG.

### ⚙️ Features:

* Allows execution of Python functions
* Ideal for custom logic and data processing

### 🔧 Code Snippet:

```python
from airflow.providers.standard.operators.python import PythonOperator

def greet():
    print("Hello from PythonOperator!")

python_task = PythonOperator(
    task_id="greet_task", python_callable=greet
)
```

---

## 🌿 3. `BranchPythonOperator`

### ✅ Purpose:

Facilitates conditional branching in DAG execution.

### ⚙️ Features:

* Decides which path to follow at runtime
* Skips tasks not in the selected branch

### 🔧 Code Snippet:

```python
from airflow.providers.standard.operators.python import BranchPythonOperator

def choose_branch():
    return "branch_a" if datetime.now().minute % 2 == 0 else "branch_b"

branch_task = BranchPythonOperator(
    task_id="branch_task", python_callable=choose_branch
)
```

---

## 🔄 4. `EmptyOperator`

### ✅ Purpose:

Acts as a placeholder or marker in a DAG.

### ⚙️ Features:

* Useful for defining start, join, or end points
* Does not perform any action

### 🔧 Code Snippet:

```python
from airflow.providers.standard.operators.empty import EmptyOperator

start = EmptyOperator(task_id="start")
end = EmptyOperator(task_id="end")
```

---

## 🔄 5. `TriggerDagRunOperator`

### ✅ Purpose:

Triggers another DAG from within a DAG.

### ⚙️ Features:

* Can wait for the triggered DAG to complete
* Useful for orchestrating workflows across multiple DAGs

### 🔧 Code Snippet:

```python
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator

trigger_task = TriggerDagRunOperator(
    task_id="trigger_child",
    trigger_dag_id="child_dag_id",
    wait_for_completion=True
)
```

---

## 🔄 6. `ShortCircuitOperator`

### ✅ Purpose:

Skips downstream tasks if a condition is not met.

### ⚙️ Features:

* Evaluates a Python callable
* Skips downstream tasks if the callable returns `False`

### 🔧 Code Snippet:

```python
from airflow.providers.standard.operators.python import ShortCircuitOperator

def condition():
    return True

short_circuit_task = ShortCircuitOperator(
    task_id="check_condition", python_callable=condition
)
```

---

## ✅ Updated Summary Table

| Operator Name            | Key Feature                   | Example DAG          |
| ------------------------ | ----------------------------- | -------------------- |
| `BashOperator`           | Execute Shell Commands        | `bash_operator_example` |
| `PythonOperator`         | Execute Python Functions      | `python_operator_example` |
| `BranchPythonOperator`   | Conditional Path Execution    | `branch_python_operator_example` |
| `EmptyOperator`          | Placeholder Tasks             | `empty_operator_example` |
| `TriggerDagRunOperator`  | Trigger Another DAG           | `trigger_dagrun_example` |
| `ShortCircuitOperator`   | Conditional Task Execution    | `short_circuit_example` |

---

## 🧭 Next Module Preview: Advanced DAG Patterns

In the next module, we will explore advanced DAG patterns, including dynamic DAG generation, task groups, and cross-DAG dependencies.
