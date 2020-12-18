from covid import Covid
covid = Covid()
daily_case = covid.get_status_by_country_name("enter_the_country_here")
for x in daily_case:
    print(x,';', daily_case[x])
