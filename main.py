import socket

hedef = input("Domain veya IP adresi gir: ")

print(f"\n--- {hedef} üzerindeki servisler taranıyor ---\n")

kritik_portlar = {
    21: "FTP (Dosya Transfer)",
    22: "SSH (Güvenli Bağlantı)",
    23: "Telnet (Eski Bağlantı)",
    25: "SMTP (Mail Gönderme)",
    53: "DNS (Alan Adı)",
    80: "HTTP (Web Sitesi)",
    110: "POP3 (Mail Alma)",
    139: "NetBIOS (Dosya Paylaşım)",
    143: "IMAP (Mail Okuma)",
    443: "HTTPS (Güvenli Web)",
    445: "SMB (Windows Paylaşım)",
    1433: "MSSQL (SQL Server)",
    3306: "MySQL (Veritabanı)",
    3389: "RDP (Uzak Masaüstü)",
    5432: "PostgreSQL",
    5900: "VNC (Ekran Paylaşımı)",
    6379: "Redis",
    8080: "HTTP-Alt (Web Proxy)",
    8443: "HTTPS-Alt",
    27017: "MongoDB"
}

for port, servis_adi in kritik_portlar.items():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.settimeout(0.5) 
    
    sonuc = s.connect_ex((hedef, port))
    
    if sonuc == 0:
        print(f"Port {port:<5} [{servis_adi}] -> AÇIK")
    else:
        print(f"Port {port:<5} [{servis_adi}] -> KAPALI")
        
    s.close()

print("\n--- Tarama Tamamlandı ---")