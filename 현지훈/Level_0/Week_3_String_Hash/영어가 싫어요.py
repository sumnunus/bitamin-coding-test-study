def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))

    return int(numbers)


numbers_input = "onetwothreefourfivesixseveneightnine"
print(solution(numbers_input))