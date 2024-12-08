import pandas as pd


# BIST 30 hisseleri sembolleri
bist30_symbols = [
    'AKBNK.E', 'ARCLK.E', 'ASELS.E', 'BIMAS.E', 'EREGL.E', 'FROTO.E', 'GARAN.E',
    'KCHOL.E', 'KRDMD.E', 'KOZAA.E', 'KOZAL.E', 'PGSUS.E', 'SAHOL.E', 'SISE.E',
    'TAVHL.E', 'TCELL.E', 'THYAO.E', 'TKFEN.E', 'TTKOM.E', 'TUPRS.E', 'VAKBN.E', 'YKBNK.E'
]
for j in range(17,20):
    for i in range(1, 13):
        a = str(i)
        b= str(j)
        if a != "10" and a != "11" and a != "12":
            isim = "PP_GUNSONUFIYATHACIM.M.20" + b + "0" + a + ".csv"
            file_path = 'C:/Users/yusuf/Desktop/veri/' + isim
            df = pd.read_csv(file_path, sep=';')

            # İlgili sütunları seç

            df_filtered = df[df.iloc[:, 1].isin(bist30_symbols)][[df.columns[0], df.columns[1], df.columns[22]]]

            # Sonuçları kaydet
            son = "C:/Users/yusuf/Desktop/tem veri/"+"20"+ b + "0" + a +"BIST30_Kapanis_Fiyatlari.csv"
            df_filtered.to_csv(son, index=False)

            df_filtered.head()
        else:
            isimi = "PP_GUNSONUFIYATHACIM.M.20" + b + a + ".csv"
            file_path = 'C:/Users/yusuf/Desktop/veri/' + isimi
            df = pd.read_csv(file_path, sep=';')

            # İlgili sütunları seç

            df_filtered = df[df.iloc[:, 1].isin(bist30_symbols)][[df.columns[0], df.columns[1], df.columns[22]]]

            # Sonuçları kaydet
            son = "C:/Users/yusuf/Desktop/tem veri/" + "20" + b + a + "BIST30_Kapanis_Fiyatlari.csv"
            df_filtered.to_csv(son, index=False)

            df_filtered.head()






