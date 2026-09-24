import os
#displays the main menu
def print_display_main_menu():
    print('=' * 40)
    print('      SALES RECORD MANAGEMENT SYSTEM  ')
    print('=' * 40)
    print('1. Add Sale Record')
    print('2. View All Records & Summary Statistics')
    print('3. Clear All Sales Data')
    print('4. Exit System')

#asks for user input from the main menu and validates it
def get_user_selection():
    user_selection = input('Select an option 1-4')

    #Validates user input
    try:
        selected_input = int(user_selection)
    except ValueError:
        print('Please enter a valid input like numbers 1 to 4')
        print_display_main_menu()
        get_user_selection()

    if selected_input > 4 or selected_input < 1:
        print('Please enter a valid input like numbers 1 to 4')
        print_display_main_menu()
        get_user_selection()
    elif selected_input >= 1 and selected_input <= 4:
        return selected_input

#add record to file
def add_sales_record():
    item_name = input('Item Name: ')
    quantity_sold_input = input('Quantity Sold: ')
    price_per_unit_input = input('Price Per Unit: ')

    try:
        quantity_sold = int(quantity_sold_input)
        price_per_unit = float(price_per_unit_input)
    except ValueError:
        print('Inputs are Invalid Please Try Again.')
        add_sales_record()

    if not item_name.strip():
        print('Item Name cannot be blank')
        add_sales_record()
    try:
        fhand = open('sales_log.txt', 'a')
    except FileNotFoundError:
        # if file not found then create
        fhand = open('sales_log.txt' 'x')
        fhand.write('Name|Quantity|Price Per Unit|Total Amount')

    # calculates then inserts it to the files
    total_amount = quantity_sold * price_per_unit
    fhand.write(f'{item_name},{quantity_sold},{price_per_unit},{total_amount}')
    print('Sales record saved successfully')
    print_display_main_menu()
    get_user_selection()

# Views the entire files and displays it to the user
def view_all_records(total_units_sold = 0,
        grand_total_revenue = 0):
    try:
        fhand = open('sales_log.txt', 'r')
    except FileNotFoundError:
        print('No records found')
        print_display_main_menu()
        get_user_selection()


    for lines in fhand:
        print(lines)
        lines_info = lines.split(',')
        if len(lines_info) >0:
            total_units_sold += int(lines_info[1])
            grand_total_revenue += int(lines_info[3])

        print(f'Total Units Sold: {total_units_sold}')
        print(f'Grand Total Revenue: {grand_total_revenue}')

#deletes the entire file
def clear_all_record():
    fhand = open('sales_log.txt')
    os.remove('sales_log.txt')
    print('All records cleared. No records remaining.')
    print_display_main_menu()
    get_user_selection()



print_display_main_menu()

#checks for user input and directs to proper process
user_option_selected = get_user_selection()
if user_option_selected == 1:
    add_sales_record()
elif user_option_selected == 2:
    view_all_records()
elif user_option_selected == 3:
    add_sales_record()
elif user_option_selected == 4:
    exit('Thank you for using the Sales Record Management System.')





