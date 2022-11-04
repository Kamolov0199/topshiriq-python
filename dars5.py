class Person:
    def __init__(self, name, surname, otchestvo):
        self.name = name
        self.surname = surname
        self.otchestvo = otchestvo
    def __str__(self):
        return f"{self.ism} {self.surname} {self.otchestvo}"


class Hobby(Person):
    def __init__(self, name, surname, otchestvo, hobby,cause):
        super().__init__(name, surname, otchestvo)
        self.hobby = hobby
        self.cause = cause

    def seal(self):
        print(self.name, self.surname, self.otchestvo, self.hobby, "ga qiziqadi, chunki u", self.cause, "ni yoqtiradi" )

hobby1 = Hobby("Asadova", "Madina", "Malikovna", "Anime", "Anime kurish")
hobby2 = Hobby("Mardonov", "Murod", "Aliyevich", "Futbol", "Futbol o'ynash")
hobby3 = Hobby("Mironov", "Emil", "Maratovich", "Counter-Strike o'ynash", "kompyuterda uyin uynash")

print(hobby1.seal())
print(hobby2.seal())
print(hobby3.seal())


class Job(Person):
    def __init__(self, name, surname, otchestvo, job, work):
        super().__init__(name, surname, otchestvo)
        self.job = job
        self.work = work

    def pechat(self):
        print(self.name, self.surname, self.otchestvo, self.job, "kasbini egasi. U", self.work)

job1 = Job("Hamrayeva", "Umida", "Aliyevna", "o'qituvchi", "bolalarga dars beradi")
job2 = Job("Halilova", "Gulhayo", "Gafurovna", "programmist", "dastur tuzadi")
job3 = Job("Abduraimov", "Oybek", "Ulug'bekovich", "direktor", "Cipheredu markazini boshqaradi")

print(job1.pechat())
print(job2.pechat())
print(job3.pechat())
 

class Maktab(Person):
    def __init__(self, name, surname, otchestvo, school, sinf):
        super().__init__(name, surname, otchestvo)
        self.school = school
        self.sinf = sinf

    def chiqarish(self):
        print(self.name, self.surname, self.otchestvo, self.school, self.sinf)

school1 = Maktab("Nuriddinova", "Araylim", "Tolgatovna", "35-maktab", "11-A sinfini tugatgan")
school2 = Maktab("Hushvaqtova", "Ruxsora", "Nasimovna", "1-IDUM", "9-B sinf o'quvchisi")
school3 = Maktab("Abduvaliyava", "Setora", "Akmalovna", "33-maktab", "10-F sinf o'quvchisi")

print(school1.chiqarish())
print(school2.chiqarish())
print(school3.chiqarish())
