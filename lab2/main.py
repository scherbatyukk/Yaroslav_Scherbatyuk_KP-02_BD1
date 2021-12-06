from controller import Control_Input_Output
from model import do_Database_Changing
from viewer import find_Parameters

while True:
    request = find_Parameters(1)
    if (request == "0"):
        print("Finished")
        exit(666)
    else:
        parameters = request.split()
        Control_Input_Output(parameters)
