class Students:
    student = {}
    
    def __init__(self, name, kelas, npm):
        self.name = name
        self.kelas = kelas
        self.npm = npm
        
        if npm not in Students.student:  # Periksa jika npm belum ada
            Students.student[npm] = {"name": name, "kelas": kelas, "NPM" : npm}
            print(f"Mahasiswa {name} telah ditambahkan.")
        else:  # Jika npm sudah ada, perbarui data mahasiswa
            Students.student[npm] = {"name": name, "kelas": kelas, "NPM" : npm}
            print(f"Data mahasiswa dengan NPM {npm} telah diperbarui.")
        
        
student1 = Students("lutfi", "4IA21", 51421012)
print(Students.student)
student1 = Students("lutfi", "4IA22", 51421011)
print(Students.student)
