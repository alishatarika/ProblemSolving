import os
if(not os.path.exists("data")):
 os.mkdir("Data")
for i in range(0,100):
 os.mkdir(f"data/Day{i+1}")

