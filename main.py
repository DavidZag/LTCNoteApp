#import ltc_reader
#ltc_reader.start_read_ltc()
from datetime import datetime

#Startup Application
now = datetime.now()
fName = str(now)[:10] + ".txt"

f = open(fName, "w")
notes = ""

#Running gay

while True:
  n = input()
  
  if str(n) == "done":
    break

  now = datetime.now()
  n = n + " | " + str(now) + "\n"
  notes += n
  print(n)


#Finished

f.write(notes)