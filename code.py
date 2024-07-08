import shutil
import os 
import datetime
import time

while True:
    today = datetime.datetime.now()
    month = today.strftime("%m")
    day = today.strftime("%d")
    filename = month + day + "TRD" + ".txt"
    CM_filename = month + day + "TRD" + "CM" + "_SK" + ".txt"
    FO_filename = month + day + "TRD" + "FO" + "_SK" + ".txt"
    print(filename)
    if os.path.isfile(os.path.join(r'C:\Users\Admin\OneDrive\Desktop\backup', FO_filename)):
        os.remove(os.path.join(r'C:\Users\Admin\OneDrive\Desktop\backup', FO_filename))
    original = os.path.join(r'D:\OdinIntegrated\Admin\OnLineBackup\NSE Derivatives\Trades',  filename)
    target =os.path.join(r'C:\Users\Admin\OneDrive\Desktop\backup', filename)
                         
    shutil.copyfile(original, target)
    os.rename(os.path.join(r'C:\Users\Admin\OneDrive\Desktop\backup', filename), os.path.join(r'C:\Users\Admin\OneDrive\Desktop\backup', FO_filename))
    print("Successfully copied")
    time.sleep(60)

#C:\OdinIntegrated\Admin\OnLineBackup\NSE Equities\Trades
#C:\OdinIntegrated\Admin\OnLineBackup\NSE Derivatives\Trades


