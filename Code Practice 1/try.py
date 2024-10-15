import pandas as pd
points_table = {'Team_':['MI', 'CSK', 'Devils', 'MI', 'CSK',
   'RCB', 'CSK', 'CSK', 'KKR', 'KKR', 'KKR', 'RCB'],
   'Rank_' :[1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year_' :[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Point_':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(points_table)
df.plot.hist('Team_')
