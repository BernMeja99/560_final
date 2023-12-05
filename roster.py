# Link to unc roster
#https://goheels.com/sports/mens-basketball/roster
import pandas as pd
#UNC Men's Basketball Player Stats (10 Players)
player = {"Last Name": [ 'Davis', 'Ryan', 'Bacot', 'High', 'Cadeau', 'Trimble', 'Wojcik','Washington', 'Lebo', 'Okonkwo'],
          "First Name": ["RJ","Cormac", "Armando", "Zayden", "Elliot", "Seth", "Paxson","Jalen", "Creighton", "James"],
          "Height": [72, 77,83,81,73,75,77,82,73,80],
          "Weight": [180,195,240,225,180,195,195,230,180,240]}

data = pd.DataFrame(player)

#BMI = weight in kg / height in meters
data["BMI"] = (data["Weight"]/2.205)/ ((data["Height"]/39.37)**2)

print(data)

data.to_csv("bmi.csv")

