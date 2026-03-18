def main():
    while True:

        print("\n" + "=" * 30)
        print("   Python Assignment 2 Menu")
        print("=" * 30)
        print("1. Students Marks (Lists)")
        print("2. Sum of digits (While loop)")
        print("3. Factorial of a number")
        print("4. Find the largest of three numbers")
        print("5. Sum of N numbers")
        print("6. Count number of digits")
        print("7. Prime numbers in a Tuple")
        print("8. Sort employee names")
        print("0. Exit")
        print("=" * 30)

        choice = input("Enter the question number: ")

        if choice == '1':

            stdmarks = [["Ali", 45], ["Noor", 80], ["Zaid", 60]]
            print(f"Initial list: {stdmarks}")

            stdmarks.insert(2, ["Huda", 75])

            stdmarks[2] = ["Mona", 90]

            passed_students = [s for s in stdmarks if s[1] >= 50]
            print(f"Passed Students: {passed_students}")

        elif choice == '2':

            num = int(input("Enter a positive integer: "))
            temp = num
            total = 0
            while temp > 0:
                total += temp % 10
                temp //= 10
            print(f"Sum of digits for {num} is: {total}")

        elif choice == '3':

            n = int(input("Enter a number: "))
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            print(f"Factorial of {n} is: {fact}")

        elif choice == '4':

            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            n3 = float(input("Enter third number: "))
            largest = max(n1, n2, n3)
            print(f"The largest number is: {largest}")

        elif choice == '5':

            N = int(input("Enter N: "))
            total_sum = sum(range(1, N + 1))
            print(f"Sum of first {N} numbers is: {total_sum}")

        elif choice == '6':

            n = abs(int(input("Enter an integer: ")))
            print(f"Number of digits: {len(str(n))}")

        elif choice == '7':

            limit = int(input("Enter upper limit to find primes: "))
            primes = []
            for num in range(2, limit + 1):
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)
            print(f"Prime numbers up to {limit}: {tuple(primes)}")

        elif choice == '8':

            names_str = input("Enter names separated by space: ")
            names_list = names_str.split()
            names_list.sort()
            print(f"Sorted names: {names_list}")

        elif choice == '0':
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 0 and 8.")


if __name__ == "__main__":
    main()