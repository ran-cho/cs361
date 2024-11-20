import zmq
import matplotlib.pyplot as plt
import csv
from datetime import datetime

FILENAME = "budget-test.csv"

def generate_bar_graph(start_date, end_date):
    """Generate a bar graph showing total income and expenses within a date range."""
    try:
        income_total = 0
        expense_total = 0

        # Read and process the CSV file
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                date = datetime.strptime(row["Date"], "%Y-%m-%d")
                if start_date <= date <= end_date:
                    amount = float(row["Amount"])
                    if row["Type"] == "Income":
                        income_total += amount
                    elif row["Type"] == "Expense":
                        expense_total += amount

        # Plot the bar graph
        categories = ["Income", "Expenses"]
        totals = [income_total, expense_total]

        plt.figure(figsize=(8, 5))
        plt.bar(categories, totals, color=["green", "red"])
        plt.title(f"Total Income vs. Expenses ({start_date.date()} to {end_date.date()})")
        plt.ylabel("Amount ($)")
        plt.tight_layout()
        plt.show()

        return "Bar graph generated successfully!"
    except FileNotFoundError:
        return "Error: Budget file not found."
    except ValueError:
        return "Error processing data. Please check the CSV file for valid entries."

def main():
    """ZeroMQ server to handle plot requests."""
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5555")

    print("Plotting service started. Waiting for requests...")

    while True:
        # Wait for a request
        message = socket.recv_string()
        print(f"Received request: {message}")

        if message.startswith("BAR"):
            _, start_date_str, end_date_str = message.split()
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            response = generate_bar_graph(start_date, end_date)
        else:
            response = "Unknown request. Please send 'BAR' with a valid date range."

        # Send response back to the client
        socket.send_string(response)

if __name__ == "__main__":
    main()
