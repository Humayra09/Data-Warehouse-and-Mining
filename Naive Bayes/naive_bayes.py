import pandas as pd
df = pd.read_csv('play_tennis.csv')
print(df.head(10))
print("\nCount")
print(df.play.value_counts())

p_yes = 9 / 14
print("\nProbability of Playing Tennis "+str(p_yes))
p_no = 5 / 14
print("\nProbability of not Playing Tennis "+str(p_no))
print("\nPlaying Probabiltiy depending on outlook\n")
print(pd.crosstab(df.outlook,df.play))

p_overcast_no = (0/5)
p_overcast_yes = (4/9)

p_Rain_no = (2/5)
p_Rain_yes = (3/9)

p_Sunny_no = (3/5)
p_Sunny_yes = (2/9)
print("\nPlaying Probabiltiy depending on Temperature\n")
print(pd.crosstab(df.temp,df.play))

p_cool_no = (1/5)
p_cool_yes = (3/9)
p_Hot_no = (2/5)
p_Hot_yes = (2/9)
p_Mild_no = (2/5)
p_Mild_yes = (4/9)
print("\nPlaying Probabiltiy depending on Humidity\n")
print(pd.crosstab(df.humidity,df.play))

p_high_no = (4/5)
p_high_yes = (3/9)
p_normal_no = (1/5)
p_normal_yes = (6/9)
print("\nPlaying Probabiltiy depending on Wind\n")
print(pd.crosstab(df.wind,df.play))

p_strong_yes = 3/9
p_strong_no = 3/5
p_weak_yes = 6/9
p_weak_no =2/5

# problem 1
print('######Problem 1######\n')
#outlook = sunny, Temp = hot , humidity = high, wind = weak
p_yes_osunny_thot_hhigh_wweak = p_yes*p_Sunny_yes*p_Hot_yes*p_high_yes*p_weak_yes
print(p_yes_osunny_thot_hhigh_wweak)

p_no_osunny_thot_hhigh_wweak = p_no*p_Sunny_no*p_Hot_no*p_high_no*p_weak_no
print(p_no_osunny_thot_hhigh_wweak)

if(p_yes_osunny_thot_hhigh_wweak>p_no_osunny_thot_hhigh_wweak):
    print("Tennis will be Played")
else:
    print("Tennis will not be Played")


# problem 2
print('######Problem 2######\n')
#outlook = Overcast, Temp = cold , humidity = low, wind = weak
p_yes_oovercast_tcold_hlow_wweak = p_yes*p_overcast_yes*p_cool_yes*p_normal_yes*p_weak_yes
print(p_yes_oovercast_tcold_hlow_wweak)

p_no_oovercast_tcold_hlow_wweak = p_no*p_overcast_no*p_cool_no*p_normal_no*p_weak_no
print(p_no_oovercast_tcold_hlow_wweak)

if(p_yes_oovercast_tcold_hlow_wweak>p_no_oovercast_tcold_hlow_wweak):
    print("Tennis will be Played")
else:
    print("Tennis will not be Played")
