expenses = []
budgets = {}

class InvalidExpenseError(Exception):
    def __init__(self, message):
        super().__init__(message)

def cekInvalid(description, amount):
    if not description.strip():
        raise InvalidExpenseError("Error: Deskripsi tidak boleh kosong.")
    if amount <= 0:
        raise InvalidExpenseError("Error: Jumlah harus lebih dari 0.")


while True:
    print("=== Expense Tracker ===")
    print("1. Tambah Pengeluaran\n2. Hapus Pengeluaran\n3. Lihat Semua Pengeluaran\n4. Total Pengeluaran per Kategori\n5. Atur Budget Kategori\n6. Cek Status Budget\n7. Keluar")

    try:
        inputUser = int(input("Pilih: "))
    except ValueError:
        print("Error: Pilihan harus berupa angka!\n")
        continue

    if inputUser == 7:
        break

    elif inputUser == 3:
        if not expenses:
            print("List pengeluaran masih kosong!")
        else:
            print("\n=== List Pengeluaran ===")
            for i, item in enumerate(expenses, start=1):
                amountStr = f"{item['amount']:,}".replace(",", ".")
                print(f"{i}. {item['description']} - Rp.{amountStr} ({item['category']})")

    elif inputUser == 4:
        if not expenses:
            print("List pengeluaran masih kosong!")
        else:
            kategoriDict = {}
            for item in expenses:
                kategori = item["category"]
                if kategori not in kategoriDict:
                    kategoriDict[kategori] = []
                kategoriDict[kategori].append(item)

            for kategori, listItem in kategoriDict.items():
                print(f"\n=== Kategori: {kategori} ===")
                for item in listItem:
                    amountStr = f"{item['amount']:,}".replace(",", ".")
                    print(f"- {item['description']} - Rp.{amountStr}")
            
    try:
        if inputUser == 1:
            while True:
                deskripsi = input("Masukkan deskripsi: ")
                if not deskripsi.strip():
                    print("Deskripsi tidak boleh kosong!")
                    continue

                while True:
                    try:
                        jumlah = int(input("Masukkan jumlah pengeluaran (Rupiah): "))
                        if jumlah <= 0:
                            print("Jumlah pengeluaran harus lebih besar dari 0!")
                            continue
                    except ValueError:
                        print("Jumlah pengeluaran harus berupa angka!")
                    else:
                        break

                while True:
                    kategoriInput = input("Masukkan kategori: ")
                    if not kategoriInput.strip():
                        print("Kategori tidak boleh kosong!")
                        continue
                    else:
                        break
                break
            try:
                cekInvalid(deskripsi, jumlah)
                expenseBaru = {"description": deskripsi, "amount": jumlah, "category": kategoriInput}
                expenses.append(expenseBaru)
                if kategoriInput in budgets:
                    total = 0
                    for exp in expenses:
                        if exp["category"] == kategoriInput:
                            total += exp["amount"]
                    if total > budgets[kategoriInput]:
                        totalStr = f"{total:,}".replace(",", ".")
                        budgetStr = f"{budgets[kategoriInput]:,}".replace(",", ".")
                        print(f"Budget {kategoriInput} terlampaui! Total: {totalStr}, Budget: {budgetStr}")
                print("Pengeluaran berhasil dicatat.")
            except InvalidExpenseError as e:
                print(e)
            finally:
                print("Proses pencatatan selesai.")

        elif inputUser == 2:
            while True:
                if not expenses:
                    print("List pengeluaran masih kosong!")
                    break
                else:
                    try:
                        for i, item in enumerate(expenses, start=1):
                            amountStr = f"{item['amount']:,}".replace(",", ".")
                            print(f"{i}. {item['description']} - Rp.{amountStr} ({item['category']})")
                        deleteExp = int(input("Masukkan index pengeluaran yang ingin dihapus: "))
                        if deleteExp > len(expenses) or deleteExp <= 0:
                            raise IndexError("Error: Masukkan index yang valid!")
                        else:
                            print(f"{deleteExp}. {expenses[deleteExp - 1]['description']} berhasil dihapus!")
                            expenses.pop(deleteExp - 1)
                            break
                    except ValueError:
                        print("Error: Index hanya berupa angka!")
                    except IndexError as e:
                        print(e)

        elif inputUser == 5:
            while True:
                newKategori = input("Masukkan nama kategori: ")
                if not newKategori.strip():
                    print("Kategori tidak boleh kosong!")
                    continue
                else:
                    while True:
                        try:
                            jumlahBudget = int(input("Masukkan jumlah budget: "))
                            if jumlahBudget <= 0:
                                print("Jumlah budget harus lebih besar dari 0!")
                                continue
                        except ValueError:
                            print("Jumlah budget harus berupa angka!")
                        else:
                            break
                    break

            assert jumlahBudget >= 0, "Error: Budget tidak boleh negatif."
            budgets[newKategori] = jumlahBudget
            jumlahBudgetStr = f"{jumlahBudget:,}".replace(",", ".")
            print(f"Budget untuk kategori '{newKategori}' berhasil diatur: Rp. {jumlahBudgetStr}")

        elif inputUser == 6:
            if not budgets:
                print("Belum ada budget yang diatur.")
            else:
                for category in budgets:
                    total = 0
                    for expense in expenses:
                        if expense["category"] == category:
                            total += expense["amount"]

                    budgetStr = f"{budgets[category]:,}".replace(",", ".")
                    totalStr = f"{total:,}".replace(",", ".")
                    if total > budgets[category]:
                        print(f"Budget {category} terlampaui! Total: {totalStr}, Budget: {budgetStr}")
                    else:
                        print(f"Budget {category} aman. Total: {totalStr}, Budget: {budgetStr}")   
    except InvalidExpenseError as e:
        print(e)
    except AssertionError as e:
        print(e)
    finally:
        print()