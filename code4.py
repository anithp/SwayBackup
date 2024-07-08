import shutil
import os
import datetime
import time

backup_path = r'C:\Users\Admin\OneDrive\Desktop\backup'
trades_path = r'D:\OdinIntegrated\Admin\OnLineBackup\BSE Equities\Trades'

while True:
	today = datetime.datetime.now()
	month = today.strftime("%m")
	day = today.strftime("%d")
	year = today.strftime("%Y")
	filename ="TR" + day + month + year + ".txt"
	FO_filename = "TR" +day + month + year + "BSE_SK" + ".txt"
	print(filename)
	if os.path.isfile(os.path.join(backup_path, FO_filename)):
		os.remove(os.path.join(backup_path, FO_filename))
	original = os.path.join(trades_path, filename)
	target = os.path.join(backup_path, filename)
	shutil.copyfile(original, target)	
	os.rename(os.path.join(backup_path, filename), os.path.join(backup_path, FO_filename))
	print("Successfully copied")
	time.sleep(60)
