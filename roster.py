# Link to unc roster
#https://goheels.com/sports/mens-basketball/roster
import pandas as pd
#Player Stats
#Height is in inches
#Weight is in Pouns
player = {"Last Name": [ 'Davis', 'Ryan', 'Bacot' ],
          "First Name": ["RJ","Cormac", "Armando"],
          "Height": [72, 77,83],
          "Weight": [180,195,240]}

data = pd.DataFrame(player)

#BMI = weight in kg / height in meters
data["BMI"] = (data["Weight"]/2.205)/ ((data["Height"]/39.37)**2)
print(data)

