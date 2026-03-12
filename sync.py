import os
import requests
import time
from datetime import datetime
from datetime import timedelta
from dotenv import load_dotenv
from ytmusicapi import YTMusic

load_dotenv()

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
LASTFM_USER = os.getenv("LASTFM_USER")
YT_PLAYLIST_ID = os.getenv("YT_PLAYLIST_ID")
START_DATE = datetime.now() - timedelta(days=2) # Başlangıç tarihi

def get_lastfm_tracks():
    if not LASTFM_API_KEY or not LASTFM_USER:
        print("❌ HATA: Last.fm API Key veya Kullanıcı Adı eksik.")
        return []

    print(f"📡 Last.fm verileri çekiliyor... (Kullanıcı: {LASTFM_USER})")
    
    start_timestamp = int(START_DATE.timestamp())
    all_tracks = []
    page = 1
    total_pages = 1
    
    while page <= total_pages:
        url = "http://ws.audioscrobbler.com/2.0/"
        params = {
            "method": "user.getrecenttracks",
            "user": LASTFM_USER,
            "api_key": LASTFM_API_KEY,
            "format": "json",
            "from": start_timestamp,
            "limit": 200,
            "page": page
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if "recenttracks" in data:
                total_pages = int(data["recenttracks"]["@attr"]["totalPages"])
                current_batch = data["recenttracks"]["track"]
                
                if not isinstance(current_batch, list):
                    current_batch = [current_batch]

                for track in current_batch:
                    if "@attr" in track and track["@attr"].get("nowplaying") == "true":
                        continue
                    
                    artist = track['artist']['#text']
                    song = track['name']
                    #"Sanatçı - Şarkı"
                    all_tracks.append(f"{artist} - {song}")
                
                print(f"   -> Sayfa {page}/{total_pages} işlendi.")
                page += 1
                time.sleep(0.5) 
            else:
                print("⚠️ Last.fm'den veri dönmedi veya limit aşıldı.")
                break
        except Exception as e:
            print(f"❌ Last.fm Bağlantı Hatası: {e}")
            break

    unique_tracks = list(dict.fromkeys(all_tracks[::-1]))
    print(f"✅ Toplam {len(unique_tracks)} benzersiz şarkı bulundu.")
    return unique_tracks

def get_existing_yt_tracks(yt):
    print("🔍 YouTube Playlist içeriği kontrol ediliyor...")
    try:
        playlist = yt.get_playlist(YT_PLAYLIST_ID)
        existing_set = set()
        
        for item in playlist.get('tracks', []):
            title = item['title']
            artists = item.get('artists', [])
            artist_name = artists[0]['name'] if artists else ""
            
            full_name = f"{artist_name} - {title}"
            existing_set.add(full_name.lower())
            
        return existing_set
    except Exception as e:
        print(f"⚠️ Playlist okunamadı (Boş olabilir veya ID hatalı): {e}")
        return set()

def sync_to_youtube(track_names):
    if not os.path.exists("browser.json"):
        print("❌ HATA: 'browser.json' dosyası bulunamadı. Lütfen 'ytmusicapi setup' yapın.")
        return

    print("\n🔴 YouTube Music Bağlantısı Kuruluyor...")
    try:
        yt = YTMusic("browser.json")
    except Exception as e:
        print(f"❌ Oturum Hatası: {e}")
        return

    existing_tracks = get_existing_yt_tracks(yt)
    print(f"   -> Playlistte şu an {len(existing_tracks)} şarkı var.")
    
    print(f"\n🚀 Senkronizasyon Başlıyor...")
    added_count = 0

    for i, song_query in enumerate(track_names):
        if song_query.lower() in existing_tracks:
            continue

        try:
            search_results = yt.search(song_query, filter="songs")
            
            if search_results:
                target_song = search_results[0]
                video_id = target_song['videoId']
                
                yt.add_playlist_items(YT_PLAYLIST_ID, [video_id])
                
                print(f"[{i+1}/{len(track_names)}] 🆕 Eklendi: {song_query}")
                added_count += 1
                
                existing_tracks.add(song_query.lower())
                
                time.sleep(10) #ekleme süresi
            else:
                print(f"[{i+1}/{len(track_names)}] ❌ Bulunamadı: {song_query}")
                
        except Exception as e:
            print(f"⚠️ Hata ({song_query}): {e}")
            time.sleep(10) # ekleme süresi

    print(f"\n🏁 İşlem Tamamlandı! Toplam {added_count} yeni şarkı eklendi.")

if __name__ == "__main__":
    tracks = get_lastfm_tracks()
    if tracks:
        sync_to_youtube(tracks)
    else:
        print("Eklenecek yeni şarkı yok veya Last.fm verisi boş.")