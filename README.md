# -IMDb-Movie-Dataset-Analysis
IMDb Top 1000 Film Analizi Projesi
Bu proje, IMDb'nin en iyi 1000 filminden oluşan veri setinin kapsamlı analizini içeren bir veri bilimi projesidir.

📊 Proje Hakkında
IMDb Top 1000 veri setini kullanarak film endüstrisi hakkında detaylı analizler ve görselleştirmeler yapılmıştır. Proje, veri temizleme, keşifsel veri analizi (EDA), veri görselleştirme ve raporlama aşamalarını içermektedir.

🎯 Proje Amaçları
IMDb'nin en iyi 1000 filminin demografik analizi

Film özellikleri ile puanlar arasındaki ilişkilerin incelenmesi

Yıllara göre film trendlerinin analizi

Yönetmen ve tür bazlı performans değerlendirmesi

Görsel veri keşfi ile içgörü elde etme

📁 Veri Seti
Dosya: imdb_top_1000.csv

İçerdiği Önemli Sütunlar:

title: Film başlığı

year: Yayın yılı

genre: Film türü

director: Yönetmen

imdbRating: IMDB puanı

imdbVotes: Oy sayısı

runtime: Süre

metacritic: Metacritic skoru

🛠️ Kullanılan Teknolojiler
Python 3.x

Pandas: Veri işleme ve analiz

NumPy: Sayısal hesaplamalar

Matplotlib: Temel görselleştirme

Seaborn: İstatistiksel görselleştirme

Jupyter Notebook: Etkileşimli analiz ortamı

📊 Analiz Başlıkları
1. Veri Ön İşleme ve Temizleme
Eksik veri analizi

Veri tipi dönüşümleri

Anomali tespiti ve temizleme

2. Keşifsel Veri Analizi (EDA)
Temel istatistikler

Korelasyon analizi

Dağılım analizleri

Trend analizleri

3. Görselleştirmeler
IMDB puan dağılımı

Yıllara göre film sayısı

Meta skor vs IMDB puanı ilişkisi

En popüler film türleri

En başarılı yönetmenler

Film süresi vs puan ilişkisi

Korelasyon ısı haritası

4. İçgörüler ve Bulgular
Film süresi ile puan arasındaki ilişki

En popüler türler ve yönetmenler

Zaman içinde film kalitesi trendleri

Farklı rating sistemleri arasındaki korelasyon

🚀 Kurulum ve Çalıştırma
Gereksinimler
bash
pip install pandas numpy matplotlib seaborn jupyter
Çalıştırma
bash
# Script olarak çalıştırma
python imdb_analysis.py

# Jupyter Notebook'ta çalıştırma
jupyter notebook
📈 Önemli Bulgular
Film Süresi & Puan İlişkisi: Uzun filmlerin genellikle daha yüksek puan aldığı gözlemlenmiştir.

Tür Dağılımı: Dram ve aksiyon filmleri en popüler türler arasındadır.

Zaman Trendi: Son yıllarda film sayısı artarken, ortalama puanlarda belirgin bir değişiklik yoktur.

Yönetmen Etkisi: Bazı yönetmenlerin filmleri tutarlı şekilde yüksek puanlar almaktadır.

📝 Proje Yapısı
text
imdb-analysis/
├── imdb_analysis.py          # Ana analiz scripti
├── imdb_top_1000.csv         # Veri seti
├── requirements.txt          # Gereksinimler
├── README.md                 # Proje dokümantasyonu
└── images/                   # Görselleştirme çıktıları
👥 Katkıda Bulunma
Bu depoyu fork edin

Feature branch oluşturun (git checkout -b feature/amazing-feature)

Değişikliklerinizi commit edin (git commit -m 'Add some amazing feature')

Branch'inize push edin (git push origin feature/amazing-feature)

Pull Request oluşturun
