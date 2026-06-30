print("=== INPUT DATA ===")
total = float(input("Total belanja (dalam Rupiah): "))
is_member = input("Member? (True/False): ")
is_member = bool(is_member.lower().capitalize())
promo = input("Kode promo: ")

def hitung_diskon(total, is_member, promo):
    print(f"Total awal: Rp{total:,}")
    memberdisc = 0
    promodisc = 0

    if is_member and total > 500000:
        memberdisc = total * 20 / 100
        print(f"Diskon dasar (20%): Rp{round(memberdisc):,}".replace(',', '.'))
    elif is_member:
        memberdisc = total * 10 / 100
        print(f"Diskon dasar (10%): Rp{round(memberdisc):,}".replace(',', '.'))
    else:
        print("Diskon dasar: Rp0.00")
    
    if promo == "HEMA" and (total - memberdisc) >= 100000:
        promodisc = (total - memberdisc) * 5 / 100
        print(f"Diskon tambahan (5% dari {round(total - memberdisc):,}): Rp{round(promodisc):,}".replace(',', '.'))
    else:
        if (total - memberdisc) < 100000:
            print("Diskon tambahan: tidak berlaku (total setelah diskon < 100,000)")
        else:
            print("Diskon tambahan: tidak berlaku (kode promo tidak valid)")
    
    print(f"Total akhir: Rp{round(total - memberdisc - promodisc):,}".replace(',', '.'))

print("\n=== RINGKASAN ===")
hitung_diskon(total, is_member, promo)
