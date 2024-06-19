# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
deposits_made = 0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0 and (principal * (1+rate/12) - (payment + extra_payment)) >= 0:
	principal = principal * (1+rate/12) - payment
	total_paid = total_paid + payment
	deposits_made += 1
	print(deposits_made, total_paid, principal)

	if extra_payment > 0 and deposits_made == extra_payment_start_month and deposits_made <= extra_payment_end_month:
		for i in range(extra_payment_start_month, extra_payment_end_month):
			if (principal * (1+rate/12) - (payment + extra_payment)) <= 0:
				break
			else:
				principal = principal * (1+rate/12) - (payment + extra_payment)
				total_paid = total_paid + (payment + extra_payment)
				deposits_made += 1
				print(deposits_made, total_paid, principal)
print(f"Total paid {total_paid}\nMonths: {deposits_made}")