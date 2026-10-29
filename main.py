# Desert AgriTech - Smart Irrigation Simulation
# Soil moisture-based automated irrigation control

def sulama_kontrolu(nem_orani):
    print(f"Mevcut Toprak Nem Oranı: %{nem_orani}")
    
    # Kurak bölge / çöl şartları için kritik nem eşiği: %30
    if nem_orani < 30:
        print("⚠️ Uyarı: Toprak çok kuru! Sulama pompası AKTİFLEŞTİRİLDİ. 💧")
    elif 30 <= nem_orani <= 70:
        print("✅ Toprak nemi ideal seviyede. Sistem beklemede.")
    else:
        print("💧 Toprak yeterince ıslak. Sulama kapalı.")

# Test edelim
if __name__ == "__main__":
    # Simülasyon verisi
    ornek_nem = 22
    sulama_kontrolu(ornek_nem)
