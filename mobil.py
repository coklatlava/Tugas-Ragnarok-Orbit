from abc import abstractmethod, ABC


class Mobil(object):
    def __init__(self, jenis, tahun, mesin):
        self.jenis = jenis
        self.tahun = tahun
        self.mesin = mesin
    
    def h(self, durasi):
        for i in range(durasi):
            print("jenis ")
            
    def info(self):
        print(f"jenis: {self.jenis}\nTahun: {self.tahun}\nMesin: {self.mesin}")

        
class GTR(mobil):
    def __init__(self, jenis, tahun, mesin, keturunan):
        super().__init__(jenis, tahun, mesin)
        self.keturunan= keturunan
        
        
    def ab(self, durasi):
        for i in range(durasi):
            print("stututututututu.")
            
            
class Mobil(object):
    
    def __init__(mb, input_merk, input_mesin, input_tahun, input_horsepower):
        mb.merk = input_merk
        mb.mesin = input_mesin
        mb.tahun = input_tahun
        mb.horsepower=input_horsepower

    def jm(mb, mob):
        for x in range(mob):
            print(" 6inline")

    def info(mb):
        print(f"merk: {mb.merk}, mesin: {mb.mesin}, tahun :{mb.tahun}, horsepower :{mb.horsepower}")


mobil1 = Mobil("Nissan GTR", "RB26", "2000", "500HP")

mobil1.info()
        

merk= "GTR"
warna= "hitam"
barang = "Mobil"
horsepower = " 500hp"

def GTR():
    print("Nissan Skyline GTR...")
    
def info_GTR(merk,warna,barang,horsepower):
    print(f"merk: {merk}, warna: {warna}, barang :{barang}, horsepower :{horsepower}") 

info_GTR(merk,warna,barang,horsepower)
GTR()


class Mobil(ABC):
    
    @abstractmethod
    def caramengemudi(self):
        pass
    
class GTR(Mobil):
    def caramengemudi(self):
        print("Mobil ini bisa digunakan untuk Drag, Harian, maupun Drift.\n")
        
class Silvia(Mobil):
    def caramengemudi(self):
        print("Mobil ini dapat digunakan untuk harian namun lebih sering digunakan untuk ajang drift.")
gtr1=GTR()
silvia1=Silvia()

gtr1.caramengemudi()
silvia1.caramengemudi()