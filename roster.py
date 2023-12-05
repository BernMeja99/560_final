# Link to unc roster
#https://goheels.com/sports/mens-basketball/roster
import pandas as pd
roster = [ 'Davis', 'Ryan', 'Bacot' ]
player = {"Last Name": roster}
data = pd.DataFrame(roster)
print(data)

