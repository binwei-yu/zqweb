# SI 507 - Lab 3

# We've provided a little bit of structure for some code that will help you start working on a representation of an extremely simplified financial system.
# For now, there are only 3 currencies, it's easy to simply set up banks, and while it is possible to convert one currency to another (e.g. dollars to pounds, or pounds to yuan, or yuan to dollars), it's not possible to deposit money in dollars to a bank that keeps yuan.

# In this lab, you'll be:
# - using your knowledge of object-oriented programming to write some code that will make it possible to convert an instance of Dollar that e.g. represents 4 dollars to Yuan or to Pounds, although we've written most of the conversion logic already!
# - using your knowledge of object-oriented programming and Python overall (and Google searching/reading abilities!) to write some code that will allow you to create an instance of a class Bank that follows particular specifications, including the ability to deposit money to the bank (as long as you follow the deposit rules).

# Here lives the code, including all boilerplate code provided for you to work from!

# Read the instructions carefully, and think about what you need to understand to write some code.

# We've provided some sample code that uses the class definitions you're working on.

# When you are done, you can submit this code -- lab3_code.py -- to the Gradescope assignment Lab 3.

# You can also test yourself at ANY point you are working on this by submitting to the autograder on Gradescope, in order to find out what tests you pass.
# Remember, passing tests is necessary (but not necessarily sufficient) for credit on this lab. You can re-submit to the Lab 3 gradescope assignment as many times as you want prior to the deadline. (See late policies re: submitting after the deadline.)
# We don't grade assignments that don't run -- make sure that even if your code doesn't do everything you hoped it would, it does run!

## [STEP 1]
# Define classes to represent currencies, as follows:

## We have provided the definition of class Currency, the parent class of all currencies.
# Note that the class Currency includes a method conversion, which will allow any instance of a sub-class to be converted to another currency sub-class.

# Given this definition of Currency to refer to, you should implement three subclasses of class Currency, to represent 3 different curriences: Dollar, Yuan, and Pound.

# Ensure each of your subclasses have the class variable(s), constructor and string method they need. You will need to infer from reading the
# code in the class Currency what you need in order to correctly implement the subclasses.
# The string method for each subclass should print something like the following:
#           "7 Pounds", "10 Yuan", "1 Pound"

# HINT: This does not involve writing very much code, but make sure you understand how the subclasses work with their parent class Currency.

class Currency:
    
    unit_name = "currency" # class variable because it's true of ALL instances of this class (unless overridden in a subclass)
    
    def __init__(self, value):
        self.value = value
        self.base_rate = 1 #always

    def conversion(self, result_currency_reference):
        if(type(self) == Pound):
            rate = Pound.rate
        elif (type(self) == Yuan):
            rate = Yuan.rate
        elif (type(self) == Dollar):
            rate = Dollar.rate
        else:
            return "Can't convert. Please enter a valid currency."

        #Conversion
        value_in_currency = self.value * rate
        value_at_reference_rate = value_in_currency / result_currency_reference.rate
        return result_currency_reference(value_at_reference_rate)

# Complete class Dollar with class variable(s) and a constructor method. Ensure that the conversion method in its parent class will work for it!
# Class Dollar's exchange rate should be 20 units of Currency.
class Dollar(Currency):
        rate = 20
        unit_name = "Dollar"
        def __init__(self, value):
            super().__init__(value)

        def __str__(self):
            if (self.value > 1):
                return "{} Dollars".format(self.value)
            else:
                return "{} Dollar".format(self.value)

class Pound(Currency):
        rate = 15
        unit_name = "Pound"
        def __init__(self, value):
            super().__init__(value)

        def __str__(self):
            if (self.value > 1):
                return "{} Pounds".format(self.value)
            else:
                return "{} Pound".format(self.value)

class Yuan(Currency):
        rate = 8
        unit_name = "Yuan"
        def __init__(self, value):
            super().__init__(value)

        def __str__(self):
            return "{} Yuan".format(self.value)

## The below code provided should work when your class definitions are complete. Of course, you should also submit to the autograder to see your test results.

# TODO @ INSTRS

## [STEP 2]
# Define code for a class Bank, as follows.

# First, define a constructor for class Bank that accepts as input a name for the bank, a reference to the currency of the bank (HINT: which is one of the class you implemented above) and an initial value the bank holds. The default for the initial value should be 0.
# The constructor for class Bank should then initialize instance variables.
# An instance variable called "name" should be populated with the bank's name. An instance variable called "unit" should be populated with the reference to the bank's currency, and an instance variable called "current_account" should be assigned the bank's initial value.
# "current_account" is also the variable that is keeping track of the total amount in the bank. IT SHOULD be in the units the bank use.
# HINT: the "current_account" instance variable is not a number, but a Currency. So instead of 10 it will be 10 Pounds (or whatver the unit is). So make sure you construct an instance of the a Currency, rather than just saving the value.

# Second, define a string method for class Bank that represents each instance of class Bank as follows, replacing all <> values with the appropriate instance variable values: "<NAME> Bank holds the <CURRENCY> currency and currently holds <VALUE> of <CURRENCY>"

# Third, define a method in class Bank called deposit, to manage deposits to the Bank.
# A bank can only accept deposits of the bank's currency. For example, a bank that holds Yuan cannot accept a deposit in Dollars.
# This method should accept as input an instance of a currency, which has some value.
# The method should check whether this deposit input is of an acceptable currency for this bank. HINT: check out the built-in Python function isinstance or type!
# If the deposit is the acceptable currency, then the method should add the value of this deposit to the bank's value, and should return a string "successful deposit". If it is NOT the acceptable currency, it should not do anything except return the string "ERROR: cannot deposit that currency."

class Bank():

    def __init__(self, name, unit, value = 0):
        self.unit = unit
        self.name = name
        self.current_account= self.unit(value)

    def __str__(self):
            return "{} Bank holds the {} currency and currently holds {} of {}".format(self.name, self.unit.unit_name, self.current_account.value, self.unit.unit_name)

    def deposit(self, cur):
        if(type(cur) == self.unit):
            self.current_account.value += cur.value
            return "successful deposit"
        else:
            return "ERROR: cannot deposit that currency."


# The below code provided should work when your class definitions are complete. Of course, you should also submit to the autograder to see your test results.

# TODO @ INSTRS

jpMorgan = Bank("J.P.Morgan", Dollar, 1)
barclays = Bank("Barclays", Pound, 1)
bank_of_china = Bank("Bank of China", Yuan, 1)

dollar = Dollar(1)
pound = Pound(1)
yuan = Yuan(1)


'''
jpMorgan = Bank("J.P.Morgan", Dollar, 1)
barclays = Bank("Barclays", Pound, 1)
bank_of_china = Bank("Bank of China", Yuan, 1)

dollar = Dollar(1)
pound = Pound(1)
yuan = Yuan(1)

print(yuan.conversion(Pound))
0.5333333333333333 Pound

print(pound.conversion(Pound))
1.0 Pound

print(pound.conversion(Dollar))
0.75 Dollar

print(jpMorgan.current_account.value)
1

print(jpMorgan.deposit(dollar))
'successful deposit'

print(jpMorgan.current_account.value)
2

print(jpMorgan.deposit(pound))
'ERROR: cannot deposit that currency.'


'''
