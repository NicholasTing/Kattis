import math

test_cases = int(input())

candle_radius = 8

while test_cases != 0:

    location = input().split()
    x = float(location[0])
    y = float(location[1])

    total_candles = int(input())
    lit = False

    while total_candles != 0:
        candle_location = input().split()
        cx = float(candle_location[0])
        cy = float(candle_location[1])


        if ((x-cx) ** 2 + (y-cy) ** 2) <= candle_radius ** 2:
            lit = True

        total_candles -= 1

    if lit:
        print("light a candle")
    else:
        print("curse the darkness")

    test_cases -= 1
