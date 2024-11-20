# Budgeting Plot Service Microservice

This repository implements a Budgeting Plot Service Microservice using ZeroMQ. The microservice processes requests to generate a bar graph comparing total income and expenses within a given date range. The service reads from a CSV file (`budget.csv`) where entries of income and expenses are logged.

---

## Communication Contract

1. **Protocol**: ZeroMQ REQ-REP  
2. **Request Format**:  
   The client sends a string message: `"BAR YYYY-MM-DD YYYY-MM-DD"` (start date and end date in the format `YYYY-MM-DD`).  
   Only this specific format will work for requesting the bar graph.  
3. **Response Format**:  
   The server replies with a string containing the status of the plot request (success or failure message).

---

## How to Request / Receive Data 

To request data, the client must:

1. Connect to the server's endpoint (`tcp://localhost:5555`, but the port can be changed).
2. Send the message: `"BAR YYYY-MM-DD YYYY-MM-DD"` (start date and end date). Example:

3. Ensure the `budget.csv` file exists and contains valid entries.

To receive data, the client must:

1. The server will generate a bar graph comparing total income and total expenses for the specified date range.
2. The result will be shown as a bar graph where:
- Green bar: Total Income
- Red bar: Total Expenses
3. The response from the server will indicate whether the graph was generated successfully or if there was an issue (e.g., file not found, invalid date range).

### Code Snippet:

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
 start_date = input("Enter start date (YYYY-MM-DD): ")
 end_date = input("Enter end date (YYYY-MM-DD): ")
 request_plot(start_date, end_date)

Notes
-The server expects a request in the form: "BAR YYYY-MM-DD YYYY-MM-DD", where the first date is the start date and the second date is the end date.
-The server processes the request and returns a success message or error.
-If the file budget.csv is not found or contains errors, the server will respond with an error message.
-The CSV file should have entries with the following format: Date, Type (Income/Expense), Category, Description, Amount
-Ensure that the date range provided by the client matches the format YYYY-MM-DD.
-The server will display a bar graph where:
    -Green represents total income.
    -Red represents total expenses.