# <!-- Let's create a program along the lines of the example above. This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish. Please have a look at the example below.

# Sample output
# hi
# Shall we continue? yes
# hi
# Shall we continue? oui
# hi
# Shall we continue? jawohl
# hi
# Shall we continue? no
# okay then -->

try:
    while True:
             message = int(input(" Hi\n shall we continue ? "))
             if message == 1234:
                 break
             print(" Ok! lets continue ")            
except:
     print(" ENter a valid numberic input")