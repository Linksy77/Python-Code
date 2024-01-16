DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
           as the calling object (self).'''
        dnew =Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
           whether or not they are in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        ''' Changes the calling object so that it represents one day
            after the date it originally represented. (I.e. self.day
            will change, potentially changing self.month and self.year
            accordingly.
        '''
        self.day += 1
        if self.day > DAYS_IN_MONTH[self.month]:
            if self.month != 2:
                self.month += 1
                self.day = 1
            elif self.isLeapYear() == False:
                self.month += 1
                self.day = 1
            else:
                if self.day > 29:
                    self.month += 1
                    self.day = 1
            if self.month > 12:
                self.month = 1
                self.year += 1

    def yesterday(self):
        ''' Changes the calling object so that it represents one
            calendar day before the date it originally represented.
            (I.e. self.day will change, potentially changing
            self.month and self.year accordingly).
        '''
        self.day -= 1
        if self.day < 1:
            self.month -= 1
            if self.month == 0:
                self.month = 12
                self.day = DAYS_IN_MONTH[self.month]
                self.year -= 1
            elif self.month != 2:
                self.day = DAYS_IN_MONTH[self.month]
            else:
                if self.isLeapYear() == False:
                    self.day = DAYS_IN_MONTH[self.month]
                else:
                    self.day = 29

    def addNDays(self, N):
        ''' Changes the calling object so that it represents N
            calendar days after the date it originally represented.
            (Only handles nonnegative integer inputs N.)
        '''
        print(self)
        for i in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        ''' Changes the calling bject so that it represents N
            calendar days before the date it originally represented.
            (Only handles nonnegative integer inputs N.)
        '''
        print(self)
        for i in range(N):
            self.yesterday()
            print(self)

    def isBefore(self, d2):
        ''' Returns True if the calling object is a calendar date
            before the input named d2 (which will always be an
            object of type Date). Returns False if self and d2
            represent the same day, or if self is after d2. 
        '''
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def isAfter(self, d2):
        ''' Returns True is the calling object is a calendar date
            after the input named d2 (which will always be an
            object of type Date). Returns False if self and d2
            represent the same day, or if self is before d2.
        '''

        if self.isBefore(d2) == True:
            return False
        elif self.equals(d2) == True:
            return False
        else:
            return True

    def diff(self, d2):
        ''' Returns an integer representing the number of days
            between self and d2. (In essence: self - d2)
        '''
        newSelf = self.copy()
        newd2 = d2.copy()
        numOfDays = 0

        if newSelf.equals(newd2) == False:
            if newSelf.isBefore(newd2) == True:
                while newSelf.isBefore(newd2) == True:
                    newd2.yesterday()
                    numOfDays -= 1
            if newSelf.isAfter(newd2):
                while newSelf.isAfter(newd2) == True:
                    newd2.tomorrow()
                    numOfDays += 1
        return numOfDays

    def dow(self):
        ''' Returns a string that indicates the day of the week
            (dow) of the object (of type Date) that calls it.
            (Returns one of the following strings: "Monday",
            "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", or "Sunday".
        '''
        refDate = Date(11,9,2011)
        refDateWD = "Wednesday"

        rdSelfDiff = self.diff(refDate)
        
        if rdSelfDiff % 7 == 0:
            return refDateWD
        elif rdSelfDiff % 7 == 1:
            return "Thursday"
        elif rdSelfDiff % 7 == 2:
            return "Friday"
        elif rdSelfDiff % 7 == 3:
            return "Saturday"
        elif rdSelfDiff % 7 == 4:
            return "Sunday"
        elif rdSelfDiff % 7 == 5:
            return "Monday"
        elif rdSelfDiff % 7 == 6:
            return "Tuesday"
