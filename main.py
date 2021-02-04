import ltc_reader
from datetime import datetime
from ltc_reader import get_curr_tc
import threading


#Startup Application
now = datetime.now()
fName = str(now)[:10] + ".txt"

f = open(fName, "w")
notes = ""

t = threading.Thread(target=ltc_reader.start_read_ltc())
t.start()

print("sssss")
#ltc_reader.start_read_ltc()

#Running gay

for i in range(1):
  n = input()
  
  if str(n) == "done":
    break
  
  now = get_curr_tc()
  print("TIME NOW: " + now)
  n = n + " | " + str(now) + "\n"
  notes += n
  print(n)


#Finished

f.write(notes)