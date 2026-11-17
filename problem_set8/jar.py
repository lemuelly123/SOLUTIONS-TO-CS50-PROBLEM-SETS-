class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __valid(self, value, operation):
        if not isinstance(value, int):
            raise ValueError(f"Enter whole numbers for {operation}")
        if value <= 0:
            raise ValueError(f"Number of cookies to {operation} must be greater than zero")
        return value
        
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if not isinstance(new_capacity, int):
            raise ValueError("Enter whole numbers for capacity")
        if new_capacity < 0:
            raise ValueError(f"Capacity cannot be negative")
        self._capacity = new_capacity
    
    def __str__(self):
        if self.size == 0:
            return "Empty cookie jar"
        return f"Number of cookies are: {"🍪" * self.size}"

    def deposit(self, n):
        deposit = self.__valid(n, "deposit")
        if deposit > self.capacity:
            raise ValueError("Jar capacity exceeded")
        self.size += deposit
        return self.size

    def withdraw(self, n):
        print(self.size)
        withdraw = self.__valid(n, "withdraw")
        if n > self.size:
            raise ValueError(
                "Number of cookies to withdraw exceed the maximum amount of cookies available"
            )
        if self.capacity == 0:
            raise ValueError("Cannot withdraw from empty jar")
        self.size -= withdraw
        return self.size
    
def main():
    jar1 = Jar()
    jar2 = Jar(10)
    jar1.deposit(12)
    jar1.withdraw(8)
    print(jar1)
    print(jar2)


if __name__ == "__main__":
    main()