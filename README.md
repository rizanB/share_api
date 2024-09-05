## Fetch Last Updated Price for Stocks

Fetches security name and last updated price for stocks.

### Install Dependencies

```
pip install -r requirements.txt
```

### Running

```
python app.py
```

### Usage

GET Endpoint: 

```
http://127.0.0.1:5000/share_price?symbol=nabil
```

Response:
```
{
  "last_updated_price": 595.0,
  "security_name": "Nabil Bank Limited",
  "symbol": "NABIL"
}

```

### Depends on
- Selenium
- pandas
- Flask