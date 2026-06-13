print ("== Personal finance calculator == ")
print (' 1. Tip calculator')
print (' 2. Salary Breakdown')
print (' 3. Savings Goal')
print (' 4. Loan payment Estimator')

choice = input ('pick an option (1-4)')
choice = int(choice)

if choice == 1:
    tip = input('how much of a percentage do you want to tip ? (input percentage without symbol)')
    tip = float(tip)

    bill = input('what is the total bill value?')
    bill = float(bill)

    result = (tip/100) * bill

    print (f'You should tip ${result :0.2f} making a total bill of ${result + bill :0.2f} ')

elif choice == 2:
    salary = input ('what is your early salary ?')
    salary = float(salary)

    print(f'Yearly  :  {salary :0.2f}')
    print(f'Monthly :  {salary/12 :0.2f}')
    print(f'Weekly  :  {salary/52 :0.2f}')
    print(f'Daily   :  {salary/365  :0.2f}')

elif choice == 3:
    goal=input('what is your savings goal?')
    goal = float(goal)

    save=input('how much can you save per month?')
    save = float(save)

    print (f'It will take you {goal/save} months to reah your goal')

elif choice == 4:
    loan = input(' what is the loan amount?')
    interest = input ('what is the annual interest rate?')
    years = input('what is the number of years for the loan?')

    loan = float(loan)
    interest = float(interest)
    years = float(years)

    monthly_rate =interest/(100*12)
    num_payments = years*12
    monthly_payment = loan* (monthly_rate *(1+ monthly_rate)**num_payments)/((1 + monthly_rate)**num_payments -1)
    



print (f'Loan amount $              {loan :0.1f}')
print (f'Annual interest rate (%) : {interest :0.1f}')
print (f'Loan term (years)        : {years :0.1f}')
print (f'Monthly payment          : ${monthly_payment :0.1f}')
print (f'Total paid               : ${(monthly_payment*num_payments) :0.1f}')
print (f'Total interest.          : ${((monthly_payment*num_payments)-loan) :0.1f}')


    
