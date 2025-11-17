import random
import events
import missions
import flavortext
import saves
import stats

# Mainloop

game_over = False

while game_over == False:
   while day_count != mission_day_requirement:
      print (day_start_text)
      days_until_mission = mission_day_requirement-day_count

      if  multi_day_event == False:
          event_check = random_number = random.randint(1, 10)
          # Long event = 1, only morning = 2/3, only afternoon = 4/5, all day = 6/7, no event = 7-10
          if event_check == 8 or 9 or 10: 
             pass
          elif event_check == 6 or 7:
             all_day_event()
             pass
          elif event_check == 4 or 5:
             afternoon_event()
             pass
          elif event_checker == 2 or 3:
             morning_event()
             pass
          else:
             multi_day_event_1
             pass
      else:
         if multi_day_event_count == 1:
            multi_day_event_2()
            pass
         elif multi_day_event_count == 2:
            multi_day_event_3()
            pass
         else: 
            multi_day_event_4()
            pass
      print(day_end_text)
      day_count = day_count+1
   mission()
   day_count = 0

print(end_game_flavor)