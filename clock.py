import time
# A fake comment
# Add to dev
seconds = 50
minutes = 59
hours = 12
ampm = 1
text_ampm = ""

while 1==1:
    print(hours,":",minutes,":",seconds,text_ampm)
    seconds = seconds +1 
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes = minutes +1

    if minutes == 60:
        minutes = 0
        hours = hours +1
    
    if hours == 13:
        hours = 1
        ampm = ampm +1

    if ampm == 1:
        text_ampm = "am"
    
    if ampm == 2:
        ampm = 0
        text_ampm = "pm"
        
    # Alarm    
    if hours == 12 and minutes == 59 and seconds == 59:
        print("alarm")

