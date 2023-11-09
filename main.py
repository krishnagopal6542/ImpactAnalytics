def probability_of_attendance(prev_attendance, missing_attendance, number_of_days, miss_flag, ans, last_day_miss, day):
    if missing_attendance >= 4:
        miss_flag = True
        return ans, last_day_miss

    if number_of_days == day:
        if not miss_flag and prev_attendance[-1] == 'A':
            last_day_miss += 1
        ans += 1
        return ans, last_day_miss

    # Recursively explore both possibilities:
    ans, last_day_miss = probability_of_attendance(prev_attendance + 'P', 0, number_of_days + 1, miss_flag, ans,last_day_miss, day)
    ans, last_day_miss = probability_of_attendance(prev_attendance + 'A', missing_attendance + 1, number_of_days + 1,miss_flag, ans, last_day_miss, day)

    return ans, last_day_miss


def calculate_probability(day):
    # Initialize counters
    ans, last_day_miss = 0, 0
    ans, last_day_miss = probability_of_attendance("", 0, 0, False, ans, last_day_miss, day)

    return last_day_miss, ans


if __name__ == '__main__':
    days = 10
    last_day_missed, res = calculate_probability(days)
    print(f'{last_day_missed}/{res}')
