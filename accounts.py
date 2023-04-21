# Alice Varley, student No. 201685457

"""Below describes two types of bank account, Basic and Premium. BasicAccount serves as a superclass to PremiumAccount.
PremiumAccount has added attributes which refer to an overdraft. It also has an additional method used to adjust the overdraft limit."""

from random import randint
from datetime import datetime, timedelta

class BasicAccount:
    """
    BasicAccount is a class which serves as a superclass to PremiumAccount and establishes basic information associated with a bank account. It has a class variable,
    accCount, which is used as the basis for a counter used to generate an account number. 

    When a BasicAccount object is created, it has an associated account holder name (acName, a string) and balance used to open the account (openingBalance, a float). 
    It also has an associated account number (acNum, an integer), but this is generated automatically rather than being entered by the user. The class variable accCount 
    is used as a counter in order to sequentially generate account numbers. 
 
    Other variables are added after the creation of the instance; cardNum is a 16-digit string which is generated if a new card is requested and cardExp (a tuple formed
    of two integers) serves as the expiry date on the card. 

    Methods:-
        init: 
            creates the BasicAccount object (i.e. creates the bank account) including account holder's name (acName) and openingBalance. Includes a counter used to
            create an account number (acNum). 
        str:
            provides a string representation of the object, which greets the account holder and displays their current balance via self.name and self.balance.
        deposit: 
            allows the user to update the balance by the given amount, via self.balance and amount. Restricts the user from depositing a negative amount.
        withdraw: 
            checks whether the given amount is valid (i.e. that there are sufficient funds to complete the transaction), updates self.balance using amount if
            appropriate and prints a string representation of the transaction using self.name, amount and self.balance. If there are insufficient funds, it prints a 
            message stating that the withdrawal of the given amount cannot occur. This is managed through exception handling. 
        getAvailableBalance: 
            creates and then returns a new variable, availableBalance, which has the same value as self.balance and represents the available funds in
            the account.  
        getBalance: 
            returns the balance of the account. Functionally, for BasicAccount this has the same utility as getAvailableBalance, however it differs for the 
            subclass PremiumAccount.
        printBalance: 
            prints a string which displays the account balance via self.balance. 
        getName: 
            returns the name of the account holder as a string via self.name. 
        getAcNum:
            returns the account number as a string via self.acNum. The value for this was assigned within the construction of the instance. 
        issueNewCard:
            creates a new card number with the expiry date being 3 years to the month from now. The card has sixteen digits, each of which are randomly assigned 
            an integer value between 0 and 9 using the random module. They are then each appended to the local list newCardDigits, and the digits are then
            converted to a string by joining them to it. 
            For the expiry date, a datetime object is created representing 3 years in the future from now. The corresponding month and year representing this are
            then converted into integers within the tuple. 
            In order to ensure that the card number generated is unique, it is cross-referenced with a global scope list, issuedCards. If the randomly generated
            number has already been issued (i.e., is in the list), then the function is called again using recursion.
        closeAccount: 
            checks whether there is any remaining balance in the account. If so, the balance is withdrawn and the function returns True. If the balance is exactly
            0, the function just returns True because there is nothing to withdraw. Finally, if the customer is in debt, a string explaining that they are overdrawn
            is printed and the function returns False. 
"""
    #A class variable initially set to zero. To be used to generate account numbers as a counter. 
    accCount = 0 
    def __init__(self, acName: str, openingBalance: float):
        """
        Initialises the BasicAccount object instance. 
        Parameters: self, acName (string) - the account holder's name, openingBalance (float) - the amount of money that the account is opened
        with
        Returns: nothing
        """
        #Assigns the argument for acName to the variable 'name'
        self.name = acName
        #Assigns the argument for openingBalance to the variable 'balance'
        self.balance = openingBalance 
        #Adds 1 to accCount and links it to this instance of the class object 
        BasicAccount.accCount += 1
        #Stores the value of accCount (which in practice is the number of accounts that have been created) as the object's account number
        self.acNum = BasicAccount.accCount
    def __str__(self): 
        """
        Provides a default string representation of the BasicAccount object instance. 
        Parameters: self. None to be given by user.
        Returns: string
        """
        #Returns an f-string 
        return f"Hello {self.name}, your available balance is currently £{self.balance}."  
    def deposit(self, amount: float):
        """
        Deposit updates the balance of a BasicAccount object by the specified amount.
        Parameters: self, amount (float amount to be deposited)
        Returns: nothing
        """
        #An exception handling block which raises and then throws a ValueError if amount is less than or equal to zero using an if-statement.
        try:
            #Checks whether the amount to be deposited is negative. If so, a ValueError is raised and the transaction is not successful.
            if amount <=0:
                raise ValueError("You must deposit a positive value greater than zero. Please try again.")
            else:
                #Where the deposit amount is positive, it adds the amount to the object's balance. 
                self.balance = self.balance + amount
        #Throws the ValueError for printing
        except ValueError as e1:
            print(e1)
    def withdraw(self, amount: float):
        """
        Withdraws the amount from the account if there are sufficient available funds in it and updates the account balance accordingly.
        Parameters: self, amount (float amount to be withdrawn)
        Returns: nothing 
        """
        #An exception handling block which raises and then throws a ValueError if amount is greater than the balance of the account.
        try:
            #Checks whether there aren't sufficient funds to withdraw the amount and raises an exception if this is the case. 
            if amount > self.balance:
                raise ValueError(f"Can not withdraw £{amount}.") 
            else:
                #Updates the 'balance' variable by subtracting the amount withdrawn
                self.balance = self.balance - amount
                #Prints an f-string which notifies the user of who has withdrawn how much and what their updated balance is
                print(f"{self.name} has withdrawn £{amount}. New balance is £{self.balance}") 
        #Throws the ValueError and prints it to alert the user 
        except ValueError as e2: 
            print(e2)
    def getAvailableBalance(self):
        """
        Returns the balance which the customer has available to use. 
        Parameters: self. None to be given by user.
        Returns: availableBalance (float)
        """
        #Assigns the argument for the variable 'balance' to a new variable, availableBalance
        availableBalance = self.balance
        return availableBalance
    def getBalance(self):
        """
        Returns the balance of the account.
        Parameters: self. None to be given by user.
        Returns: self.balance (float)
        """

        return self.balance
    def printBalance(self):
        """
        Prints to screen a message which shows the balance of the account. 
        Parameters: self. None to be given by user.
        Returns: nothing.
        """
        #Prints an f-string with the current balance of the account. Uses the balance returned by getBalance()
        print(f"Your current balance is {self.balance}.")
    def getName(self):
        """
        Returns the name of the account holder as a string.
        Parameters: self. None to be given by user.
        Returns: string version of self.name
        """
        #Converts self.name into a string and returns the f-string. 
        return f"{self.name}"
    def getAcNum(self):
        """
        Returns the account number of the instance as a string.
        Parameters: Self. None to be given by user. 
        Returns: number within a string which should also correspond to the number of accounts that have been opened.
        """
        #Converts self.acNum from an int into a string and returns the string
        return f"{self.acNum}"
    def issueNewCard(self):
        """
        Creates a new (unique) 16-digit card number with an expiry date being 3 years to the month from now. This is done by iterating 
        randomly generated ints over a list of variables all set by default to 0, appending each variable to a list then converting that
        list into a string. The card number is then checked against a list of already issued cards; if it hasn't appeared before (which is 
        most likely the case), then the card number is just added to the list of issued cards for future reference. If it has, then the 
        function is called again using recursion. 
        Parameters: Self. None to be given by user.
        Returns: nothing. 
        """
        #An exception handling block that checks whether the random number has already been used for a card. This ensures that card numbers are unique
        #An empty list of local scope which is used to store sixteen-digit strings of card numbers that have already been generated 
        issuedCards = []
        #An empty list of local scope that will be used to store sixteen random integers 
        newCardDigits = []
        try:
            #16 variables representing each digit of the card number, assigned the value of 0
            firstDigit = secondDigit = thirdDigit = fourthDigit = fifthDigit = sixthDigit = seventhDigit = eighthDigit = ninthDigit = tenthDigit = eleventhDigit = twelfthDigit = thirteenthDigit = fourteenthDigit = fifteenthDigit = sixteenthDigit = 0
            #A list containing the variables (digits), still all with the value 0
            cardNumDigits = [firstDigit,secondDigit,thirdDigit,fourthDigit,fifthDigit,sixthDigit,seventhDigit,eighthDigit,ninthDigit,tenthDigit,eleventhDigit,twelfthDigit,thirteenthDigit,fourteenthDigit,fifteenthDigit,sixteenthDigit]
            #A for-loop which iterates over each of the 16 digits
            for digit in cardNumDigits:
                #Assigns each position a random digit
                digit = randint(0,9)
                #Collates the digit into the list of new numbers
                newCardDigits.append(digit)
            #Converts the list of new numbers into a string 
            newCardNum = "".join(str(digit) for digit in newCardDigits)
            #Checks whether the string already exists in the list issuedCards
            if newCardNum in issuedCards:
                raise Exception("This card number has already been issued.")
            else:
                #Assigns the string to the variable 'cardNum'
                self.cardNum = newCardNum
                #Creates a datetime object which is three years in the future from now
                expYear = datetime.now() + timedelta(weeks=3*52, days=3, seconds=34)
                #Creates a tuple containing integer versions of the current month and the year three years from now. The year is converted to a two digit number using "%y"
                cardExp = (int(datetime.now().month), int(expYear.strftime("%y")))
                #Assigns the tuple to the variable 'cardExp'
                self.cardExp = cardExp
                #Appens the card number to the list of issued cards 
                issuedCards.append(newCardNum)
        except Exception as e3:
            #Recursively calls the function until a unique card number has been produced 
            self.issueNewCard()
    def closeAccount(self):
        """
        A method which is called before deleting an object instance. 
        The remaining balance is returned to customer via the withdraw method if it is a positive value. Note that there shouldn't be a 
        negative value here, as the class prevents users from withdrawing more than they have in debit in the account.
        Parameters: Self. None to be given by user.
        Returns: a Boolean value. 
        """
        #Checks if the account balance is greater than zero
        if self.balance > 0:
            #Calls the withdraw method on the remaining balance of the acount
            self.withdraw(self.balance)
            return True
        #Checks if the account balance is exactly zero, i.e. has no funds 
        elif self.balance == 0:
            return True
        #Assumes that the account has a negative balance. However, this shouldn't happen with BasicAccount because the withdraw method prevents the account balance from becoming negative. 
        else: 
            print(f"Can not close account due to customer being overdrawn by £{self.balance}")
            return False       
class PremiumAccount(BasicAccount):  
    """
    PremiumAccount is a subclass of BasicAccount. It has the added functionality of an overdraft. It inherits the initialiser for BasicAccount as well as the class
    variable acCount, and adds an overdraft (initialOverdraft, as a float). It inherits all the methods from BasicAccount, with some remaining exactly the same and 
    others with some changes in how they behave (owing to the overdraft).

    Methods:-
        init: 
            includes the initialiser from BasicAccount, plus initialOverdraft (a float). Three variables are created with the value of initialOverdraft; self.initialOverdraft,
        self.overdraftLimit and self.newLimit. They are created in the initialiser so that they can be accessed later on in other methods. There is also another variable,
        self.overdraft, which is a Boolean and will return True. 
        str:
            provides a string representation of the object, which greets the account holder and displays their available balance, actual balance, overdraft limit and 
            remaining overdraft available (i.e. which hasn't been used yet), via self.name, self.balance, self.overdraftLimit, self.balance, self.newLimit and 
            self.overdraftLimit respectively.
        deposit:
            calls the deposit method from BasicAccount via the super() function. The deposit method works in exactly the same way for the two classes. 
        withdraw:
            checks whether the given amount is valid (i.e. that there are sufficient funds to complete the transaction) by checking the balance plus overdraftLimit,
            then updates self.balance using amount if appropriate and prints a string representation of the transaction using self.name, amount, self.balance and 
            self.overdraftLimit. If there are insufficient funds, it prints a message stating that the withdrawal of the given amount cannot occur. This is managed 
            through exception handling.
        getAvailableBalance: 
            creates and then returns a new variable, availableBalance, which has the same value as self.balance + self.overdraftLimit and represents the available 
            funds in the account (that is to say, the account balance and any overdraft available). 
        getBalance:
            calls the getBalance method from BasicAccount via the super() function. The getBalance method works in exactly the same way for the two classes. However, it
            should be noted that, for PremiumAccount objects, there is now a difference between balance and available balance, as the latter takes into account the 
            available overdraft.
        printBalance:
            prints a string which displays the account balance, using self.balance and self.overdraftLimit, as well as the overdraft limit (self.newLimit) and
            remaining overdraft available (self.overdraftLimit).
        getName:
            calls and returns the getName method from BasicAccount via the super() function. 
        getAcNum:
            calls and returns the getAcNum method from BasicAccount via the super() function. 
        issueNewCard: 
            calls the issueNewCard method from BasicAccount via the super() function. 
        closeAccount: 
            almost identical to the closeAccount method from BasicAccount, except that the printed string is slightly different due to the calculations taking into 
            account overdrafts. 
        setOverdraftLimit:
            a method unique to this class. It takes a given float (newLimit) and gives this value to self.newLimit.

    """
    def __init__(self, acName: str, openingBalance: float, initialOverdraft: float):
        """
        Initialises the PremiumAccount object instance. 
        Parameters: self, acName (string) - the account holder's name, openingBalance (float) - the amount of money that the account is opened,
        initialOverdraft - the overdraft limit at the time of the opening of the bank account. 
        Returns: nothing
        """
        #Calls the __init__ method from the superclass, passing the parameters acName and openingBalance
        super().__init__(acName, openingBalance)
        #Assigns the argument for initialOverdraft to the variable initialOverdraft 
        self.initialOverdraft = initialOverdraft 
        #Assigns the argument for initialOverdraft to the variable overdraftLimit, in order to give the variable an initial value and tie it to the object instance. 
        self.overdraftLimit = initialOverdraft
        #Assigns the argument for initialOverdraft to the variable newLimit, in order to tie newLimit to the object instance.  
        self.newLimit = initialOverdraft
        #Calls the built-in function isinstance() to the variable overdraft. This will return False and thus assign False to the variable, as the account is a PremiumAccount object.
        self.overdraft = isinstance(self, BasicAccount)
    def __str__(self):
        """
        Provides a default string representation of the PremiumAccount object instance. 
        Parameters: self. None to be given by user.
        Returns: string
        """
        #This gives a welcome message to the customer including their name, balance, and overdraft limit
        return f"Welcome {self.name}. \n Your available balance is £{self.balance + self.overdraftLimit}. \n Your balance is {self.balance}. \n Your overdraft limit is {self.newLimit}. \n Your remaining overdraft is {self.overdraftLimit}."
    def deposit(self, amount: float): 
        """
        Deposit updates the balance of a BasicAccount object by the specified amount. The method is shared with the superclass BasicAccount
        and is called using the super() function. 
        Parameters: self, amount - a float to be deposited into the account. 
        Returns: nothing.
        """
        #Calls the deposit method from the superclass using the super() function
        super().deposit(amount)
    def withdraw(self, amount: float):
        """
        Withdraws the amount from the account if there are sufficient funds available in it and updates the account balance accordingly.
        Parameters: self, amount - a float to be removed from the account. 
        Returns: nothing 
        """
        #An exception handling block which raises and then throws a ValueError if amount is greater than the available balance of the account.
        try:
            #Checks whether there aren't sufficient funds to withdraw the amount and raises an exception if this is the case.
            if amount > self.balance + self.overdraftLimit:
                raise ValueError(f"Can not withdraw £{amount}.")
            else:
                #Updates the balance variable by subtracting the amount 
                self.balance = self.balance - amount 
                #Checks whether an overdraft has been used
                if self.balance + self.overdraftLimit - amount < 0:
                    #Updates the value of overdraftLimit by subtracting the amount of overdraft that has been used in order to withdraw that amount.
                    self.overdraftLimit = self.overdraftLimit - (self.overdraftLimit - (self.overdraftLimit + self.balance - amount))  
                    #Calls a built-in function, which will return True and assigns this value to the variable  
                    self.overdraft = isinstance(self, PremiumAccount) 
                #Prints an f-string to represent the transaction 
                print(f"{self.name} has withdrawn £{amount}. New balance is £{self.balance + self.overdraftLimit}.")
        #Throws and prints an error to alert the user that the transaction was unsuccessful
        except ValueError as e3:             
            print(e3)
    def getAvailableBalance(self):
        """
        Returns the balance which the customer has available to use. 
        Parameters: self. None to be given by user.
        Returns: availableBalance (float)
        """
        #Creates a variable which stores a float summing the object's balance and remaining available overdraft
        availableBalance = self.balance + self.overdraftLimit 
        return availableBalance 
    def getBalance(self):
        """
        Returns the balance of the account. The method is shared with the superclass BasicAccount
        and is called using the super() function. 
        Parameters: self. None to be given by user.
        Returns: self.balance (float)
        """
        #Calls the getBalance() method from the superclass and returns its value 
        return super().getBalance()
    def printBalance(self):
        """
        Prints to screen a message which shows the balance of the account, overdraft limit and remaining overdraft available. 
        Parameters: self. None to be given by user.
        Returns: nothing.
        """
        #Prints an f-string describing the current available balance, overdraft limit, and remaining overdraft.
        print(f"Your current balance is {self.balance + self.overdraftLimit}. \n Your current overdraft limit is £{self.newLimit}, and you have £{self.overdraftLimit} remaining from your overdraft.") #I don't think this is right 
    def getName(self):
        """
        Returns the name of the account holder as a string. The method is shared with the superclass BasicAccount
        and is called using the super() function.
        Parameters: self. None to be given by user.
        Returns: string version of self.name
        """
        #Calls the superclass method, which returns the account holder's name (acName). 
        return super().getName() 
    def getAcNum(self):
        """
        Returns the account number of the instance as a string. The method is shared with the superclass BasicAccount
        and is called using the super() function.
        Parameters: Self. None to be given by user. 
        Returns: number within a string which should also correspond to the number of accounts that have been opened.
        """
        #Calls the superclass method, which in turn returns the account number (acNum). 
        return super().getAcNum()
    def issueNewCard(self):
        """
        Creates a new (unique) 16-digit card number with an expiry date being 3 years to the month from now. This is done by iterating 
        randomly generated ints over a list of variables all set by default to 0, appending each variable to a list then converting that
        list into a string. The card number is then checked against a list of already issued cards; if it hasn't appeared before (which is 
        most likely the case), then the card number is just added to the list of issued cards for future reference. If it has, then the 
        function is called again using recursion. 
        This method is shared with the superclass BasicAccount and is called using the super() function. 
        Parameters: Self. None to be given by user.
        Returns: nothing. 
        """
        #Calls the superclass method 
        super().issueNewCard()
    def closeAccount(self):
        """
        A method which is called before deleting an object instance. The remaining balance is returned to customer via the 
        withdraw method if it is a positive value. 
        It differs slightly from the BasicAccount version of the method because it takes into account the overdraft. Therefore, it is 
        possible for the balance for a PremiumAccount to be negative.
        Parameters: Self. None to be given by user.
        Returns: a Boolean value.  
        """  
        #Checks whether there is a positive value left in the account. 
        if self.balance > 0:
            #Calls the withdraw() method on the account balance 
            self.withdraw(self.balance)
            return True
        #Checks whether there is nothing in the account - if so, the function returns True. 
        elif self.balance == 0:
            return True
        #The condition for the else statement is a negative value in the account, i.e. the account being overdrawn 
        else: 
            print(f"Can not close account due to customer being overdrawn by £{self.newLimit-self.overdraftLimit}")
            return False
    def setOverdraftLimit(self, newLimit: float):
        """
        This method allows a user to override and update overdraft limits for a particular account. 
        Parameters: Self, newLimit - a float which overrides previous limits (such as initialOverdraftLimit)
        Returns: nothing 
        """
        #Assigns the argument to the variable 
        self.newLimit = newLimit
        #Overrides the previous overdraft balance
        self.overdraftLimit = newLimit
