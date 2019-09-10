def divisible_by_4(y):
    return y % 4 == 0


def divisible_by_100(y):
    return y % 100 == 0


def divisible_by_400(y):
    return y % 400 == 0


def is_leap_year(year):
    # if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
    #     return True
    # if divisible_by_4(year):
    #     if divisible_by_100(year):
    #         if divisible_by_400(year):
    #             return True
    #         return False
    #     return True
    # return False
    #
    if divisible_by_4(year) and (not divisible_by_100(year) or divisible_by_400(year)):
        return True
    return False
