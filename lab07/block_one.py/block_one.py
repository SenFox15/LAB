import pickle

def analyze_os_market_share():
    

    os_data = {
        "Windows": {"2018": 0.35, "2019": 0.34, "2020": 0.32, "2021": 0.31, "2022": 0.30},
        "macOS": {"2018": 0.15, "2019": 0.16, "2020": 0.17, "2021": 0.18, "2022": 0.19},
        "Android": {"2018": 0.70, "2019": 0.72, "2020": 0.71, "2021": 0.73, "2022": 0.74},
        "iOS": {"2018": 0.12, "2019": 0.13, "2020": 0.14, "2021": 0.13, "2022": 0.12},
        "Linux": {"2018": 0.02, "2019": 0.03, "2020": 0.025, "2021": 0.04, "2022": 0.05},
        "Chrome OS": {"2018": 0.01, "2019": 0.015, "2020": 0.02, "2021": 0.025, "2022": 0.03},
        "Others": {"2018": 0.05, "2019": 0.04, "2020": 0.035, "2021": 0.03, "2022": 0.02}
    }


    
    avg_shares = {os: sum(years.values()) / len(years) for os, years in os_data.items()}
    print("\nAverage Market Share:")
    for os, avg_share in avg_shares.items():
        print(f"{os}: {avg_share:.2f}")

   
    min_max_years = {}
    for os, years in os_data.items():
        min_year = min(years, key=years.get)
        max_year = max(years, key=years.get)
        min_max_years[os] = {"min": min_year, "max": max_year}

    print("\nYears with Min/Max Market Share:")
    for os, years in min_max_years.items():
        print(f"{os}: Min - {years['min']}, Max - {years['max']}")

   
    print("\nMarket Share in 2020:")
    for os, years in os_data.items():
        print(f"{os}: {years.get('2020', 'N/A')}") 

    
    growth_os = []
    for os, years in os_data.items():
        start_share = years['2018']
        end_share = years['2022']
        if (end_share - start_share) / start_share * 100 > 20:
            growth_os.append(os)

    print("\nOS with >20% Growth:")
    print(growth_os)


 
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(os_data, f)
        print("\nData saved to data.pickle")

        with open("data.pickle", "rb") as f:
            loaded_data = pickle.load(f)
            print("\nData loaded from data.pickle:")
            print(loaded_data)  

    except Exception as e:
        print(f"Error during pickle operation: {e}")


analyze_os_market_share()