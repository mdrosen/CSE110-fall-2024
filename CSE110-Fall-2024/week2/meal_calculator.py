#created by Matthew Rosenthal
#added tax and change verification and add a tax function to calculate the tax on the order

#get cost of meals from user
adult_meal = float(input ('how much does the adult meal cost?: $'))
kid_meal = float(input ('how much does the kid meal cost?: $'))

# get number of meals for each category
num_adults = int(input ('How many adult meals do you want?:' ))
num_kid = int(input ('How many kid meals do you want?: '))

#get tax rate from user 
rate = float(input('what is the tax percentage?: '))
#validate tax rate
while True:
    rate < 1
    if rate <= 0:
        temp = float(input('Please enter a Valid tax rate must be greater than 1: '))
        rate = temp
    else:
        break
tax_rate = rate

print('--------------------------------------------')
#calculate total cost of meals before taxes
k = float(num_kid) * kid_meal
a = float(num_adults) * adult_meal
subtotal = k + a 
sub_total = (f'{subtotal:.2f}')
print ('SubTotal: $',sub_total)

#define tax on meal function with percentage and subtotal as inputs for the function 
def tax(p , s):
    pr = float(p)
    rate = (pr * s) / 100
    return rate

#calculate tax with percentage and subtotal as inputs for the function 
# and then output to user 
total_tax = tax(tax_rate,subtotal)
print(f'Tax: ${total_tax:.2f}')

#display total due to user
total = subtotal + total_tax
print (f'Total: ${total:.2f}')
cash = float(input('How much cash were you given?: $'))
C = cash
T = total
change = C-T
#Cash and total

while True:
    change < 0
    if change >= 0:
        print(f'The change due is: ${change:.2f}')
        break
    else:
        temp = abs(change)
        print(f'Still Needed: ${temp:.2f}')
        more = float(input('How much more money was given?: $'))
        C += more
        change = C-T

print('-------------------------------------------------')

