almamater = open("alma_mater.txt","r")
# this was in schoology,free game
while True:
    line = almamater.readline()
    if len(line) == 0:
        break
    print(line,end ="")

almamater.close()