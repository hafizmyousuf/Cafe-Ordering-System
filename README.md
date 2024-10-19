# Cafe Ordering System

## Overview
The **Cafe Ordering System** is a simple Python console application that allows users to place orders from a pre-defined menu. The program calculates the total bill based on the items ordered and displays the bill once the order is completed.

## Features
- **Menu options** include: Pizza, Drink, Tea, Coffee, and Water with corresponding prices.
- Allows the user to select items multiple times until the order is completed.
- Displays the total bill at the end of the ordering process.
- Provides input validation to handle invalid inputs gracefully.
  
## Menu
- Pizza: 1000 PKR
- Drink: 200 PKR
- Tea: 150 PKR
- Coffee: 250 PKR
- Water: 50 PKR

## How it Works
1. The user is welcomed with a menu of available items.
2. The user can type the name of an item (e.g., "Pizza" or "Coffee") to place an order.
3. The program accumulates the total bill based on the items selected.
4. If the user enters an item not in the menu, the program will prompt the user to try again.
5. The order can be completed by pressing `Q` or `q`.
6. The program then displays the final bill with a thank-you message.

## Code Structure
- **`Cafe` class**: The main class that manages the customer's orders and billing process.
  - **`details()` method**: Handles customer inputs, checks the order against the menu, and calculates the total bill.
  - **`print_bill()` method**: Displays the final bill after the order is completed.

## Example Usage
```
********** Welcome To Pathan Cafe **********
Our Menu List is:
Pizza : 1000
Drink : 200
Tea : 150
Coffee : 250
Water : 50

Place your order with order name or press Q to complete your order: Pizza
Place your order with order name or press Q to complete your order: Drink
Place your order with order name or press Q to complete your order: q

********** Welcome To Pathan Cafe **********

********** Thanks For Coming here **********

Total Bill = 1200
```

## How to Run the Program
1. Clone or download the project files.
2. Ensure Python is installed on your system.
3. Run the program using:
   ```bash
   python cafe_ordering_system.py
   ```
4. Follow the prompts in the terminal to place your order and get the total bill.

## License
This project is open-source and can be modified or distributed freely.
