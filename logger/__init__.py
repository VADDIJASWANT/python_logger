import os
from datetime import datetime

class Logger:
    def __init__(self, log_file_name, heading):
        self.log_file_name = log_file_name if log_file_name.endswith('.txt') else log_file_name + '.txt'
        self.heading = heading
        self.logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Logs')
        os.makedirs(self.logs_dir, exist_ok=True)
        self.log_path = os.path.join(self.logs_dir, self.log_file_name)
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w', encoding='utf-8') as f:
                pass

    def Write(self, message):
        now = datetime.now().strftime('%d-%b-%Y %H:%M:%S')
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(f"{now} | {self.heading}\n{message}\n\n")