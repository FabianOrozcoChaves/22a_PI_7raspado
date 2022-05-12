from datetime import datetime

#######################################################################

TXT_RESET = '\033[0m'
TXT_BLUE = '\033[34m'
TXT_RED = '\033[31m'
TXT_GREEN = '\033[32m'


#######################################################################

## Printing method to test class
# @param msg is the string to print
def printMsgTime(msg):
    # Imprime el día y la hora actuales + el mensaje enviado por parámetro
    time = datetime.now().strftime('%x - %X')
    print (f'{TXT_BLUE}[{time}]{TXT_RESET} {msg}')