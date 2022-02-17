# The first line of the input gives the number of test cases, T. T test cases follow.
# Each test case consists of two lines.
# The first line of each test case contains two integers:
# integer N, the number of candy bags, and M, the number of kids.
# The next line contains N non-negative integers C1,C2,…,CN
# representing array C, where the i-th integer
# represents the number of candies in the i-th bag.


def main():
    number_of_test_cases = int(input())
    pieces_of_candy_remaining = []
    while number_of_test_cases > 0:
        number_of_candy_bags, number_of_kids = tuple(
            [int(num) for num in input().split(' ')])
        candy_bags = [int(num) for num in input().split(' ')]
        assert number_of_candy_bags == len(candy_bags)
        pieces_of_candy_remaining.append(sum(candy_bags) % number_of_kids)
        number_of_test_cases -= 1

    for i in range(len(pieces_of_candy_remaining)):
        print(f'Case #{i + 1}: {pieces_of_candy_remaining[i]}')


if __name__ == '__main__':
    main()
