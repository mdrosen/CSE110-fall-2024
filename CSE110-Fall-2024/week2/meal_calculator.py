
#get cost of meals from user
adult_meal=float(input ('how much does the adult meal cost?: $'))
kid_meal = float(input ('how much does the kid meal cost?: $'))
# get number of meals for each category
num_adults = int(input ('How many adult meals do you want?:' ))
num_kid = int(input ('How many kid meals do you want?: '))
#get tax rate from user 
tax_rate = float(input('what is the tax percentage?: '))
#calculate total cost of meals before taxes
k = float(num_kid) * kid_meal
a = float(num_adults) * adult_meal
subtotal = k + a 
sub_total=(f'{subtotal:.2f}')
print ('SubTotal: $',sub_total)
#define tax with percentage and subtotal as inputs for the function 
def tax(p , s):
    pr=float(p)
    rate = (pr * s )/100
    return rate

#calculate tax with percentage and subtotal as inputs for the function 
# and then output to user 
total_tax = tax(tax_rate,subtotal)
print(f'Tax: ${total_tax:.2f}')

total = subtotal + total_tax
print (f'Total: ${total:.2f}')

#Cash and total 
def change(c,t):
    change = c - t
    return change

cash = float(input('How much cash were you given?: '))
change_due = cash-total
print (f'the Change Due is: ${change_due:.2f}')
