# Link to unc roster
#https://goheels.com/sports/mens-basketball/roster
import pandas as pd
player = {"Last Name": [ 'Davis', 'Ryan', 'Bacot' ],
          "First Name": ["RJ","Cormac", "Armando"],
          "Height": [6,6.5,6.11],
          "Weight": [180,195,240]}
data = pd.DataFrame(player)
print(data)

