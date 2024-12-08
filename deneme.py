

for j in range(14,24):
    for i in range(1, 13):
        a = str(i)
        b= str(j)
        if a != "10" and a != "11" and a != "12":
            isim = "PP_GUNSONUFIYATHACIM.M.20" + b + "0" + a + ".csv"
            print(isim)
        else:
            isimi = "PP_GUNSONUFIYATHACIM.M.20" + b + a + ".csv"
            print(isimi)


# CSV dosyasını oku
file_path = 'C:/Users/yusuf/Desktop/veri/' + isim
df = pd.read_csv(file_path, sep=';')


# İlgili sütunları seç

df_filtered = df[df.iloc[:, 1].isin(bist30_symbols)][[df.columns[0], df.columns[1], df.columns[21]]]

# Sonuçları kaydet
df_filtered.to_csv('C:/Users/yusuf/Desktop/veri/BIST30_Kapanis_Fiyatlari.csv', index=False)

df_filtered.head()


son = "C:/Users/yusuf/Desktop/veri/"+"20"+ b + a +"BIST30_Kapanis_Fiyatlari.csv"
            df_filtered.to_csv(son, index=False)



import os
import glob

# Dosya yolu ve dosya adları
folder_path = '/path/to/your/csv/files/'  # CSV dosyalarının bulunduğu klasör yolu
all_files = glob.glob(os.path.join(folder_path, '*.csv'))  # Tüm CSV dosyalarını al

# Tüm CSV dosyalarını okuyup tek bir DataFrame'e birleştir
df_list = []
for file in all_files:
    df = pd.read_csv(file, delimiter=',')  # Dosyayı virgülle ayırmak için delimiter parametresi kullanılır
    df_list.append(df)

# Tüm DataFrame'leri birleştir
combined_df = pd.concat(df_list, ignore_index=True)

# Tarih sütununu datetime formatına dönüştür
combined_df['Tarih'] = pd.to_datetime(combined_df['Tarih'])

# Hisse ismine göre gruplayın ve işlemleriniz için devam edin
grouped_df = combined_df.groupby('Sembol')

# Gruplandıktan sonra örnek olarak ilk hisse için veriyi göstermek için
print(grouped_df.get_group('HisseAdi'))

# Sonuçları başka bir CSV dosyasına yazdırabilirsiniz
grouped_df.to_csv('combined_data.csv')

