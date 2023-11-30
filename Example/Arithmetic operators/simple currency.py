# Currency conversion rates
idr_to_usd = 0.000070
usd_to_idr = 14285.71

# Function to convert IDR to USD
def idr_to_usd_converter(amount):
    return amount * idr_to_usd

# Function to convert USD to IDR
def usd_to_idr_converter(amount):
    return amount * usd_to_idr

# Main program
print("Currency Converter")
print("1. IDR to USD")
print("2. USD to IDR")

choice = int(input("Enter your choice (1/2): "))

if choice == 1:
    idr_amount = float(input("Enter the amount in IDR: "))
    usd_amount = idr_to_usd_converter(idr_amount)
    print(f"{idr_amount} IDR is equal to {usd_amount} USD")
elif choice == 2:
    usd_amount = float(input("Enter the amount in USD: "))
    idr_amount = usd_to_idr_converter(usd_amount)
    print(f"{usd_amount} USD is equal to {idr_amount} IDR")
else:
    print("Invalid choice!")
