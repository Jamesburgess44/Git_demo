class Alarm_clock:
    def __init__(self):
        self.alarm_is_on = False
        self.current_time = "12PM"
        self.alarm_time = ""

    def on_off_cycle(self):
        if self.alarm_is_on == False:
            self.alarm_is_on = True
            print("alarm is now on")
        elif self.alarm_is_on == True:
            self.alarm_is_on = False
            print("The alarm is off now")

    def set_current_time(self):
        self.current_time = input("What would you like to set the current time to?")
        print(f'The current time was set to {self.current_time}')

    def set_alarm_time(self):
        self.alarm_time = input("what time do you want to set the alarm for")
        print(f'the alarm is set for {self.alarm_time}')