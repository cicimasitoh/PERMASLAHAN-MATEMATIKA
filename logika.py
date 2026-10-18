# luas_lingkaran.py
# Program Menghitung Luas dan Keliling Lingkaran

# Definisi Konstanta
PI = 3.14159

print("=== PROGRAM HITUNG LUAS DAN KELILING LINGKARAN ===")

# Input dari pengguna
try:
    r = float(input("Masukkan panjang jari-jari (r): "))

    # Pengondisian / Seleksi
    if r > 0:
        luas = PI * (r ** 2)
        keliling = 2 * PI * r

        # Output hasil
        print(f"\nHasil Perhitungan:")
        print(f"Luas Lingkaran     : {luas:.2f}")
        print(f"Keliling Lingkaran : {keliling:.2f}")
    else:
        print("\nPeringatan: Jari-jari harus lebih besar dari 0!")

except ValueError:
    print("\nError: Input harus berupa angka/bilangan!")