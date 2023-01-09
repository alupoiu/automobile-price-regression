import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()
# print(new_df)
new_df['miles'] = new_df['miles'].str.replace('miles', '')
new_df['miles'] = new_df['miles'].str.replace(',', '')
new_df['price'] = new_df['price'].str.replace(',', '')
# new_df['listing_type'] = ''
# new_df.loc['Used' in new_df['model'], 'listing_type'] = 'Used'
# new_df.loc['Used' in new_df['miles'], 'listing_type'] = 'Used'
# len(new_df.index)
# new_df['listing_type'] = new_df['model'].apply(lambda x: 'Used' if 'Used' in x else 'Certified')

new_df['listing_type'] = new_df['model'].apply(lambda x: 'Used' if 'Used' in x else 'Certified')
new_df['year'] = new_df['model'].str.extract('(\d+)')
# new_df['model'] = new_df['model'].str.split('Civic ',1)[2]
# new_df['model'] = new_df['model'].str.slice(str.index('Civic '))
new_df['model'] = new_df['model'].map(lambda x: x.split('Civic ',1)[1])

print(new_df)

# x = "Used 2018 Honda Civic EX"
# y = 'Civic '
# print(x.index(y))

new_df.to_csv('processed-data.csv', index=False)
