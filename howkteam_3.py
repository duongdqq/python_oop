# update attribute by class - normal way
class SieuNhan:
    suc_manh = 50

    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac


sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")

SieuNhan.suc_manh = 40


# update attribute by class method - advantage way
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