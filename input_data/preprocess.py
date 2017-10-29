import pandas as pd

input_filename  = 'input-ibaraki-utf8.csv'
output_filename = 'filtered.csv'
raw_csv = pd.read_csv(input_filename)

input_data = raw_csv.assign(
    南側道路あり=lambda x: (x['前面道路の方位区分'] == '南').astype(int),
    不整形地=lambda x: (x['形状区分'] != '_').astype(int),
    総価格=lambda x: (x['地積'] * x['Ｈ２９価格'])
)

filtered_data = input_data[(input_data['地積'] < 250) & (input_data['駅距離'] > 1) & (input_data['駅距離'] < 2000)]

print('writing to', output_filename, ':', filtered_data.shape[0], 'rows')
filtered_data[['地積', '不整形地', '南側道路あり', '駅距離', '建ぺい率', '総価格']].to_csv(output_filename, index=False)
