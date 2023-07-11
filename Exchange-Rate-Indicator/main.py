import yfinance as yf

def doviz_donusumu():
    
    base_currency = "TRY"  # Dönüştürme yapılacak para birimi (Türk Lirası)
    target_currencies = ["USD", "EUR", "GBP"]  # Hedef para birimleri (Dolar, Euro, Sterlin)

    for currency in target_currencies:
        ticker = f"{currency}{base_currency}=X"  # Yahoo Finance sembolü
        data = yf.download(tickers=ticker, period="1d")
        if not data.empty:
            rate = data["Close"][-1]  # Türk Lirası karşısındaki değeri al
            print(f"1 {currency} = {rate} {base_currency}")
        else:
            print(f"Kur bilgisi bulunamadı: {currency}")

doviz_donusumu()
