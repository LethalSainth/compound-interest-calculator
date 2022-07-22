# Building a simple compound interest calculator

print('How much is currently in your acount?')
Principal = float(input('Account Balance:',))

print('How many years will you be investing for?')
years = int(input('Years:'))

print('How much do you plan on investing monthly?')
monthly_invest = float(input('Monthly investment amount:'))

print('What do you expecr will be the yearly interest on this investment')
interest = float(input('Interest %:'))/100



monthly_invest = monthly_invest * 12
final_amount  = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = Principal

    final_amount = (final_amount + monthly_invest) * (1 + interest)


print(f'You will have {final_amount:.2f} after {years} years')