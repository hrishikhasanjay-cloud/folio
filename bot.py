import requests
from datetime import date

def getweather(city="Thiruvananthapuram"):
    url=f"https://wttr.in/{city}?format=3"
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"Weather unavailable ({e})"

def get_quote():
    url="https://zenquotes.io/api/random"
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status()
        data=response.json()
        quote=data[0]["q"]
        author=data[0]["a"]
        return f'"{quote}" - {author}'
    except Exception as e:
        return f"Quote unavailable({e})"

def build_summary():
    today=date.today().strftime("%A,%d %B %Y")
    weather=getweather()
    quote=get_quote()
    summary=f"""
        PULSE -Daily Summary
        {today}
        WEATHER
            {weather}
        TODAY'S QUOTE
            {quote}
        """
    return summary
def run():
    summary=build_summary()
    print(summary)

    with open("summary.txt","w") as f:
        f.write(summary)
        print("pulse ran successfully.")
if __name__=="__main__":
    run()
