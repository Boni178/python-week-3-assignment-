def calculate_discount():
    try:
        # Get the users input for the price and the discount percent
        price = float (input ( "Enter your price: " ))
        discount_percent = float (input ( "Enter your discount percentage: " ))

        # Calculate the discounted price
        discount_price = price - ( price * discount_percent / 100 )

        # Checks to see if the discount price is 20% or more
        #.2f limits the output to 2 decimal places 

        # Check if the discount is 20% or more of the original price
        if (price - discount_price) >= (0.2 * price):

            # prints the discount price
            print ( f"Discounted price: {discount_price:.2f}" ) 

        # prints the original price
        else:
            print ( f"Original price: {price:.2f}" ) 
             
        #makes sure the input is a valid number3
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

# Calls the function to execute program
calculate_discount()