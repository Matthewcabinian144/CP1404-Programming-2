"""CP1404 Practice & Extension work: Electrcity bill 2.0"""
#Tariff pricing per day
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_option = int(input("What is your Tariff Option? 11 or 31?: "))
number_of_billing_days = int(input("Enter number of billing days: "))
daily_use_kWh = float(input("Enter daily use in kWh: "))

if tariff_option == 11:
    customer_tariff = TARIFF_11
elif tariff_option == 31:
    customer_tariff = TARIFF_31
else:
    print("Invalid Tariff Number")

estimated_bill = customer_tariff * daily_use_kWh * float(number_of_billing_days)
print(round(estimated_bill, 2))
