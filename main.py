from table import crew, menu
import os, time
order = []
orderPrice = []
orderAmount = []
totalHarga = 0

def masuk():
    order.clear()
    orderAmount.clear()
    orderPrice.clear()
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
        print('ID makanan tidak ada.')
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
        os.system('cls||clear')
        pesanSelesai()
        os.system('pause')
        os.system('cls||clear')
        masuk()
    else:
        print('unknow input')
        time.sleep(2)
        pesanLagi()
        

        
def pesanSelesai():
    print('')
    print('')
    print(f'{"Resto Amdiketu":^48}')
    print(f'{"Jl. Ambatukam, No 68":^48}')
    print(f'{"________________________________":^48}')
    print(f'{"Telp : 021 - 14045":^48}')
    print(f'{"Pesanan":<28}{"Jumlah":^9}{"Harga":^14}')
    for o, p, m in zip(order, orderPrice, orderAmount):
        print(f'{o:<28}{m:^7}','  Rp {:<12,.0f}'.format(p))
    print('')
    print(f'{"TOTAL :":>4}{" Rp ":>2}''{:>2,.0f}'.format(sum(orderPrice)))
    print('')
    print('')

masuk()