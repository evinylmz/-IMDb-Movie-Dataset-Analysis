# Gerekli kütüphaneleri içe aktar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Görselleştirme ayarları
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (12, 8)
sns.set_palette("husl")

# Aşama 1: Veri Yükleme ve Hazırlık
def load_and_prepare_data():
    """
    IMDb veri setini yükler ve temel veri hazırlığı yapar
    """
    try:
        # Veri setini yükle
        df = pd.read_csv('imdb_top_1000.csv')
        print("Veri seti başarıyla yüklendi!")
    except:
        print("Veri seti bulunamadı. Lütfen dosya yolunu kontrol edin.")
        return None
    
    # Temel bilgileri göster
    print(f"Veri seti boyutu: {df.shape}")
    print("\nİlk 5 satır:")
    print(df.head())
    
    print("\nSütunlar:")
    print(df.columns.tolist())
    
    print("\nVeri tipleri:")
    print(df.dtypes)
    
    print("\nEksik değerler:")
    print(df.isnull().sum())
    
    # Veri temizleme
    df = clean_data(df)
    
    return df

def clean_data(df):
    """
    Veriyi temizler ve yeni sütunlar oluşturur
    """
    # Kopya oluştur
    df_clean = df.copy()
    
    # Year sütununu temizle (sadece sayısal değerleri al)
    df_clean['year_clean'] = pd.to_numeric(df_clean['year'], errors='coerce')
    
    # Runtime sütununu temizle (dakikaya çevir)
    df_clean['runtime_clean'] = df_clean['runtime'].str.extract(r'(\d+)').astype(float)
    
    # Rating sütununu temizle
    df_clean['rating_clean'] = df_clean['rating'].replace({
        'NOT RATED': np.nan,
        'UNRATED': np.nan,
        'APPROVED': np.nan,
        'PASSED': np.nan
    })
    
    # IMDB puanını ve oy sayısını temizle
    df_clean['imdb_rating_clean'] = df_clean['imdbRating']
    df_clean['imdb_votes_clean'] = df_clean['imdbVotes']
    
    # Tür sütununu temizle
    df_clean['genre_clean'] = df_clean['genre']
    
    return df_clean

# Aşama 2: Keşifsel Veri Analizi (EDA)
def exploratory_data_analysis(df):
    """
    Veri setini keşfederek temel istatistikleri ve ilişkileri analiz eder
    """
    print("\n" + "="*50)
    print("KEŞİFSEL VERİ ANALİZİ (EDA)")
    print("="*50)
    
    # Temel istatistikler
    print("\nTemel İstatistikler:")
    numeric_cols = ['metacritic', 'imdb_rating_clean', 'imdb_votes_clean', 'runtime_clean']
    print(df[numeric_cols].describe())
    
    # Sayısal değişkenler arasındaki korelasyon
    print(f"\nSayısal değişkenler arası korelasyon:")
    correlation_matrix = df[numeric_cols].corr()
    print(correlation_matrix)
    
    # En yüksek puanlı filmler
    print("\nEn yüksek puanlı 10 film:")
    top_rated = df.nlargest(10, 'imdb_rating_clean')[['title', 'imdb_rating_clean', 'genre_clean', 'director']]
    print(top_rated)
    
    # En çok oy alan filmler
    print("\nEn çok oy alan 10 film:")
    most_voted = df.nlargest(10, 'imdb_votes_clean')[['title', 'imdb_votes_clean', 'imdb_rating_clean', 'director']]
    print(most_voted)
    
    # Yıllara göre film sayısı
    print("\nYıllara göre film dağılımı (ilk 10 yıl):")
    yearly_counts = df['year_clean'].value_counts().sort_index().dropna()
    print(yearly_counts.head(10))
    
    return correlation_matrix

# Aşama 3: Veri Görselleştirme
def create_visualizations(df, correlation_matrix):
    """
    Veriyi görselleştirerek içgörüler oluşturur
    """
    print("\n" + "="*50)
    print("VERİ GÖRSELLEŞTİRME")
    print("="*50)
    
    # NaN değerleri temizle
    df_viz = df.dropna(subset=['imdb_rating_clean', 'runtime_clean', 'metacritic'])
    
    # 1. IMDB Puan Dağılımı
    plt.figure(figsize=(15, 12))
    
    plt.subplot(2, 3, 1)
    plt.hist(df_viz['imdb_rating_clean'], bins=30, edgecolor='black', alpha=0.7)
    plt.title('IMDB Puan Dağılımı')
    plt.xlabel('IMDB Puanı')
    plt.ylabel('Film Sayısı')
    plt.grid(True, alpha=0.3)
    
    # 2. Yıllara Göre Film Sayısı
    plt.subplot(2, 3, 2)
    yearly_counts = df['year_clean'].value_counts().sort_index().dropna()
    # Son 50 yılı göster
    recent_years = yearly_counts.tail(50)
    plt.plot(recent_years.index, recent_years.values, marker='o', linewidth=2, markersize=3)
    plt.title('Son 50 Yılda Film Sayısı')
    plt.xlabel('Yıl')
    plt.ylabel('Film Sayısı')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    # 3. Meta Skor vs IMDB Puanı
    plt.subplot(2, 3, 3)
    plt.scatter(df_viz['metacritic'], df_viz['imdb_rating_clean'], alpha=0.6)
    plt.title('Meta Skor vs IMDB Puanı')
    plt.xlabel('Meta Skor')
    plt.ylabel('IMDB Puanı')
    plt.grid(True, alpha=0.3)
    
    # 4. En Popüler Türler
    plt.subplot(2, 3, 4)
    # Türleri ayır ve say
    all_genres = df['genre_clean'].str.split(', ').explode().dropna()
    genre_counts = all_genres.value_counts().head(10)
    genre_counts.plot(kind='bar')
    plt.title('En Popüler 10 Film Türü')
    plt.xlabel('Tür')
    plt.ylabel('Film Sayısı')
    plt.xticks(rotation=45)
    
    # 5. En Başarılı Yönetmenler (en az 5 filmi olan)
    plt.subplot(2, 3, 5)
    director_stats = df.groupby('director').agg({
        'imdb_rating_clean': ['mean', 'count']
    }).round(2)
    director_stats.columns = ['mean_rating', 'movie_count']
    # En az 5 filmi olan yönetmenler
    qualified_directors = director_stats[director_stats['movie_count'] >= 5]
    top_directors = qualified_directors.nlargest(10, 'mean_rating')
    top_directors['mean_rating'].plot(kind='bar')
    plt.title('En Yüksek Puan Ortalamasına Sahip 10 Yönetmen\n(En az 5 film)')
    plt.xlabel('Yönetmen')
    plt.ylabel('Ortalama IMDB Puanı')
    plt.xticks(rotation=45)
    
    # 6. Süre vs IMDB Puanı
    plt.subplot(2, 3, 6)
    plt.scatter(df_viz['runtime_clean'], df_viz['imdb_rating_clean'], alpha=0.6)
    plt.title('Film Süresi vs IMDB Puanı')
    plt.xlabel('Süre (dakika)')
    plt.ylabel('IMDB Puanı')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # 7. Korelasyon Isı Haritası
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=0.5, fmt='.3f')
    plt.title('Değişkenler Arası Korelasyon Isı Haritası')
    plt.tight_layout()
    plt.show()
    
    # 8. Yıllara Göre Ortalama IMDB Puanı
    plt.figure(figsize=(12, 6))
    yearly_avg_rating = df.groupby('year_clean')['imdb_rating_clean'].mean().dropna()
    # Son 50 yılı göster
    recent_ratings = yearly_avg_rating.tail(50)
    plt.plot(recent_ratings.index, recent_ratings.values, 
             marker='o', linewidth=2, markersize=4)
    plt.title('Son 50 Yılda Ortalama IMDB Puanı')
    plt.xlabel('Yıl')
    plt.ylabel('Ortalama IMDB Puanı')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Aşama 4: Raporlama
def generate_report(df):
    """
    Analiz sonuçlarını özetleyen bir rapor oluşturur
    """
    print("\n" + "="*50)
    print("ANALİZ RAPORU")
    print("="*50)
    
    # Temel istatistikler
    total_movies = len(df)
    avg_rating = df['imdb_rating_clean'].mean()
    avg_votes = df['imdb_votes_clean'].mean()
    avg_runtime = df['runtime_clean'].mean()
    
    print(f"Toplam Film Sayısı: {total_movies:,}")
    print(f"Ortalama IMDB Puanı: {avg_rating:.2f}")
    print(f"Ortalama Oy Sayısı: {avg_votes:,.0f}")
    print(f"Ortalama Film Süresi: {avg_runtime:.1f} dakika")
    
    # En iyi film
    best_movie_idx = df['imdb_rating_clean'].idxmax()
    best_movie = df.loc[best_movie_idx]
    print(f"\nEn Yüksek Puanlı Film: {best_movie['title']} ({best_movie['imdb_rating_clean']})")
    
    # En çok oy alan film
    most_voted_idx = df['imdb_votes_clean'].idxmax()
    most_voted_movie = df.loc[most_voted_idx]
    print(f"En Çok Oy Alan Film: {most_voted_movie['title']} ({most_voted_movie['imdb_votes_clean']:,.0f} oy)")
    
    # En popüler tür
    all_genres = df['genre_clean'].str.split(', ').explode().dropna()
    most_popular_genre = all_genres.value_counts().index[0]
    print(f"En Popüler Tür: {most_popular_genre}")
    
    # En üretken yönetmen
    most_prolific_director = df['director'].value_counts().index[0]
    print(f"En Çok Film Üreten Yönetmen: {most_prolific_director}")
    
    # Yıllara göre trend
    valid_years = df['year_clean'].dropna()
    recent_year = valid_years.max()
    oldest_year = valid_years.min()
    
    recent_year_avg = df[df['year_clean'] == recent_year]['imdb_rating_clean'].mean()
    oldest_year_avg = df[df['year_clean'] == oldest_year]['imdb_rating_clean'].mean()
    
    print(f"\nPuan Trendi:")
    print(f"En eski yıldaki ortalama puan ({int(oldest_year)}): {oldest_year_avg:.2f}")
    print(f"En yeni yıldaki ortalama puan ({int(recent_year)}): {recent_year_avg:.2f}")
    
    # Süre ve puan ilişkisi
    runtime_corr = df['runtime_clean'].corr(df['imdb_rating_clean'])
    print(f"\nFilm Süresi ve IMDB Puanı Arasındaki Korelasyon: {runtime_corr:.3f}")
    
    # Meta skor ve IMDB puanı ilişkisi
    meta_corr = df['metacritic'].corr(df['imdb_rating_clean'])
    print(f"Meta Skor ve IMDB Puanı Arasındaki Korelasyon: {meta_corr:.3f}")
    
    # Önemli bulgular
    print("\n" + "="*50)
    print("ÖNEMLİ BULGULAR")
    print("="*50)
    print("1. Film süresi ile IMDB puanı arasındaki ilişki analiz edildi.")
    print("2. En popüler film türleri belirlendi.")
    print("3. Yıllar içinde film sayısı ve puan trendleri incelendi.")
    print("4. Meta skor ile IMDB puanı arasındaki korelasyon hesaplandı.")
    print("5. En başarılı yönetmenler (en az 5 filmi olan) listelendi.")

# Ana fonksiyon
def main():
    """
    Ana analiz işlemlerini yürütür
    """
    print("IMDb Film Veri Seti Analizi Başlatılıyor...")
    
    # Aşama 1: Veri Yükleme ve Hazırlık
    df = load_and_prepare_data()
    
    if df is None:
        print("Veri yüklenemedi. Program sonlandırılıyor.")
        return
    
    # Aşama 2: Keşifsel Veri Analizi
    correlation_matrix = exploratory_data_analysis(df)
    
    # Aşama 3: Veri Görselleştirme
    create_visualizations(df, correlation_matrix)
    
    # Aşama 4: Raporlama
    generate_report(df)
    
    print("\n" + "="*50)
    print("ANALİZ TAMAMLANDI")
    print("="*50)

# Programı çalıştır
if __name__ == "__main__":
    main()