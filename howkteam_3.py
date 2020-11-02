# update attribute by class - normal way
class SieuNhan:
    suc_manh = 50

    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac


sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")

SieuNhan.suc_manh = 40


# update attribute by class which calls method - advantage way
class SieuNhan:
    suc_manh = 50

    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

    @classmethod
    def cap_nhat_suc_manh(cls, para_sucmanh):
        cls.suc_manh = para_sucmanh


sieu_nhan_B = SieuNhan("Sieu nhan do", "Kiem", "Do")
print(SieuNhan.suc_manh)
print(sieu_nhan_B.suc_manh)

SieuNhan.cap_nhat_suc_manh(0)
print(SieuNhan.suc_manh)
print(sieu_nhan_B.suc_manh)


# update attribute by class of object which calls method - advantage way
class SieuNhan:
    suc_manh = 50

    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

    @classmethod
    def cap_nhat_suc_manh(cls, para_sucmanh):
        cls.suc_manh = para_sucmanh


sieu_nhan_C = SieuNhan("Sieu nhan do", "Kiem", "Do")
print(SieuNhan.suc_manh)
print(sieu_nhan_C.suc_manh)

sieu_nhan_C.cap_nhat_suc_manh(0)
print(SieuNhan.suc_manh)
print(sieu_nhan_C.suc_manh)


# create a object by class method
class SieuNhan:
    suc_manh = 50

    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

    @classmethod
    def from_string(cls, s):  # usually the method is processed like that is name 'from'
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        ten, vukhi, mausac = new_lst
        return cls(ten, vukhi, mausac)


raw_string = "Bito - kiem - trang"
sieu_nhan_D = SieuNhan.from_string(raw_string)
print(sieu_nhan_D.__dict__)


# static method
class SieuNhan:
    suc_manh = 50

    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

    @staticmethod
    def say_hi():
        print('hello')


sieu_nhan_E = SieuNhan('a', 'b', 'c')
sieu_nhan_E.say_hi()



