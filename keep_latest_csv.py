import re
import os
from datetime import datetime

def keep_latest_csv(p):
    csv_files = [f for f in os.listdir(p) if f.endswith('.csv')]

    latest_file = None
    latest_date = None

    for csv_file in csv_files:
        date_str = re.search(r'\d{4}-\d{2}-\d{2}', csv_file)
        if date_str:
            date = datetime.strptime(date_str.group(), '%Y-%m-%d').date()
            
            if latest_date is None or date > latest_date:
                latest_date = date
                latest_file = csv_file

    for csv_file in csv_files:
        if csv_file != latest_file:
            os.remove(os.path.join(p, csv_file))

    return latest_file