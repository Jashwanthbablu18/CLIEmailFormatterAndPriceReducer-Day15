# Day 14 - map, filter and reduce
# Topic: Using Map/Filter to clean and format a list of emails. Using reduce to total prices.

# Importing reduce from functools module. map() and filter() are built-in functions
from functools import reduce

# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("🛠️ Day 15 - Map, Filter, Reduce")
    print("🔹 Topic: Email Cleaning & Price Summation using Functional Tools\n")

# This function is used to clean and filter emails
def clean_emails(emails):
    print("📧 Cleaning and filtering emails...\n")

    # Here we are using .strip() and .lower() to remove spaces and conbert into lowercase letters of emails by using map().
    cleaned = list(map(lambda e: e.strip().lower(), emails))

    # Here we are validating cleaned emails by filtering by @ and . by using filter().
    valid = list(filter(lambda e: "@" in e and "." in e, cleaned))

    # This line is used to display the valid emails after maping, filtering.
    print("✅ Cleaned & Valid Emails:")
    for email in valid:
        print("   -", email)

    # returns valid emails
    return valid

# This function is used to reduce the list of all prices into a single value.
def calculate_total(prices):
    print("\n💰 Calculating total price using reduce...")

    # Uses lambda function in reduce() by passing prices list to reduce all prices into a single value.
    total = reduce(lambda x, y: x + y, prices)

# Displays and returns the total reduced value
    print(f"🧾 Total Price: ₹{total}")
    return total

# main
def main():

    # calling show_intro() to display introduction msg.
    show_intro()

    # List of raw emails
    raw_emails = [
        "  JasHwanthN2004@gmail.com  ",
        "NavadEEp@gMaIl.COM",
        "chetana@HealthCare.com",
        "TeStCaSe@example",
        "   TrIsHuL@eDu.oRg   ",
        "   SuDaRsHan@Edu.iN   ",
        "invalid-email"
    ]

    # Passing the raw emails list into clean_emails() by calling it to validate, filtered and cleaned emails
    clean_emails(raw_emails)

    # list of prices
    prices = [199.99, 49.50, 25.00, 100.00]

    # Passing the prices list into calculate_total() by caling it to reduce prices into a single value
    calculate_total(prices)


# Starting point: The script is designed to run when executed directly. The conditional if __name__ == "__main__": main() ensures that main() is called only when the script is run as a standalone program, not when imported as a module.
if __name__ == "__main__":
    main()

