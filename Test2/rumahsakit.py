# Class untuk pasien
class Pasien:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Pasien: {self.nama}, Umur: {self.umur}"

class Dokter:
    def __init__(self, nama, spesialis):
        self.nama = nama
        self.spesialis = spesialis

    def info(self):
        return f"Dokter: {self.nama}, Spesialis: {self.spesialis}"

class Ruangan:
    def __init__(self, nomor, jenis):
        self.nomor = nomor
        self.jenis = jenis

    def info(self):
        return f"Ruangan: {self.nomor}, Jenis: {self.jenis}"

class RekamMedis:
    def __init__(self, pasien):
        self.pasien = pasien
        self.rekam = []

    def tambah_rekam(self, detail):
        self.rekam.append(detail)

    def info(self):
        rekam_info = "\n".join(self.rekam)
        return f"Rekam Medis untuk {self.pasien.info()}:\n{rekam_info}"

class RumahSakit:
    def __init__(self, nama):
        self.nama = nama
        self.ruangan_list = []
        self.dokter_list = []

    def tambah_ruangan(self, ruangan):
        self.ruangan_list.append(ruangan)

    def tambah_dokter(self, dokter):
        self.dokter_list.append(dokter)

    def info(self):
        ruangan_info = ", ".join([ruangan.info() for ruangan in self.ruangan_list])
        dokter_info = ", ".join([dokter.info() for dokter in self.dokter_list])
        return f"Rumah Sakit: {self.nama}\nRuangan: {ruangan_info}\nDokter: {dokter_info}"


rs = RumahSakit("RS Walanda")
rs.tambah_ruangan(Ruangan(101, "Kamar Tidur"))
rs.tambah_ruangan(Ruangan(102, "ICU"))
rs.tambah_dokter(Dokter("Dr. MelChris", "Kardiologi"))
rs.tambah_dokter(Dokter("Dr. K.Hukom", "Pediatri"))

pasien1 = Pasien("Rivael Tambengi", 21)
rekam1 = RekamMedis(pasien1)
rekam1.tambah_rekam("Diagnosa: Ambeien")
rekam1.tambah_rekam("Pengobatan: Obat A")

print(rs.info())
print(rekam1.info())
