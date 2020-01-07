x = input("Masukkan jam mulai dgn format 24 jam (TT.TT) : ")  #input bilangan float yang didahului oleh kalimat sebelum proses input
y = input("Masukkan lamanya durasi waktu dalam bilangan bulat (menit) : ") #input bilangan integer yang didahului oleh kalimat sebelum proses input


# untuk y, jika y kurang dr 60 maka tinggal dibagi 100
# jadinya y = 0 koma sekian...
# contoh 45 menit berarti tinggal 0.45
# kalau salah berarti y lebih dari 60 maka :
# "int(int(y)/60)" agar mendapat jam nya
# "(int(y)%60/100))" agar mendapat menitnya
# contoh y = 150
#  int(int(y)/60)= 2
# (int(y)%60/100)) = 0.30
#  maka y = (int(int(y)/60) + (int(y)%60/100)) = 2 + 0.30 = 2.30

if(int(y)<60): 
    y = float(int(y)/100)
else : 
    y = (int(int(y)/60) + (int(y)%60/100))



#kode di bawah untuk menjumlahkan waktu x dan y
# "%0.2f" % -> agar ketika menjumlahkan bisa muncul 2 digit belakang
#karena kalau hanya (float(x)+float(y)) , nanti misalnya penjumlahan 7.40 dengan 0.10 jadinya malah 7.1 

z = "%0.2f" % (float(x)+float(y))
print("z = "+z)

#setelah eksekusi di atas kan memungkinkan terjadinya upnormal penjumlahan jam
#mengapa bisa terjadi ? karena kan tinggal njumlahin...belum memperhitungkan bahwa 60 menit itu = 1 jam
#bisa saja terjadi 7.76, 19.85,...dst
#maka untuk mengatasinya saya buat kode di bawah ini

#----------------kode dibawah agar mendapat 2 digit di belakang koma------------------

#mulai dari sini

b = str(int(float(z)*100))
print("b = "+b)
# kode di atas agar desimal menjadi bilangan bulat 
#mislanya 7.76 akan didapatkan 776

#lalu program di bawah agar mendapat 2 digit dibelakang koma
#kenapa mengincar 2 digit di belakang koma
#karena saya mengincar 7.76 belakangnya kan 76
#agar menjadi 1 jam 16 menit
#sehingga dari 7.76 seharusnya menjadi 8.16

if(len(b)==4) :    #"len(b)" == berarti panjang bilangan bulat b tadi
    a = str(b[2:4])  #kalau panjangnya 4 ambil dari kata ke 3-4, contoh 1776 berarti 76
else :			#mengapa kok gak nulisnya str(b[2:4]), malah str(b[3:4]) kan dimulainya dari kata ke 3-4...ya memang fitu aturannya jadi dihitungnya itu setelahnya misal 2:4 berarti dari kata 3 sampai 4
    a = str(b[1:3]) #jika salah berarti panjangnya 3, lalu ambil dari kata ke 2-3, contoh 776 berarti 76
print("a = "+a)

#--------------------------berakhir untuk mendapatkan 2 digit terakhir---------------------------------
#sudah mendapatkan digit 2 terakhir kan ??


#------------------kode dibawah agar 2 digit yang bermasalah tadi jadi benar misalnya 76 menit menjadi 1 jam 16 menit-------------------------

#mulai dari sini

#(int(a) % 60 != a) -> mengapa harus ada ini ?
#karena kita mementingkan yang digitnya bermasalah lebih dr 60
#kalau misalnya kurang dari 60 ya lewat aja 2 if di bawah hehe
#contohnya 7.16 kan 2 digit terakhirnya 16
#berarti kan udah beres tinggal lewat aja

#jika panjangya 4 angka maka lewat di bawah ini
if((int(a) % 60 != int(a)) and (len(b)==4) ) :
    z="%0.2f" % float(((int(b[0:2])+ 1.00) + ((int(a) % 60.00)/100) ))
#(int(a) % 60.00)/100) -> agar mendapat menitnya contoh tadi kan udh 76, maka diambil menitnya 16 menit
#menitnya tadi langsung dibagi 100 agar mendapat 0.16
#karena panjangya 4 maka (int(b[0:2])+ 1.00) yaitu 2 angka pertama diambil lalu ditambah 1
#contohnya kan tadi 1776, angka 2 pertama 17, maka 17 + 1 nanti jadi 18
#lalu dijumlah deh,  18 + 0.16 = 18.16


#jika panjangya 3 angka maka lewat di bawah ini
if((int(a) % 60 != int(a)) and (len(b)==3) ) :
    z="%0.2f" % float(((int(b[0:1])+ 1.00) + ((int(a) % 60.00)/100) ))
print("z = "+z)
#(int(a) % 60.00)/100) -> agar mendapat menitnya contoh tadi kan udh 76, maka diambil menitnya 16 menit
#menitnya tadi langsung dibagi 100 agar mendapat 0.16
#karena panjangya 3 maka (int(b[0:1])+ 1.00) yaitu 1 angka pertama diambil lalu ditambah 1
#contohnya kan tadi 776, angka 1 pertama 7, maka 7 + 1 nanti jadi 8
#lalu dijumlah deh,  8 + 0.16 = 8.16


#----------------------berakhir disini...------------------------------


#ini kalau misalnya penjumlahan lalu menghasilkan lebih dari pukul 24.00
if(float(z)>23.59) : 
    z = float(z) % 24.00

#print deh hasil akhirnya
print("Akhir waktunya adalah : "+ "%0.2f" % (float(z)))