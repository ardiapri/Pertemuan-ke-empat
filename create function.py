def perubahan_suhu(nilai_suhu, satuan_suhu):
    if satuan_suhu.upper() == 'C':
        # Mengonversi dari Celsius ke Fahrenheit
        hasil = (nilai_suhu * 9/5) + 32
        return f"{nilai_suhu}°C sama dengan {hasil:.2f}°F"
    elif satuan_suhu.upper() == 'F':
        # Mengonversi dari Fahrenheit ke Celsius
        hasil = (nilai_suhu - 32) * 5/9
        return f"{nilai_suhu}°F sama dengan {hasil:.2f}°C"
    else:
        return "Satuan suhu tidak valid. Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."


nilai_suhu = float(input("Masukkan nilai suhu: "))
satuan_suhu = input("Masukkan satuan suhu (C atau F): ")


hasil_konversi = perubahan_suhu(nilai_suhu, satuan_suhu)
print(hasil_konversi)
luas_lingkaran = lambda r: 3.14 * r ** 2

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas_lingkaran(jari_jari)}")

#159