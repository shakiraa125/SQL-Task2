**Name:SHAKIRA\
Company:CODETECH IT SOLUTION\
ID:CT12FDE\
Domain:SQL\
Duration:December 20th, 2024 to February 20th, 2025**
## Hotel Booking Management System 
---
**TASK:**
Create a database for managing hotel bookings, including rooms, customers, reservations, and payments. This project involves handling complex queries and managing booking data.
Design tables for rooms, customers, reservations, and
payments..\
**Language Used:**
- SQL
- Python

**Tools Utilized:**
- MySQL
- Visual Studio Code
- ### **Project Overview:**
The Hotel Booking Management System is a comprehensive application designed to manage hotel 
operations, including room management, customer data, reservations, and payments. The system leverages 
a MySQL database for backend operations and a Python-based GUI using Tkinter for user interaction. It 
features a clean, user-friendly interface and enables users to view and manage key hotel-related data 
efficiently.\

### **• Features**
**1. Room Management:**
1. Add new rooms with attributes like room number, type, and price per night.\
2. View existing room details in a tabular format.\
**2. Customer Management:**
1. Add new customer information, including name, email, and phone number.\
2. View the customer database.\
**3. Reservation Management:**
1. Record reservations with details like customer ID, room ID, check-in, and check-out dates.\
2. View reservations in a detailed table.\
**4.Payment Management:**
Manage payments with details like reservation ID, payment date, amount, and payment method.\
View all payment transactions in a tabular format.\
### **Interactive GUI**:
Buttons to view details for rooms, customers, reservations, and payments.\
Pop-up windows displaying database tables with a clean and scrollable layout.\
Light blue theme for the GUI with a bold header.\
### **System Architecture Frontend**\
**•Python Tkinter:**
• Used for designing the graphical user interface (GUI).\
• Includes buttons, labels, and tree views for displaying data.\
### **Backend**
**•MySQL Database:**
• Four tables: Rooms, Customers, Reservations, and Payments.\
• Queries are dynamically executed to fetch and display data.\
### **Database Design Tables**
***1.Rooms:**
•RoomID: Primary key\
•RoomNumber: Unique identifier for each room\
•RoomType: Type of room (e.g., Single, Double, Suite)\
•PricePerNight: Cost per night for the room\
**2.Customers:**
•CustomerID: Primary key\
•CustomerName: Name of the customer\
•Email: Email address of the customer\
•PhoneNumber: Contact number of the customer\
**3.Reservations:**\
•ReservationID: Primary key\
•CustomerID: Foreign key referencing Customers\
•RoomID: Foreign key referencing Rooms\
•CheckInDate: Start date of the reservation\
•CheckOutDate: End date of the reservation\
**4.Payments:**\
•PaymentID: Primary key\
•ReservationID: Foreign key referencing Reservations\
•PaymentDate: Date of payment\
•Amount: Payment amount\
•PaymentMethod: Mode of payment (e.g., Credit Card, Cash)\

 **GUI**
![Library Management System GUI](https://github.com/shakiraa125/SQL-Task2/blob/main/Task2-Hotel%20Booking%20management%20system/Images/Screenshot%20(244).png)
### Conclusion
The Hotel Booking Management System is a versatile and user-friendly tool for managing hotel operations. 
With its robust database design and clean interface, it simplifies the tasks of handling room bookings, 
customer data, and financial transactions. Future enhancements can make the system even more powerful 
and adaptable to complex requirements
