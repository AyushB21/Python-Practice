import pandas as pd
data ={"Name":['Ajay', 'Anil', 'Raj'],"Age":[25,26,29]}
df=pd.DataFrame(data)
df.to_csv("emp.csv")


