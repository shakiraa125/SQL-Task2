import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Connect to MySQL Database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shakira",
            database="Hotelbooking"
        )
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# Add Room
def add_room():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Rooms (RoomNumber, RoomType, PricePerNight) VALUES (%s, %s, %s)", 
                           (room_number.get(), room_type.get(), price_per_night.get()))
            conn.commit()
            messagebox.showinfo("Success", "Room added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        conn.close()

# Add Customer
def add_customer():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Customers (CustomerName, Email, PhoneNumber) VALUES (%s, %s, %s)", 
                           (customer_name.get(), email.get(), phone_number.get()))
            conn.commit()
            messagebox.showinfo("Success", "Customer added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        conn.close()

# Add Reservation
def add_reservation():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Reservations (CustomerID, RoomID, CheckInDate, CheckOutDate) VALUES (%s, %s, %s, %s)", 
                (customer_id.get(), room_id.get(), check_in_date.get(), check_out_date.get()))
            conn.commit()
            messagebox.showinfo("Success", "Reservation added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        conn.close()

# Add Payment
def add_payment():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Payments (ReservationID, PaymentDate, Amount, PaymentMethod) VALUES (%s, %s, %s, %s)", 
                (reservation_id.get(), payment_date.get(), amount.get(), payment_method.get()))
            conn.commit()
            messagebox.showinfo("Success", "Payment added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        conn.close()
# Show Table in a Popup Window
def show_table(query, columns, title):
    conn = connect_to_db()
    if not conn:
        return

    # Create Popup Window
    popup = tk.Toplevel()
    popup.title(title)
    popup.geometry("800x400")
    popup.configure(bg="#E0F7FA")

    # Treeview to Display Data
    tree = ttk.Treeview(popup, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(fill="both", expand=True)

    # Fetch and Display Data
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        conn.close()


# View Rooms
def view_rooms():
    query = "SELECT * FROM Rooms"
    columns = ["RoomID", "RoomNumber", "RoomType", "PricePerNight","AvailabilityStatus"]
    show_table(query, columns, "Room Details")


# View Customers
def view_customers():
    query = "SELECT * FROM Customers"
    columns = ["CustomerID", "CustomerName", "Email", "PhoneNumber"]
    show_table(query, columns, "Customer Details")


# View Reservations
def view_reservations():
    query = "SELECT * FROM Reservations"
    columns = ["ReservationID", "CustomerID", "RoomID", "CheckInDate", "CheckOutDate","TotalAmount","ReservationStatus"]
    show_table(query, columns, "Reservation Details")


# View Payments
def view_payments():
    query = "SELECT * FROM Payments"
    columns = ["PaymentID", "ReservationID", "PaymentDate", "Amount", "PaymentMethod"]
    show_table(query, columns, "Payment Details")


# Tkinter GUI
app = tk.Tk()
app.title("Hotel Booking Management System")
app.geometry("1200x600")
app.configure(bg="#E0F7FA")  # Light blue background

# Heading
tk.Label(app, text="Hotel Booking Management System", font=("Arial", 24, "bold"), bg="#0277BD", fg="white", pady=10).pack(fill="x")

# Frames for sections
room_frame = tk.Frame(app, bg="#E0F7FA", padx=10, pady=10)
customer_frame = tk.Frame(app, bg="#E0F7FA", padx=10, pady=10)
reservation_frame = tk.Frame(app, bg="#E0F7FA", padx=10, pady=10)
payment_frame = tk.Frame(app, bg="#E0F7FA", padx=10, pady=10)

room_frame.pack(side="left", fill="both", expand=True)
customer_frame.pack(side="left", fill="both", expand=True)
reservation_frame.pack(side="left", fill="both", expand=True)
payment_frame.pack(side="left", fill="both", expand=True)

# Room Section
tk.Label(room_frame, text="Rooms", font=("Arial", 18, "bold"), bg="#E0F7FA").pack()
tk.Label(room_frame, text="Room Number", font=("Arial", 14), bg="#E0F7FA").pack()
room_number = tk.Entry(room_frame, font=("Arial", 14))
room_number.pack()
tk.Label(room_frame, text="Room Type", font=("Arial", 14), bg="#E0F7FA").pack()
room_type = ttk.Combobox(room_frame, values=["Single", "Double", "Suite"], font=("Arial", 14))
room_type.pack()
tk.Label(room_frame, text="Price Per Night", font=("Arial", 14), bg="#E0F7FA").pack()
price_per_night = tk.Entry(room_frame, font=("Arial", 14))
price_per_night.pack()
tk.Button(room_frame, text="Add Room", command=add_room, font=("Arial", 14), bg="#0288D1", fg="white").pack(pady=10)
tk.Button(room_frame, text="View Rooms Details", command=view_rooms, font=("Arial", 14), bg="#0288D1", fg="white").pack(pady=10)


# Customer Section
tk.Label(customer_frame, text="Customers", font=("Arial", 18, "bold"), bg="#E0F7FA").pack()
tk.Label(customer_frame, text="Customer Name", font=("Arial", 14), bg="#E0F7FA").pack()
customer_name = tk.Entry(customer_frame, font=("Arial", 14))
customer_name.pack()
tk.Label(customer_frame, text="Email", font=("Arial", 14), bg="#E0F7FA").pack()
email = tk.Entry(customer_frame, font=("Arial", 14))
email.pack()
tk.Label(customer_frame, text="Phone Number", font=("Arial", 14), bg="#E0F7FA").pack()
phone_number = tk.Entry(customer_frame, font=("Arial", 14))
phone_number.pack()
tk.Button(customer_frame, text="Add Customer", command=add_customer, font=("Arial", 14), bg="#0288D1", fg="white").pack(pady=10)
tk.Button(customer_frame, text="View Customers details", command=view_customers, font=("Arial", 14), bg="#0288D1", fg="white").pack(pady=10)


# Reservation Section
tk.Label(reservation_frame, text="Reservations", font=("Arial", 18, "bold"), bg="#E0F7FA").pack()
tk.Label(reservation_frame, text="Customer ID", font=("Arial", 14), bg="#E0F7FA").pack()
customer_id = tk.Entry(reservation_frame, font=("Arial", 14))
customer_id.pack()
tk.Label(reservation_frame, text="Room ID", font=("Arial", 14), bg="#E0F7FA").pack()
room_id = tk.Entry(reservation_frame, font=("Arial", 14))
room_id.pack()
tk.Label(reservation_frame, text="Check-In Date", font=("Arial", 14), bg="#E0F7FA").pack()
check_in_date = tk.Entry(reservation_frame, font=("Arial", 14))
check_in_date.pack()
tk.Label(reservation_frame, text="Check-Out Date", font=("Arial", 14), bg="#E0F7FA").pack()
check_out_date = tk.Entry(reservation_frame, font=("Arial", 14))
check_out_date.pack()
tk.Button(reservation_frame, text="Add Reservation", command=add_reservation, font=("Arial", 14), bg="#0288D1", fg="white").pack(pady=10)
tk.Button(reservation_frame, text="View Reservations Details", command=view_reservations, font=("Arial", 14), bg="#0288D1", fg="white").pack(pady=10)

# Payment Section
tk.Label(payment_frame, text="Payments", font=("Arial", 18, "bold"), bg="#E0F7FA").pack()
tk.Label(payment_frame, text="Reservation ID", font=("Arial", 14), bg="#E0F7FA").pack()
reservation_id = tk.Entry(payment_frame, font=("Arial", 14))
reservation_id.pack()
tk.Label(payment_frame, text="Payment Date", font=("Arial", 14), bg="#E0F7FA").pack()
payment_date = tk.Entry(payment_frame, font=("Arial", 14))
payment_date.pack()
tk.Label(payment_frame, text="Amount", font=("Arial", 14), bg="#E0F7FA").pack()
amount = tk.Entry(payment_frame, font=("Arial", 14))
amount.pack()
tk.Label(payment_frame, text="Payment Method", font=("Arial", 14), bg="#E0F7FA").pack()
payment_method = ttk.Combobox(payment_frame, values=["Credit Card", "Cash", "Online"], font=("Arial", 14))
payment_method.pack()
tk.Button(payment_frame, text="Add Payment", command=add_payment, font=("Arial", 14), bg="#0288D1", fg="white").pack(pady=10)

tk.Button(payment_frame, text="View Payment Details", command=view_payments, font=("Arial", 14), bg="#0288D1", fg="white").pack(pady=10)


app.mainloop()
