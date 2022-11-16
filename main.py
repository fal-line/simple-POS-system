from table import crew, menu
import os, time
order = []
orderPrice = []
orderAmount = []
totalHarga = 0
change = []
wang = []

def masuk():
    order.clear()
    orderAmount.clear()
    orderPrice.clear()
    change.clear()
    wang.clear()
    os.system('cls||clear')
    print('Selamat Datang')
    idMasuk = input('Masukan ID: ')
    for n in crew():
        if idMasuk == n['nim']:
            print('berhasil masuk')
            halMenu(menu)
            halPesan()
            break
    if n != crew():
        print('ID salah atau tidak terdaftar')
        time.sleep(2)
        os.system('cls||clear')
        masuk()
        
def halMenu(menu):
    os.system('cls||clear')
    print(f'{"ID":^5}{"Menu":^22}{"Harga":>8}')
    for m in menu():
        mID = m['id']
        mName = m['name']
        mPrice = int(m['price'])
        print(f'{mID:^5}{mName:<22}', 'Rp {:^2,.0f}'.format(mPrice))
    
def halPesan():
    print('')
    x = input('Masukan ID Pesanan : ')
    for m in menu():
        nama = str(m['name'])
        if x == m['id']:
            try:
                j = int(input('Jumlah Pesanan : '))
                order.append(nama)
                orderAmount.append(j)
                orderPrice.append((int(m['price'])*j))
                pesanLagi()
                return order, orderPrice
            except ValueError:
                print("Jumlah tidak valid, tolong masukan angka")  
                time.sleep(2)
                os.system('cls||clear')
                halMenu(menu)
                halPesan()
    if x != m['id']:
        print('ID makanan tidak ada, atau salah.')
        time.sleep(2)
        os.system('cls||clear')
        halMenu(menu)
        halPesan()
            
def pesanLagi():
    x = input('Apakah ada pesanan lain? [y/n]')
    if x == 'y':
        os.system('cls||clear')
        halMenu(menu)
        halPesan()
    if x == 'n':
        print('')
        bayar()
        pesanSelesai()
        os.system('pause')
        os.system('cls||clear')
        masuk()
    else:
        print('unknown input')
        time.sleep(2)
        pesanLagi()
        
def bayar():
    print(f'{"Total  :":>4}{" Rp ":>2}''{:>2,.0f}'.format(sum(orderPrice)))
    try:
        pay = int(input('Masukan nomimal pembayaran : '))
        wang.append(pay)
        if pay < sum(orderPrice):
            print('Pembayaran tidak bisa kurang dari grand total.')
            time.sleep(2)
            os.system('cls||clear')
            bayar()
        if pay >= sum(orderPrice):
            pay = pay - int(sum(orderPrice))
            change.append(pay)
            os.system('cls||clear')
    except ValueError:
        print("Nominal tidak valid, tolong masukan angka")  
        time.sleep(2)
        os.system('cls||clear')
        bayar()
    
        
def pesanSelesai():
    print('')
    print('')
    print(f'{"Resto Amdiketu - Cabang 68":^48}')
    print(f'{"Jl. Ambatukam, Kranji Pusat, Blok E6-F2":^48}')
    print(f'{"==================================":^48}')
    print(f'{"Telp : 021 - 14045":^48}')
    print('')
    print(f'{"Pesanan":<28}{"Jumlah":^9}{"Harga":^14}')
    for o, p, m in zip(order, orderPrice, orderAmount):
        print(f'{o:<28}{m:^7}','  Rp {:<12,.0f}'.format(p))
    print('')
    print(f'{"TOTAL  :":>4}{" Rp ":>2}''{:>2,.0f}'.format(sum(orderPrice)))
    print(f'{"CASH   :":>4}{" Rp ":>2}''{:>2,.0f}'.format(sum(wang)))
    print(f'{"CHANGE :":>4}{" Rp ":>2}''{:>2,.0f}'.format(sum(change)))
    print('')
    print('')

masuk()