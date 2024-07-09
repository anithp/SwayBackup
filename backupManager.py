import shutil
import os
import datetime
import time

class BackupManager:
    def __init__(self, backup_path, trades_path):
        self.backup_path = backup_path
        self.trades_path = trades_path
    
    def generate_filenames(self):
        today = datetime.datetime.now()
        formatted_date = today.strftime("%Y%m%d")
        
        filename_bsecm = f"TradeBook_BSECM{formatted_date}.CSV"
        filename_nsecm = f"TradeBook_NSECM{formatted_date}.TXT"
        filename_nsefo = f"TradeBook_NSEFO{formatted_date}.TXT"
        
        return filename_bsecm, filename_nsecm, filename_nsefo
    
    def perform_backup(self):
        filename_bsecm, filename_nsecm, filename_nsefo = self.generate_filenames()
        
        # List of original and target file paths
        original_files = [
            os.path.join(self.trades_path, filename_bsecm),
            os.path.join(self.trades_path, filename_nsecm),
            os.path.join(self.trades_path, filename_nsefo)
        ]
        
        target_files = [
            os.path.join(self.backup_path, filename_bsecm),
            os.path.join(self.backup_path, filename_nsecm),
            os.path.join(self.backup_path, filename_nsefo)
        ]
        
        # Remove existing files in backup_path
        for target_file in target_files:
            if os.path.isfile(target_file):
                os.remove(target_file)
        
        # Perform the backup
        for i in range(len(original_files)):
            shutil.copyfile(original_files[i], target_files[i])
            print(f"Successfully copied {original_files[i]} to {target_files[i]}")
        
    def run(self):
        while True:
            self.perform_backup()
            time.sleep(60)

# Paths for backup and trades
backup_path = r'C:\Users\Admin\OneDrive\Desktop\JAINAM_BACKUP'
trades_path = r'C:\Users\Admin\OneDrive\Desktop\MULTITRADE BACKUP'

# Create an instance of BackupManager
backup_manager = BackupManager(backup_path, trades_path)

# Start running the backup process
backup_manager.run()
