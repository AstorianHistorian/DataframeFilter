import pandas as pd

df = pd.read_csv("pp-complete.csv",sep=',',names=['TUI', 'Price', 'DateOfTransfer','Postcode',
   'PropertyType','Old/New','Duration','PAON','SAON','Street','Locality','Town/City',
   'District','Country','PPDCategoryType','RecordedStatus'])
df = df.loc[df.duplicated(subset=['Street', 'PAON', 'Locality','Town/City','District','Country'], keep='last')].drop_duplicates(subset=['Street', 'PAON', 'Locality','Town/City','District','Country'])
df.to_csv("pp-complete-multiple-transactions.csv", sep=',', encoding='utf-8')
