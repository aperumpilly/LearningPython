logContent= "True"
with open("E:\eventlog-save.txt") as fileRead :
    with open("E:\EventError.log","a") as fileWrite:
        while logContent:
            logContent = fileRead.readline()
            if "Information" not in logContent:
             fileWrite.write(logContent)
        print("Completed")
