# Budget Plotting Microservice

This repository implements a Plotting Microservice that generates bar graphs of income and expenses over a specified date range from a CSV file. The service utilizes ZeroMQ for communication between the client and the server.

---

## Communication Contract

1. **Protocol**: ZeroMQ REQ-REP
2. **Request Format**:
    - The client sends a string message in the format: `BAR <start_date> <end_date>`.
    - The `start_date` and `end_date` are in the format `YYYY-MM-DD`.
3. **Response Format**:
    - The server replies with a string confirming if the graph was successfully generated, or an error message (e.g., file not found, invalid date range).

---

## How to Request / Receive Data

To request a plot, the client must:

1. Connect to the server's endpoint (tcp://localhost:5555, but the port can be changed).
2. Send a message in the format: `BAR <start_date> <end_date>`.

To receive data, the client will get the following response from the server:

- A string message indicating the status of the plot generation (e.g., "Bar graph generated successfully!" or an error message).

Code snippet to request a plot:

```python
import zmq

def request_plot(start_date, end_date):
    # Create a ZeroMQ context
    context = zmq.Context()

    # Create a REQ (Request) socket
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")  # Connect to the server

    # Send the request
    socket.send_string(f"BAR {start_date} {end_date}")

    # Receive the response
    response = socket.recv_string()
    print("Response from server:", response)

if __name__ == "__main__":
    # Simple prompt for date range input
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    
    # Request plot for the given date range
    request_plot(start_date, end_date)

Dependencies / Requirements
---------------------------

### Required Libraries:

1.  **ZeroMQ**:

    -   Used for messaging between the client and the microservice. It enables communication using the REQ-REP pattern.

    Install using:

    Copy code

    `pip install pyzmq`

2.  **Matplotlib**:

    -   Used for plotting the bar graph that visualizes income and expenses.

    Install using:

    Copy code

    `pip install matplotlib`

3.  **CSV (Built-in)**:

    -   The `csv` module is used to read and process the CSV file containing the budget data.
4.  **Datetime (Built-in)**:

    -   The `datetime` module is used to handle and parse the date strings in the CSV file and to perform date range filtering.

### Installing Dependencies:

You can install the required libraries by running the following command in your terminal:

bash

Copy code

`pip install pyzmq matplotlib`

### File Structure:

-   `plot_service.py`: The server that handles the plotting requests and generates graphs.
-   `client.py`: A simple test client that interacts with the `plot_service.py` microservice.
-   `budget.csv`: The CSV file containing the budget data. The CSV file should have the following columns:
    -   `Date` (format: `YYYY-MM-DD`)
    -   `Type` (either `Income` or `Expense`)
    -   `Amount` (numeric value representing the amount of income or expense)

* * * * *

Notes
-----

-   Ensure that the `budget.csv` file exists in the same directory as the `plot_service.py` script.
-   The date format in the CSV file should be `YYYY-MM-DD`.
-   The date range provided by the client must be within the range of available dates in the `budget.csv` file.
-   If the service cannot process the data, it will respond with an error message indicating the issue (e.g., invalid date range or file not found).

* * * * *

How to Run
----------

1.  **Start the Plotting Service**:

    -   In one terminal, run the `plot_service.py` script to start the server.

    bash

    Copy code

    `python plot_service.py`

2.  **Request a Plot**:

    -   In another terminal, run the `client.py` script to send a request for a bar graph of income and expenses within a date range.

    bash

    Copy code

    `python client.py`

3.  **Enter Date Range**:

    -   The client will prompt you to enter the start and end dates in the `YYYY-MM-DD` format.
    -   The server will respond with a message indicating if the bar graph was successfully generated or if there was an issue.

* * * * *

Feel free to customize the date range and other details as needed. Enjoy using the plotting microservice!

vbnet

Copy code

 `This markdown file contains:
- **Communication Contract**: Describes how the client and server communicate.
- **How to Request / Receive Data**: Instructions on how to request a plot from the service.
- **Dependencies / Requirements**: Lists the necessary libraries and how to install them.
- **Notes**: Provides additional information about the microservice's behavior.
- **How to Run**: Step-by-step guide on how to run the service and test client.

This should now be ready to copy into a `README.md` file!`

4o mini

##### You said:

no it doesn't, only the first part is in markdwon

###### ChatGPT said:

ChatGPT

Apologies for the confusion earlier. Here is the full **README.md** in markdown format, ready to be copied and pasted:

markdown

Copy code

`# Budget Plotting Microservice

This repository implements a Plotting Microservice that generates bar graphs of income and expenses over a specified date range from a CSV file. The service utilizes ZeroMQ for communication between the client and the server.

---

## Communication Contract

1. **Protocol**: ZeroMQ REQ-REP
2. **Request Format**:
 - The client sends a string message in the format: `BAR <start_date> <end_date>`.
 - The `start_date` and `end_date` are in the format `YYYY-MM-DD`.
3. **Response Format**:
 - The server replies with a string confirming if the graph was successfully generated, or an error message (e.g., file not found, invalid date range).

---

## How to Request / Receive Data

To request a plot, the client must:

1. Connect to the server's endpoint (tcp://localhost:5555, but the port can be changed).
2. Send a message in the format: `BAR <start_date> <end_date>`.

To receive data, the client will get the following response from the server:

- A string message indicating the status of the plot generation (e.g., "Bar graph generated successfully!" or an error message).

Code snippet to request a plot:

```python
import zmq

def request_plot(start_date, end_date):
    # Create a ZeroMQ context
    context = zmq.Context()

    # Create a REQ (Request) socket
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")  # Connect to the server

    # Send the request
    socket.send_string(f"BAR {start_date} {end_date}")

    # Receive the response
    response = socket.recv_string()
    print("Response from server:", response)

if __name__ == "__main__":
    # Simple prompt for date range input
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Request plot for the given date range
    request_plot(start_date, end_date) `

* * * * *

Dependencies / Requirements
---------------------------

### Required Libraries:

1.  **ZeroMQ**:

    -   Used for messaging between the client and the microservice. It enables communication using the REQ-REP pattern.

    Install using:

    Copy code

    `pip install pyzmq`

2.  **Matplotlib**:

    -   Used for plotting the bar graph that visualizes income and expenses.

    Install using:

    Copy code

    `pip install matplotlib`

3.  **CSV (Built-in)**:

    -   The `csv` module is used to read and process the CSV file containing the budget data.
4.  **Datetime (Built-in)**:

    -   The `datetime` module is used to handle and parse the date strings in the CSV file and to perform date range filtering.

### Installing Dependencies:

You can install the required libraries by running the following command in your terminal:

bash

Copy code

`pip install pyzmq matplotlib`

### File Structure:

-   `plot_service.py`: The server that handles the plotting requests and generates graphs.
-   `client.py`: A simple test client that interacts with the `plot_service.py` microservice.
-   `budget.csv`: The CSV file containing the budget data. The CSV file should have the following columns:
    -   `Date` (format: `YYYY-MM-DD`)
    -   `Type` (either `Income` or `Expense`)
    -   `Amount` (numeric value representing the amount of income or expense)

* * * * *

Notes
-----

-   Ensure that the `budget.csv` file exists in the same directory as the `plot_service.py` script.
-   The date format in the CSV file should be `YYYY-MM-DD`.
-   The date range provided by the client must be within the range of available dates in the `budget.csv` file.
-   If the service cannot process the data, it will respond with an error message indicating the issue (e.g., invalid date range or file not found).

* * * * *

How to Run
----------

1.  **Start the Plotting Service**:

    -   In one terminal, run the `plot_service.py` script to start the server.

    bash

    Copy code

    `python plot_service.py`

2.  **Request a Plot**:

    -   In another terminal, run the `client.py` script to send a request for a bar graph of income and expenses within a date range.

    bash

    Copy code

    `python client.py`

3.  **Enter Date Range**:

    -   The client will prompt you to enter the start and end dates in the `YYYY-MM-DD` format.
    -   The server will respond with a message indicating if the bar graph was successfully generated or if there was an issue.
