import os
from dotenv import load_dotenv
from keep_latest_csv import keep_latest_csv
from download_csv import download_csv
from flask import Flask, jsonify, request
import pandas as pd

load_dotenv()
share_url = os.getenv("SHARE_URL")

download_directory = os.path.abspath("data/") 
os.makedirs(download_directory, exist_ok=True)


download_csv(share_url, download_directory)
recent_csv = keep_latest_csv(download_directory)

print(recent_csv)

CSV_FILE_PATH = f"data/{recent_csv}"
print(CSV_FILE_PATH)

app = Flask(__name__)

@app.route('/share_price', methods = ['GET'])
def get_last_updated_price():
       
        
        # symbol = request.args.get('symbol').upper()
# 
        # if not symbol:
            # return jsonify({"error": "Symbol parameter is required"}), 400
        
        if not os.path.exists(CSV_FILE_PATH):
            return jsonify({"error": "CSV file not found"}), 404

        df = pd.read_csv(CSV_FILE_PATH, on_bad_lines="skip")
        # print(df)

        # stock_data = df

        # if stock_data.empty:
        #     return jsonify({"error": "Symbol not found"}), 404

        # last_updated_price = stock_data.iloc[0]['LAST_UPDATED_PRICE']
        # security_name = stock_data.iloc[0]['SECURITY_NAME']

        # return jsonify({
        #     "symbol": symbol,
        #     "security_name": security_name,
        #     "last_updated_price": last_updated_price
        # })

        df_as_dict = df.to_dict(orient='list')

        return jsonify(df_as_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)