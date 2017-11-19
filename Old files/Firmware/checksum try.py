import array
message = "3,339,264,339,325,261,339,316,269,308,350,314,395,339,265,340,325,262,340,315,268,309,351,312,396,".encode()
byteMessage = array.array('b', message)
print(byteMessage)
print(len(byteMessage))

i = 0
checkSum = 0

while i < (len(byteMessage)-1):
    checkSum ^= int(byteMessage[i])
    #print(checkSum)
    #print(i, ": ")
    #print(message[i], "\n")
    i += 1

print(checkSum)
print(chr(checkSum))
print(message.decode()[len(message)-1])

if chr(checkSum) == message.decode()[len(message)-1]:
    print('Correct')
    #Store data into buffer
else:
    print('Not Correct')
    #Send request for resend of data to Arduino
