from time import time
import subprocess
class Tools:
    @staticmethod
    def get_unix_time():
        return int(time())
    
    @staticmethod
    def execute_rf_command(rf_id, new_state):
        res = subprocess.Popen([
            "./kspRfTool",
            str(rf_id),
            str(new_state)
        ])
        try:
            res.wait(3)
        except:
            print("W: timeout!")