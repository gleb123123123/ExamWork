import random


def sort_array_in_place(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:

            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:

            mid += 1
        else:

            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


def calculate_sum(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum


def main():
    try:
        n = int(input("Введіть кількість елементів масиву (n): "))
        if n <= 0:
            print("Кількість елементів має бути більше 0.")
            return

        X = [random.randint(0, 2) for _ in range(n)]

        sort_array_in_place(X)

        arr_sum = calculate_sum(X)

        print(f"Відсортований масив: {X}")
        print(f"Сума елементів масиву: {arr_sum}")

    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")


if __name__ == "__main__":
    main()
