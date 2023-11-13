# 1) Xử lý dữ liệu cafef source cung cấp hằng ngày - Ta lấy Giá cổ phiếu 
# Note: Sử dụng Jupiter Note Booko thì trực quan hơn nhưng mỗi lần mở lâu

'''
Trong folder cần có 3 file csv lấy từ Cafef như sau:
    CafeF.HNX.Upto11.05.2023
    CafeF.HSX.Upto11.05.2023
    CafeF.UPCOM.Upto11.05.2023
Note: Ta thấy các file có dạng CafeF.UPCOM.Upto[Ngay-Thang-Nam]
'''

import pandas as pd


#Bước 0: Nhập ngày lấy data
data_ngay ='10.11.2023'    #'CafeF.HNX.Upto{data}.csv'.format(data =data_ngay)
fil_number = 20231110      #Formgay thang trong file csv DDDD-MM-DD 

#Bước 1: Load Dataset vào Dataframe - Sử dụng  format method  
HNX_df = pd.read_csv('CafeF.HNX.Upto{data}.csv'.format(data =data_ngay))
HOSE_df = pd.read_csv('CafeF.HSX.Upto{data}.csv'.format(data =data_ngay))
UPCOM_df = pd.read_csv('CafeF.UPCOM.Upto{data}.csv'.format(data =data_ngay))

HNX_df['San'] ='HNX'
HOSE_df['San'] ='HOSE'
UPCOM_df['San'] ='UPCOM'

#Bước 2: Nối 3 Dataframe bằng append method 
HNX_df.info()

print(HOSE_df)
print(HNX_df)

#In the Future .append method depricate in Pandas 2.x. Must use concat method
#df = HOSE_df.append(HNX_df, ignore_index=True).append(UPCOM_df, ignore_index=True)
df = pd.concat([HOSE_df,HNX_df,UPCOM_df], ignore_index=True)
print(df)


data = df[df['<DTYYYYMMDD>'] == fil_number]
data = data[['<Ticker>','<Close>','San', '<DTYYYYMMDD>']].sort_values(by='<Ticker>')
print(data)

#Bước 3: Đổi tên cột xuất file cho đẹp 
data.rename(columns={'<Ticker>':'Ticker', '<Close>':'Close','<DTYYYYMMDD>':'Date Time'}, inplace=True)
print(data)


data.to_csv('DataGia_{data}.csv'.format(data =data_ngay), index=False)

print('So luong ma CK duoc lay', len(data))