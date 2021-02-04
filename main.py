import ltc_reader
from datetime import datetime
from ltc_reader import get_curr_tc
from ltc_reader import stopAll
import threading

#Startup Application
now = datetime.now()
fName = str(now)[:10] + ".txt"
f = open(fName, "w")
notes = ""

ltc_reader.start_read_ltc()

#Running gay

while True:
  n = input()
  
  if str(n) == "done":
    stopAll()
    break
  
  now = get_curr_tc()
  n = n + " | " + str(now) + "\n"
  notes += n
  print("note: " + n)


#Finished

f.write(notes)