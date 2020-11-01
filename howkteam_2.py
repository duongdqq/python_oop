# declare variable in class and outside constructor
class SieuNhan:
    suc_manh = 100

    def __init__(self, para_ten, para_vukhi, para_mausac):
        self.ten = para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mausac


sieunhanA = SieuNhan('bito', 'dao', 'trang den')
print(sieunhanA.suc_manh)
print(SieuNhan.suc_manh)


# update attribute by class
class SieuNhan:
    suc_manh = 100

    def __init__(self, para_ten, para_vukhi, para_mausac):
        self.ten = para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mausac


sieunhanA = SieuNhan('bito', 'dao', 'trang den')
print(SieuNhan.suc_manh)
print(sieunhanA.suc_manh)

SieuNhan.suc_manh = 0
print(SieuNhan.suc_manh)
print(sieunhanA.suc_manh)


# update attribute by constructor
class SieuNhan:
    so_thu_tu = 1
    suc_manh = 100

    def __init__(self, para_ten, para_vukhi, para_mausac):
        self.ten = para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mausac
        self.stt = SieuNhan.so_thu_tu
        SieuNhan.so_thu_tu += 1


sieunhanB = SieuNhan('bito', 'dao', 'trang den')
sieunhanC = SieuNhan('sut', 'kiem', 'trang vang')
print(sieunhanB.stt)
print(sieunhanC.stt)
print(SieuNhan.so_thu_tu)


# update attribute by object
class SieuNhan:
    suc_manh = 100

    def __init__(self, para_ten, para_vukhi, para_mausac):
        self.ten = para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mausac


sieunhanA = SieuNhan('bito', 'dao', 'trang den')
print(SieuNhan.suc_manh)
print(sieunhanA.suc_manh)

sieunhanA.suc_manh = 0
print(SieuNhan.suc_manh)
print(sieunhanA.suc_manh)


# use attribute in methods
class SieuNhan:
    suc_manh = 100

    def __init__(self, para_ten, para_vukhi, para_mausac):
        self.ten = para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mausac

    def xinchao(self):
        print('xin chao ', self.ten)
        print('su dung vu khi', self.vukhi)


sieunhanA = SieuNhan('bito', 'dao', 'trang den')
sieunhanA.xinchao()