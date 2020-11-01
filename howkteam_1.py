# create class
class SieuNhan:
    pass


sieu_nhan_A = SieuNhan()
print(sieu_nhan_A)


# create attribute
class SieuNhan:
    pass


sieu_nhan_A = SieuNhan()
sieu_nhan_A.ten = 'bito'
sieu_nhan_A.vu_khi = 'kiem'
sieu_nhan_A.mau_sac = 'trang den'

print(sieu_nhan_A.ten)
print(sieu_nhan_A.vu_khi)
print(sieu_nhan_A.mau_sac)
# print(sieu_nhan_A.suc_manh)  # error


# how constructor works
class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac


sieu_nhan_B = SieuNhan('bia', 'dao', 'vang')
print(sieu_nhan_B.ten)
print(sieu_nhan_B.vu_khi)
print(sieu_nhan_B.mau_sac)


# how method works
class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def xinchao(self):
        return 'Hello ' + self.ten


sieu_nhan_C = SieuNhan('sut', 'bua', 'trang vang')
print(sieu_nhan_C.xinchao())  # popular calling
print(SieuNhan.xinchao(sieu_nhan_C))  # another way but unpopular



