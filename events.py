import  main
import flavortext
import missions
import saves
import stats
import random

def all_day_event():
    event_pick =  random.randint(1, 5)
    if event_pick == 1:
        print(event_choice_text_1_all_day)
        event_choice  = input("Insert Your Response: [A,B,C]")
        if event_choice == "A":
            print(event_choice_text_1_all_day_response_1)
            event_choice  = input("Insert Your Response: [A,B,C]")
            if event_choice == "A":
                print(event_choice_text_1_all_day_response_1_1)
            if event_choice == "B":
                print(event_choice_text_1_all_day_response_1_2)
            if event_choice == "C":
                print(event_choice_text_1_all_day_response_1_3)

        elif event_choice == "B":
            print(event_choice_text_1_all_day_response_2)
            event_choice  = input("Insert Your Response: [A,B,C]")
            if event_choice == "A":
                print(event_choice_text_1_all_day_response_2_1)
            if event_choice == "B":
                print(event_choice_text_1_all_day_response_2_2)
            if event_choice == "C":
                print(event_choice_text_1_all_day_response_2_3)
        else:             
            print(event_choice_text_1_all_day_response_3)
            event_choice  = input("Insert Your Response: [A,B,C]")
            if event_choice == "A":
                print(event_choice_text_1_all_day_response_3_1)
            if event_choice == "B":
                print(event_choice_text_1_all_day_response_3_2)
            if event_choice == "C":
                print(event_choice_text_1_all_day_response_3_3)
    elif event_pick == 2:

    elif event_pick == 3:

    elif event_pick == 4:

    else:
