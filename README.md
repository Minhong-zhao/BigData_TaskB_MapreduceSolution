# ✈️ MapReduce Passenger Flight Counter (Big Data Task B)

This project implements a simplified **MapReduce framework in Python** to process airline passenger data and determine which passenger(s) have taken the most flights.

It demonstrates both **single-threaded** and **multi-threaded** implementations of the MapReduce paradigm using modular components (mapper, shuffler, reducer).

---

## 📁 Project Structure
BigData_TaskB_MapreduceSolution/
│
├── .venv/ # Python virtual environment (not tracked by Git)
│
├── data/ # Input datasets
│ ├── AComp_Passenger_data_no_error.csv
│ └── AComp_Passenger_data_no_error_2.csv
│
├── main.py # Entry point of the project
├── mapper.py # Map function implementation
├── shuffle.py # Shuffle function implementation
├── reducer.py # Reduce function implementation
├── MultiThread.py # Multi-threaded MapReduce execution
├── SingleThread.py # Single-threaded MapReduce execution
└── .gitignore # Git ignore rules


---

## ⚙️ How to Run

Make sure you're using Python 3.7+ and activate the virtual environment if using one.

## 🧠 Module Description
| Module            | Description                                                 |
| ----------------- | ----------------------------------------------------------- |
| `main.py`         | Optional central runner or for testing purposes.            |
| `mapper.py`       | Defines the mapping logic: (passenger\_id, 1).              |
| `shuffle.py`      | Groups mapped data by passenger ID.                         |
| `reducer.py`      | Aggregates the count of flights per passenger.              |
| `MultiThread.py`  | Orchestrates Map → Shuffle → Reduce using multiple threads. |
| `SingleThread.py` | Sequential execution of Map → Shuffle → Reduce.             |

## 🧪 Example Output
--- Multithreaded processing results ---
Passenger IDs (with the most flights): ['UES9151GS5']
Number of flights: 25
Timing: 0.0020 seconds

--- Singlethreaded processing results ---
Passenger IDs (with the most flights): ['UES9151GS5']
Number of flights: 25
Timing: 0.0010 seconds

--- Acceleration ratio ---
Acceleration ratio (Single-thread time / Multithread time) : 0.50x
