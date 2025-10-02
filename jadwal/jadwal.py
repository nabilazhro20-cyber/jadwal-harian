from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# File PDF output
pdf_file = "Jadwal_Harian_Bilbil.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=landscape(A4))
styles = getSampleStyleSheet()
story = []

# Judul
story.append(Paragraph("📅 Jadwal Harian Bilbil (Senin - Jumat)", styles["Title"]))
story.append(Spacer(1, 12))

# Data jadwal terbaru
jadwal = {
    "Senin": [
        ("04:40 - 04:58", "Bangun + wudhu"),
        ("04:58 - 05:15", "Sholat Subuh"),
        ("05:15 - 05:45", "Sarapan"),
        ("05:45 - 06:20", "Mandi + make up"),
        ("06:20 - 06:40", "Beres-beres"),
        ("06:40 - 07:00", "Perjalanan ke kampus"),
        ("08:00 - 10:30", "Kuliah: Manajemen Proyek ICT"),
        ("10:30 - 12:00", "Kuliah: Sistem Enterprise"),
        ("12:00 - 12:20", "Perjalanan pulang"),
        ("12:20 - 12:45", "Sholat Dzuhur + makan siang"),
        ("13:00 - 15:00", "Istirahat / tidur siang"),
        ("15:28 - 15:45", "Sholat Ashar"),
        ("15:45 - 18:00", "Belajar mandiri / organisasi SmartTech"),
        ("18:20 - 18:35", "Sholat Maghrib + makan malam"),
        ("19:28 - 19:40", "Sholat Isya"),
        ("20:00 - 21:30", "Tugas / coding project"),
        ("21:30 - 22:30", "Santai / hiburan"),
        ("22:30 - 23:00", "Persiapan tidur"),
        ("23:00 - 04:40", "Tidur"),
    ],
    "Selasa": [
        ("04:40 - 04:58", "Bangun + wudhu"),
        ("04:58 - 05:15", "Sholat Subuh"),
        ("05:15 - 05:45", "Sarapan"),
        ("05:45 - 06:20", "Mandi + make up"),
        ("06:20 - 06:40", "Beres-beres"),
        ("06:40 - 07:00", "Perjalanan ke kampus"),
        ("08:50 - 10:30", "Kuliah: Basis Data Lanjut"),
        ("10:30 - 12:00", "Praktikum Basis Data Lanjut"),
        ("12:18 - 12:45", "Sholat Dzuhur + makan siang"),
        ("13:00 - 15:30", "Kuliah: Data Mining"),
        ("15:30 - 15:50", "Perjalanan pulang"),
        ("15:50 - 18:00", "Istirahat / tidur / belajar ringan"),
        ("15:28 - 15:45", "Sholat Ashar"),
        ("18:20 - 18:35", "Sholat Maghrib + makan malam"),
        ("19:28 - 19:40", "Sholat Isya"),
        ("20:00 - 21:30", "Ngerjain tugas / coding project"),
        ("21:30 - 22:30", "Santai"),
        ("22:30 - 23:00", "Persiapan tidur"),
        ("23:00 - 04:40", "Tidur"),
    ],
    "Rabu": [
        ("04:40 - 04:58", "Bangun + wudhu"),
        ("04:58 - 05:15", "Sholat Subuh"),
        ("05:15 - 05:45", "Sarapan"),
        ("05:45 - 06:20", "Mandi + make up"),
        ("06:20 - 06:40", "Beres-beres"),
        ("06:40 - 07:00", "Perjalanan ke kampus"),
        ("08:00 - 10:30", "Kuliah: Analisis & Perancangan Sistem"),
        ("10:30 - 13:00", "Kuliah: Sistem Keamanan Informasi"),
        ("13:00 - 13:20", "Perjalanan pulang"),
        ("13:20 - 15:20", "Istirahat / tidur / belajar ringan"),
        ("15:28 - 15:45", "Sholat Ashar"),
        ("15:45 - 17:30", "Belajar / persiapan asistensi"),
        ("17:30 - 17:50", "Perjalanan ke kampus"),
        ("18:00 - 20:01", "Asisten Lab"),
        ("20:01 - 20:20", "Perjalanan pulang"),
        ("20:20 - 20:40", "Sholat Isya + makan malam ringan"),
        ("20:40 - 21:30", "Tugas / coding project"),
        ("21:30 - 22:30", "Santai"),
        ("22:30 - 23:00", "Persiapan tidur"),
        ("23:00 - 04:40", "Tidur"),
    ],
    "Kamis": [
        ("04:40 - 04:58", "Bangun + wudhu"),
        ("04:58 - 05:15", "Sholat Subuh"),
        ("05:15 - 05:45", "Sarapan"),
        ("05:45 - 06:20", "Mandi + make up"),
        ("06:20 - 06:40", "Beres-beres"),
        ("06:40 - 07:00", "Perjalanan ke kampus"),
        ("08:00 - 10:16", "Asisten Lab"),
        ("10:30 - 12:00", "Kuliah: PBO Lanjut"),
        ("12:18 - 12:45", "Sholat Dzuhur + makan siang"),
        ("13:00 - 14:30", "Praktikum PBO Lanjut"),
        ("14:30 - 14:50", "Perjalanan pulang"),
        ("15:00 - 15:20", "Sholat Ashar"),
        ("15:20 - 18:00", "Istirahat / tidur / belajar"),
        ("18:20 - 18:35", "Sholat Maghrib + makan malam"),
        ("19:28 - 19:40", "Sholat Isya"),
        ("20:00 - 21:30", "Tugas / coding project"),
        ("21:30 - 22:30", "Santai"),
        ("22:30 - 23:00", "Persiapan tidur"),
        ("23:00 - 04:40", "Tidur"),
    ],
    "Jumat": [
        ("04:40 - 04:58", "Bangun + wudhu"),
        ("04:58 - 05:15", "Sholat Subuh"),
        ("05:15 - 05:45", "Sarapan"),
        ("05:45 - 06:20", "Mandi + make up"),
        ("06:20 - 06:40", "Beres-beres"),
        ("06:40 - 07:00", "Perjalanan ke kampus"),
        ("08:50 - 10:30", "Kuliah: Front End Development"),
        ("10:30 - 12:00", "Praktikum Front End Development"),
        ("12:00 - 12:20", "Perjalanan pulang"),
        ("12:20 - 12:50", "Sholat Jumat + makan siang"),
        ("13:00 - 15:20", "Istirahat / tidur siang"),
        ("15:28 - 15:45", "Sholat Ashar"),
        ("15:45 - 17:30", "Belajar / persiapan asistensi"),
        ("17:30 - 17:50", "Perjalanan ke kampus"),
        ("18:00 - 20:01", "Asisten Lab"),
        ("20:01 - 20:20", "Perjalanan pulang"),
        ("20:20 - 20:40", "Sholat Isya + makan malam ringan"),
        ("20:40 - 21:30", "Tugas / coding project"),
        ("21:30 - 22:30", "Santai"),
        ("22:30 - 23:00", "Persiapan tidur"),
        ("23:00 - 04:40", "Tidur"),
    ]
}

# Generate tabel per hari
for hari, kegiatan in jadwal.items():
    story.append(Paragraph(f"📌 {hari}", styles["Heading2"]))
    data = [["Jam", "Kegiatan"]] + kegiatan
    table = Table(data, colWidths=[100, 450])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    story.append(table)
    story.append(Spacer(1, 20))

# Build PDF
doc.build(story)
print(f"✅ Jadwal berhasil dibuat: {pdf_file}")
