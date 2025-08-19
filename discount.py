# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount: price * (discount_percent / 100)
        discount_amount = price * (discount_percent / 100)
        # Return final price after discount
        return price - discount_amount
    return price

# Prompt user for input
try:
    # Get original price
    price = float(input("Enter the original price of the item: "))
    # Get discount percentage
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Validate inputs
    if price < 0 or discount_percent < 0:
        print("Error: Price and discount percentage must be non-negative.")
    else:
        # Calculate final price using the function
        final_price = calculate_discount(price, discount_percent)
        # Print result with 2 decimal places for currency
        print(f"The final price is: ${final_price:.2f}")
except ValueError:
    print("Error: Please enter valid numbers for price and discount percentage.")