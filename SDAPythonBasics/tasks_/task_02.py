"""2- Write a program which, based on the variables: amount - amount (float) and
number of installments - number_of_installments (int), will calculate the monthly loan installment and write it to the console.

The parameters have restrictions:
    -the loan amount must be between PLN 100.00 and PLN 10,000.00,
    -the number of installments must be between 6 and 48.

If the loan amount exceeds the acceptable range, the loan amount should be set at PLN 5,000.00.
If the number of installments exceeds the acceptable range, the number of installments should be set to 36.

The calculated monthly installment should also include interest. To simplify the calculations, assume that you add X percent
to the loan amount depending on the number of installments:

6-12 installments - 2.5%,
13-24 installments - 5.0%,
25-48 installments - 10.0%,
and then calculate the installment amount based on the number of installments.

Get data from the user in the console using argument-less input().

"""
amount_str = input("Type amount you wish:")
number_installments_str = input("Type number of installments:")

amount = float(amount_str)
number_installments = int(number_installments_str)

if amount < 100 or amount > 10000.0:
    print("We can not provide a loan for this amount")
    exit()

if number_installments < 6 or number_installments > 48:
    print("We can not provide a loan for this number of installments")
    exit()


loan_interest = 0

if number_installments >= 6 and number_installments <= 12:
    loan_interest = 0.025
elif number_installments >= 13 and number_installments <= 24:
    loan_interest = 0.05
else:
    loan_interest = 0.1

monthly_payment_amount = amount * (1.0 + loan_interest) / number_installments

print("Your monthly payment will be ", monthly_payment_amount)

