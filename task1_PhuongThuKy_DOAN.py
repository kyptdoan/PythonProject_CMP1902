# This program prompts the user to input integer numbers, saves to a list and prints
# the amount, sum, mean, max, min and prime numbers of the list.
class Numbers():
    """
    A class to represent a list of integers
    ...
    Attributes:
        list: list
            a list contains all the integers the user input
        counts: int
            the number of integers in the list
        sum: int
            sum value of integers in the list
        mean: int
            mean value of the list
        max: int
            the max value of the list
        min: int
            the min value of the list
        prime_numbers: list
            a list contains all the prime numbers of the list
    ...
    Methods:
        count_numbers(): count numbers in the list
        print_numbers(): print the list 
        calculate_sum(): calculate the sum value of integers in the list
        calculate_mean(): calculate the mean value of the list
        find_max(): find the max value of the list
        find_mean(): find the mean value of the list
        find_prime_numbers(): find all the prime numbers in the list
    """
    def __init__(self, list_of_number):
        """
        Constructs all the necessary attributes for a numbers object

        Args:
            list_of_number (list): a list contains all the intergers the user input
        """
        self.list = list_of_number
        self.counts = 0
        self.sum = 0
        self.mean = 0
        self.max = 0
        self.min = 0
        self.prime_numbers = []
        
    def count_numbers(self):
        """
        Count numbers in the list

        Returns:
            int: the numbers count of the list
        """
        self.counts = len(self.list)
        
        return self.counts
    
    def print_numbers(self):
        """
        Print the list 
        """
        print("They are ", end=' ')
        
        # Loop through each integer in the list
        for num in self.list:
            # Print them out in a single line, separated by a " ' " 
            print(num, sep = ',', end = ' ')
    
    def calculate_sum(self):
        """
        calculate the sum value of integers in the list

        Returns:
            int: the sum value of the list
        """
        # Temporary variable for the sum value
        sum = 0
        # Loop through each integer in the list
        for num in self.list:
            # Add them to the temporary sum value
            sum += num
            
        # Save the sum value
        self.sum = sum
        
        return self.sum      
    
    def calculate_mean(self):
        """
        calculate the mean value of the list

        Returns:
            int: the mean value of the list
        """
        # Find the counts using 'count_numbers' method
        Numbers.count_numbers(self)
        
        # Find the sum using 'calculate_sum' method
        Numbers.calculate_sum(self)
        
        # Calculate the mean
        self.mean = self.sum / self.counts
        
        return self.mean
    
    def find_max(self):
        """
        Find the max value of the list

        Returns:
            int: the max value of the list
        """
        # At the beginning, assume that the first element of the list is the max value
        max_of_nums = self.list[0]
        
        # Loop through each element in the list
        for number in self.list:
            # Check if the current element is bigger than value in 'max_of_num'
            if (number > max_of_nums):
                # If yes, update the value of the current list's element to the 'max_of_nums'
                max_of_nums = number
        
        self.max = max_of_nums

        return self.max
    
    def find_min(self):
        """
        Find the min value of the list

        Returns:
            int: the min value of the list
        """
        
        # At the beginning, assume that the first element of the list is the min value
        min_of_num = self.list[0]
        
        # Loop through each element in the list
        for number in self.list:
             # Check if the current element is smaller than value in 'max_of_num'
            if (number < min_of_num):
                # If yes, update the value of the current list's element to the 'min_of_nums'
                min_of_num = number
        
        self.min = min_of_num
        
        return self.min

    def find_prime_numbers(self): 
        """
        A method to find prime numbers in the list and save them into another list
        
        Returns:
            list: a list contains all the prime numbers in the list
        """
        def check_prime_number(number):
            """
            A method to check if an integer is a prime number

            Args:
                number (int): the integer to be checked

            Returns:
                bool: True if the integer is a prime number, False if it is not
            """
            
            # An integer is not a prime number if it is smaller than 2
            # Because 2 is the smallest integer
            if number < 2:
                return False
            
            # If it is equal to 2 or bigger than 2
            # Loop through each integer from 2 to (the number value - 1)
            for i in range (2, number):
                # If the integer can divide any other integer to remain 0, it is not a prime number
                if (number % i == 0):
                    return False
            
            # After the list is looped over and the program has not been returend False
            # The integer is a prime number, returns the program to True
            return True
        
        # find prime number in the list using check_prime_number method and save them in self.prime_numbers
        # Loop through each number in the list
        for number in self.list:
            # Check if it is a prime number by passing it into the "check_prime_number" method
            if (check_prime_number(number) == True):
                # If it is, append it into the "prime_number_list"
                self.prime_numbers.append(number)
        
        return self.prime_numbers
    
def main():
    """
    The main function in which the user is prompted to input integers and the class's methods are called
    """
    
    print("Type in as many integer as you want. If you finished, press Enter.")
    
    # a list to contain the user's integers
    list_of_numbers = []
    
    # Erroneous input handling when the user does not type in an integer.
    while True:
        # A variable to temporarily hold the input value
        temp = input("Type in an integer: ")
        
        # When the user press 'Enter', they finish their input
        # and the infinite loop is broken to move to the calculation steps
        if temp == '':
            break
        
        try:
            num = int(temp)
            list_of_numbers.append(num)
        except:
            print("Invalid input. Please enter integers.")
    
    # Handling the empty list when the user does not type in anything
    # which leads to 'Divideby0' error in 'calculate_mean' method.
    if (len(list_of_numbers) == 0):
        print("You have not typed in any integer.")
    else:
        numbers = Numbers(list_of_numbers)
        print(f"There are: {numbers.count_numbers()} numbers in the list.")
        print(f"They are: {list_of_numbers}.")
        print(f"Sum of these numbers is: {numbers.calculate_sum()}.")
        print(f"Mean of these numbers is: {numbers.calculate_mean()}.")
        print(f"The largest number in the list is: {numbers.find_max()}.") 
        print(f"The smallest number in the list is: {numbers.find_min()}.")
        print(f"Prime numbers in the list are: {numbers.find_prime_numbers()}.")   
    
if __name__ == "__main__":
    main()