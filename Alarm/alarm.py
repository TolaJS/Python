"""
SIMPLE PYTHON ALARM CLOCK

Description = "Simple python alarm clock designed to ring a set time between the current time 
and the end of the day(23:59)"
Name = alarm.py
Author = Tola Shobande (tolajs)
"""

from playsound import playsound
from datetime import datetime as dt


def alarm(date_time):
    """
    alarm(date_time) ->
        Takes in a datetime argument. Calculates difference in seconds between
        the current time and date_time parameter. Sound is played when difference
        is less than or equal to zero.
    """
    while (date_time - dt.now()).total_seconds() > 0:
        pass

    # Play sound for 30 seconds
    for _ in range(30):
        playsound("alarm.wav")


def entry(hour, min):
    """
    entry(hour, min) ->
        Checks if parameters hour and min are valid entries using try and
        except block for value errors. Returns True if the entry is valid
        and False otherwise.
    """
    try:
        hour = int(hour)
        min = int(min)
        current_hr = dt.now().hour

        if current_hr <= hour <= 23:
            # If param hour same as current_hr, param min > current minute <= 59
            if current_hr == hour and 59 >= min > dt.now().minute:
                return True
            elif current_hr < hour and 0 <= min <= 59:
                return True
            else:
                print("Invalid minute entry")
                return False
        print("Invalid hour entry")
        return False

    except ValueError:
        print("Invalid entry, please input a valid hour and minute (24HR FORMAT)")
        return False


def main():

    print("THIS ALARM WILL ONLY WORK FOR ANY VALID TIME BEFORE TOMORROW!\n")
    print("To set an alarm, enter a valid hour and minute ahead of the current time")

    while True:
        hour = input("Hour: ")
        minute = input("Minute: ")

        if entry(hour, minute):
            date_time = dt.now().replace(
                hour=int(hour), minute=int(minute), second=0, microsecond=0
            )
            alarm(date_time)
            break


if __name__ == "__main__":
    main()
