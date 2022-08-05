from alarm_clock import Alarm_clock

alarm_one = Alarm_clock()
alarm_two = Alarm_clock()

print(alarm_one.current_time)
alarm_one.set_current_time()
print(alarm_one.current_time)



print("")
print("")
print(alarm_two.current_time)


alarm_two.on_off_cycle()
alarm_two.on_off_cycle()
alarm_two.on_off_cycle()







