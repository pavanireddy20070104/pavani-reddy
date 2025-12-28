#creating a simple traffic light simulator
#ask user to enter the colour of traffic signal(red,green,yellow)
traffic_signal=input("give the colour of traffic signal:")
#giving instructions according to colour of traffic signal
if traffic_signal=="red":
    print("STOP!")
elif traffic_signal=="yellow":
    print("Prepare to stop")
elif traffic_signal=="green":
    print("You can go")
else:
    print("Wrong input!")
