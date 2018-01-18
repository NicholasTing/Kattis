first_data = map(int,raw_input().split(":"))
second_data = map(int,raw_input().split(":"))

first_hour = first_data[0]
first_minutes = first_data[1]
first_seconds = first_data[2]

second_hour = second_data[0]
second_minutes = second_data[1]
second_seconds = second_data[2]

final_hour = 0
final_minutes = 0
final_seconds = 0

if second_hour > first_hour:

    if second_seconds >= first_seconds:
        final_seconds = second_seconds - first_seconds
    else:
        final_seconds = second_seconds + 60 - first_seconds

        if second_minutes != 0:
            second_minutes -= 1

        else:
            if second_hour != 0:
                second_hour -= 1
                second_minutes = 59

            else:
                second_hour = 23
                second_minutes = 59

    if second_minutes >= first_minutes:
        final_minutes = second_minutes - first_minutes

    else:
        final_minutes = second_minutes + 60 - first_minutes

        if second_hour != 0:
            second_hour -= 1

        else:
            second_hour = 23

    if second_hour >= first_hour:
        final_hour = second_hour - first_hour

    else:
        final_hour = second_hour + 24 - first_hour

else:
    second_hour = second_hour + 24
    if second_seconds >= first_seconds:
        final_seconds = second_seconds - first_seconds
    else:
        final_seconds = second_seconds + 60 - first_seconds

        if second_minutes != 0:
            second_minutes -= 1

        else:
            if second_hour != 0:
                second_hour -= 1
                second_minutes = 59

            else:
                second_hour = 23
                second_minutes = 59

    if second_minutes >= first_minutes:
        final_minutes = second_minutes - first_minutes

    else:
        final_minutes = second_minutes + 60 - first_minutes

        if second_hour != 0:
            second_hour -= 1

        else:
            second_hour = 23

    if second_hour >= first_hour:
        final_hour = second_hour - first_hour

    else:
        final_hour = second_hour + 24 - first_hour



print('{0:02d}:{1:02d}:{2:02d}'.format(final_hour,final_minutes,final_seconds))
