#import ltc_reader
#ltc_reader.start_read_ltc()
from datetime import datetime

#Startup Application
f = open("notes.txt", "a")
notes = ""

#Running 

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