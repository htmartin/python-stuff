
user_topic_sample['mo_year']=np.where(user_topic_sample['date']<='2017-09-30', '0917', '1017')

user_topic_sample['mo_year']=np.select([user_topic_sample['date'].between('2017-09-01','2017-09-30'),
                                        user_topic_sample['date'].between('2017-10-01','2017-10-31')], 
                                        ['0917','1017']
                                         ,'NaN')

user_topic_sample['in_0917']=np.where([user_topic_sample['mo_year']='0917', user_topic_sample['mo_year']='1017'], 
                                        ['1','0']
                                         ,'NaN')

user_topic_sample['in_0917']=np.where(user_topic_sample['mo_year']=='0917', '1','0')


user_topic_sample['in_1017']=np.where(user_topic_sample['mo_year']=='1017', '1','0')


conditions = [
    (user_topic_sample['in_0917'] == '1') & (user_topic_sample['in_1017'] == '0'),
    (user_topic_sample['in_0917'] == '0') & (user_topic_sample['in_1017'] == '1'),
    (user_topic_sample['in_0917'] == '1') & (user_topic_sample['in_1017'] == '1')]
choices = ['1', '0', '0']
user_topic_sample['gave_up'] = np.select(conditions, choices, 'NaN')

#    Can rewrite some of that with this sort of logic:
df['color'] = ['red' if x == 'Z' else 'green' for x in df['Set']]
#e.g.: 
user_topic_sample['in_0917']=['1' if x == '0917' else '0' for x in user_topic_sample['0917']]




df = pd.DataFrame({'Type':list('ABBC'), 'Set':list('ZZXY')})
df['color'] = np.where(df['Set']=='Z', 'green', 'red')
print(df)


df = pd.DataFrame({'Type':list('ABBC'), 'Set':list('ZZXY')})
conditions = [
    (df['Set'] == 'Z') & (df['Type'] == 'A'),
    (df['Set'] == 'Z') & (df['Type'] == 'B'),
    (df['Type'] == 'B')]
choices = ['yellow', 'blue', 'purple']
df['color'] = np.select(conditions, choices, default='black')
print(df)