# Getting user input
sound_level = int(input("Please enter sound level in Noise Decibel level(dB)\n"))

# List of noises
Quiet_room = 40
Alarm_clock = 70
Petrol_lawnmower = 106
Jackhammer = 130

if sound_level > Jackhammer:
    print(
        "The sound level is higher than Jackhammer noise",
    )
elif sound_level == Jackhammer:
    print(
        "The sound level is same with Jackhammer noise",
    )
elif sound_level > Petrol_lawnmower:
    print(
        "The sound level is higher than Petrol lawnmower noise",
    )
elif sound_level == Petrol_lawnmower:
    print(
        "The sound level is same with Petrol lawnmower noise",
    )
elif sound_level > Alarm_clock:
    print(
        "The sound level is higher than Alarm clock  noise",
    )
elif sound_level == Alarm_clock:
    print(
        "The sound level is same with Alarm clock  noise",
    )
elif sound_level > Quiet_room:
    print(
        "The sound level is higher than Quiet room noise",
    )
else:
    print(
        "The sound level is same with Quiet room noise",
    )

## test case assertion 1
"""
sound_level = 130
print("The sound level is same with Jackhammer noise")
"""

## test case assertion 2
"""
sound_level = 65
print("The sound level is higher than Quiet room noise")
"""
