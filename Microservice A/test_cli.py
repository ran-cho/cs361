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
