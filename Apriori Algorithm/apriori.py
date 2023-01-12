import numpy as np
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
df=pd.read_csv('GroceryStoreDataSet.csv', header=None)
df.columns=['items']
print(df)
txn_arr=df['items'].values
# print(txn_arr[0:10])
txn_list=[]
for i in range(0, len(txn_arr)):
    txn_list.append(txn_arr[i].split(','))
print(txn_list[0:10])
enc=TransactionEncoder()
txn_list_enc=enc.fit(txn_list).transform(txn_list)
print(txn_list_enc[0:10])
txn_df_enc=pd.DataFrame(data=txn_list_enc, columns=enc.columns_, dtype= int)
print(txn_df_enc)
df_support=apriori(txn_df_enc, use_colnames=True, min_support=0.2)
print(df_support.sort_values(by='support', ascending=False))
df_confidence=association_rules(df_support, metric='confidence', min_threshold=0.3)
print(df_confidence.sort_values(by='confidence', ascending=False))
df_lift=association_rules(df_support, metric='lift', min_threshold=1)
print(df_lift.sort_values(by='lift', ascending=False))
df_lift=association_rules(df_support, metric='lift', min_threshold=0)
print(df_lift[df_lift['lift']<1])
