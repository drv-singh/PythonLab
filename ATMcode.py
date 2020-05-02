class atm:
    def __init__(self,name):
        self.name=name
    def acc_info(self):
        print('Account Information: ')
        print('Name: ', name, end='\n')
        print('Account Number: ', info[name][0], end='\n')
        print('Phone Number: ', info[name][1], end='\n')
    def pin_change(self):
        i=3
        while(i>0):
            p=int(input('Enter Original PIN: '))
            if p==info[name][2]:
                x=input('Enter New PIN: ')
                info[name][2]=x
                break
            else:
                i=i-1
                print('Incorrect PIN, {} tries left'.format(i))
        if i==0:
            del info[name]
            print('Account Blocked!')
    def acc_balance(self):
        print('Account Balance: ',info[name][3])
    def withdraw(self):
        print('Account Balance: ',info[name][3])
        amt=float(input('Enter Amount To Withdraw: '))
        if amt<=info[name][3]:
            info[name][3]=info[name][3]-amt
            print('New Account Balance: ', info[name][3])
        else:
            print('Insufficient Balance in Account!')
    def deposit(self):
        amt=float(input('Enter Amount To Deposit: '))
        info[name][3]=info[name][3]+amt
        print('New Account Balance: ', info[name][3])
    
info={"Boss":[5212485411,123454562,1111,15000.00], "Ravi":[4559845253,1234567895,2222,100000.00], 'Dhruv':[1234567890,1122334455,1234,500000.00], "Ankit":[4559857142,12345677412,3333,190000.00], 'Darsh':[4559848475,123458481,4444,155000.00]}
k=info.keys()
while (1):
    name=str(input('Enter Name: '))
    if name in k:
        i=3
        while(i>0):
            pin=int(input('Enter PIN: '))
            if pin==info[name][2]:
                a=atm(name)
                while(1):
                    print('Enter 1 For Account Info')
                    print('Enter 2 For PIN Change')
                    print('Enter 3 For Balance Inquiry')
                    print('Enter 4 For Withdrawal')
                    print('Enter 5 For Deposit')
                    s=int(input('Select Operation: '))
                    if s==1:
                        a.acc_info()
                    elif s==2:
                        a.pin_change()
                    elif s==3:
                        a.acc_balance()
                    elif s==4:
                        a.withdraw()
                    elif s==5:
                        a.deposit()
                    else:
                        print('Invalid Option Selected! Choose Again')
                        continue
                    e=input('Enter Y to exit, press any other key to continue operations: ')
                    if e=='y' or e=='Y':
                        print('Thank You!')
                        break
                    else:
                        continue
                break
            else:
                i=i-1
                print('Incorrect PIN, {} tries left'.format(i))
        if i==0:
            del info[name]
            print('Account Blocked!')
        break
        





