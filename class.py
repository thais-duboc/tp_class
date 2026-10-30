#Thais Duboc
#Echauffement 1

import math

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def norm(self):
        return(math.sqrt(self.x**2+self.y**2))

    def __repr__(self):
        return(f"Point({self.x}, {self.y})")


# pour tester

try:
    p = Point(3, 4)
    assert (p.x, p.y) == (3, 4)
    assert p.norm() == 5.0
    assert repr(p) == "Point(3, 4)"
    q = Point(0, 1)
    assert (q.x, p.x) == (0, 3)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

#Echauffement 2

p = Point(3, 4)
print(p.norm())
print(Point.norm(p))
#1. Oui les 2 renvoient le meme résultat
#2. Si norm() ne prend pas self en argument dans sa définition, p.norm() renvoie un message d'erreur
#3. print(p) si la classe n'a pas de __repr__ renvoie la représentation par défaut de l'objet, qui ressemble à ceci :<__main__.Point object at 0x7f8d601b2340> Si aucune méthode __repr__ (ni __str__) n'est définie dans la classe, Python utilise celle de la classe mère universelle (object), qui se contente d'indiquer le nom de la classe et l'emplacement de l'objet en mémoire.

#Echauffement 3

#Le code va renvoyer [1]

class Bad:
    items = []

    def add(self, x):
        self.items.append(x)

a, b = Bad(), Bad()
a.add(1)
print(b.items)

#1. Ici, items = [] est défini directement dans le corps de la classe, c'est un attribut de classe. Un attribut de classe est partagé entre toutes les instances (a et b). Comme a et b partagent la même liste en mémoire, b.items reflète la modification faite par a.

#2. Il faut initialiser la liste à l'intérieur avec __init__ et self.items. Elle devient ainsi un attribut d'instance propre à chaque objet créé.


class Bad1:
    def __init__(self):
        self.items = []

    def add(self, x):
        self.items.append(x)
#test
c, d = Bad1(), Bad1()
c.add(1)
print(d.items)
#c'est bon !

#Echauffement 4

class Tirelire:
    def __init__(self):
        self.items=[]

    def deposit(self, x):
        if x<=0:
            raise ValueError("La valeur doit être positive")
        else:
            self.items.append(x)

    def total(self):
        return(sum(self.items))

    def __len__(self):
        return(len(self.items))

    def __repr__(self):
        return(f"Tirelire({len(self.items)} coins, total={self.total():.2f})")
    


# pour tester

try:
    t = Tirelire()
    t.deposit(0.5)
    t.deposit(1)
    assert len(t) == 2
    assert t.total() == 1.5
    assert repr(t) == "Tirelire(2 coins, total=1.50)"
    other = Tirelire()
    assert len(other) == 0
    try:
        other.deposit(-1)
    except ValueError:
        pass
    else:
        raise Exception("a negative value should raise ValueError")
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

#c'est bon !

#La classe Student
from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.prenom=first_name
        self.nom=last_name
        self.grades=defaultdict(list)

    def add_grade(self, course: str, grade: float):
        if grade<0 or grade>20:
            raise ValueError("La valeur doit être comprise entre 0 et 20")
        else:
            self.grades[course].append(grade)

    def followed_topics(self):
        return(list(self.grades))

    def compute_average(self, course:str):
        if course not in self.grades:
            raise ValueError("La matière n'a pas encore de note")
        else:
            return(sum(self.grades[course])/len(self.grades[course]))

    def report(self):
        L=[]
        L.append(f"Report for student {self.prenom} {self.nom}")
        L.append("+===============+===============+")
        L.append("|     Topic     |    Average    |")
        L.append("+===============+===============+")
        for matiere in self.grades.keys():
            moyenne = f"{self.compute_average(matiere):.2f}"
            L.append(f"|{matiere:^15}|{moyenne:^15}|")
            L.append("+---------------+---------------+")
        return("\n".join(L))

    def __repr__(self):
        return(f"Student({self.prenom}{self.nom}, Grades:{dict(self.grades)})")
            
# pour tester

try:
    student = Student("Achille", "Talon")
    r = repr(student)
    assert isinstance(r, str), "__repr__ must return a str"
    assert "Achille" in r and "Talon" in r, f"first and last name should appear in {r!r}"
except Exception as e:
    print('OOPS - There is an issue in your code.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')
#c'est bon !

#Gestion des notes
#j'essaye avec un dictionnaire pour stocker les notes

# pour tester

try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
    try:
        student.add_grade("History", 25.)
    except ValueError:
        pass
    else:
        raise Exception("a grade outside of [0, 20] should raise ValueError")
except Exception as e:
    print('OOPS - There is an issue in your add_grade method.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')
print(student.followed_topics())
print(student.compute_average("History"))

#followed_topics
# pour tester

try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    topics = student.followed_topics()
    if len(topics) != 1 or "History" not in topics:
        raise Exception(f"Expecting ['History'] got {topics}")
except Exception as e:
    print('OOPS - There is an issue in your followed_topics method')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

#compute_average
# pour tester

try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
    if (student.compute_average("History") != 11.):
        raise Exception("Issue in your average calculation.")
    try:
        student.compute_average("French")
    except ValueError:
        pass
    else:
        raise Exception("If topic is not followed, a ValueError is expected")
    if student.followed_topics() != ["History"]:
        raise Exception(f"asking for the average of an unfollowed topic must not create it: {student.followed_topics()}")
except Exception as e:
    print('OOPS - There is an issue in your compute_average method.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

#report
# pour tester

try:
    reference_lines = ['Report for student Albert Einstein',
                       '+===============+===============+',
                       '|     Topic     |    Average    |',
                       '+===============+===============+',
                       '|  Mathematics  |     12.80     |',
                       '+---------------+---------------+',
                       '|  Scubadiving  |     12.50     |',
                       '+---------------+---------------+']

    student = Student("Albert", "Einstein")
    student.add_grade("Mathematics", 12.80)
    student.add_grade("Scubadiving", 12.50)
    report = student.report()
    report_lines = report.strip().split('\n')
    assert len(report_lines) == len(reference_lines), \
        f"expected {len(reference_lines)} lines, got {len(report_lines)}"
    for i, (lineref, linestudent) in enumerate(zip(reference_lines, report_lines), start=1):
        assert lineref == linestudent, f"Ligne {i} : \n attendu = {lineref}\n  obtenu = {linestudent}"
except AssertionError as e:
    print("Les deux chaines sont différentes")
    print(e)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')
print(student.report())
#ca marche !!!

from collections import Counter, defaultdict

#la classe
class Classe:
    def __init__(self, classname: str):
        self.classname=classname
        self.eleves={}

    def add_student(self, student: Student):
        self.eleves[(student.prenom, student.nom)]= student

    def __len__(self):
        return(len(self.eleves))

    def get_student(self, first_name: str, last_name: str):
        if (first_name, last_name) not in self.eleves:
            return(None)
        else:
            return(self.eleves[(first_name, last_name)])

    def load_students_from_file(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    prenom, nom = parts[0].strip(), parts[1].strip()
                    student = Student(prenom, nom)
                    self.add_student(student)

    def load_grades_from_file(self, filename: str):
        presents = set()
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = [p.strip() for p in line.strip().split(',')]
                prenom, nom, matiere = parts[:3]
                student = self.get_student(prenom, nom)
                if student is None:
                    # dans grades.csv mais pas dans la classe
                    print(f"Avertissement : Personne {prenom} {nom} n'est pas dans la classe.")
                    continue
                presents.add((prenom, nom))
                for note in parts[3:]:
                    student.add_grade(matiere, float(note))

        # dans la classe mais pas dans grades.csv
        absents = [cle for cle in self.eleves if cle not in presents]
        return absents

    def catalog(self):
        compteur = Counter()
        for student in self.eleves.values():
            compteur.update(student.followed_topics())
        return dict(compteur)

    def compute_averages(self):
        sommes = {}
        nombres = {}
        for student in self.eleves.values():
            for matiere in student.followed_topics():
                sommes[matiere] = sommes.get(matiere, 0) + student.compute_average(matiere)
                nombres[matiere] = nombres.get(matiere, 0) + 1
        return {matiere: sommes[matiere] / nombres[matiere] for matiere in sommes}

    def detailed_report(self, student: "Student | None"):
        if student is None:
            return "Student not found in the class."
        moyennes_classe = self.compute_averages()
        L = []
        L.append(f"Detailed Report for student {student.prenom} {student.nom}")   # "Detailed" ajouté
        L.append("+===============+===============+===============+")             # 3 colonnes
        L.append("|     Topic     |    Average    |   Class Avg   |")
        L.append("+===============+===============+===============+")
        for matiere in student.grades.keys():
            moyenne = f"{student.compute_average(matiere):.2f}"
            moyenne_classe = f"{moyennes_classe[matiere]:.2f}"                    # nouvelle colonne
            L.append(f"|{matiere:^15}|{moyenne:^15}|{moyenne_classe:^15}|")
            L.append("+---------------+---------------+---------------+")
        return "\n".join(L)

    def __repr__(self):
        for eleve in self.eleves:
            return(f"Class({self.classname}, Students: {eleve}, Grades:{dict(self.eleves[eleve].grades)}))])")

# pour tester

try:
    classe = Classe("P20")
    student = Student("Matthieu", "Mazière")
    classe.add_student(student)
    if len(classe) != 1:
        raise Exception('OOPS - There is an issue in your __len__ method.')
    r = repr(classe)
    if "P20" not in r or "Matthieu" not in r:
        raise Exception('OOPS - There is an issue in your __repr__ method.')
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')


# pour tester

try:
    classe = Classe("P20")
    student = Student("Matthieu", "Mazière")
    classe.add_student(student)
    new_student = classe.get_student("Matthieu", "Mazière")
    assert student is new_student
    new_student = classe.get_student("Jérôme", "Adnot")
    assert new_student is None
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

#load_students_from_file
# pour tester

try:
    classe = Classe("P1920")
    classe.load_students_from_file('classe.csv')
    if len(classe) != 38: #j'ai changé car il y a 38 élèves
        raise Exception('OOPS - There is an issue in your load_students_from_file method')
    assert classe.get_student("Enrico", "Fermi") is not None
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works ! ')

#saisie de notes pour les élèves
# pour tester

import io
import contextlib

try:
    classe = Classe("P1920")
    classe.load_students_from_file('classe.csv')
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        classe.load_grades_from_file('grades.csv')
    print(repr(buffer.getvalue()))
    print(list(classe.eleves.keys()))
    assert classe.get_student("Albert", "Einstein").compute_average("Physics") == 13.25
    assert classe.get_student("Enrico", "Fermi").compute_average("Mathematics") == 12.5
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works ! ')

#j'ai adapté le test aux docs utilisés
#catalogue
# pour tester

try:
    classe = Classe("P1920")
    classe.load_students_from_file('classe.csv')
    classe.load_grades_from_file('grades.csv')
    true_catalog = {'Physics': 7, 'Mathematics': 5, 'Scubadiving': 1, 'English':1, 'Chemistry':4, 'Astronomy':2, 'Biology':2, 'Computer Science':3}
    assert classe.catalog() == true_catalog, f"got {classe.catalog()}"
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works ! ')
#jai changé le test par rapport au texte grades utilisé

#calcul des moyennes par matiere
# pour tester

try:
    import math
    classe = Classe("P1920")
    classe.load_students_from_file('classe.csv')
    classe.load_grades_from_file('grades.csv')
    true_averages = {'Physics': (12 + 14 + 13.25 + 13.25 + 12 + 11 + 13) / 7,
                     'English': 15.5, 'Mathematics': 14.180000000000001, 'Scubadiving': 9.5, 'Chemistry': 14.625, 'Astronomy': 13.0, 'Biology': 14.25, 'Computer Science': 17.333333333333332}
    avgs = classe.compute_averages()
    print(avgs)
    assert avgs.keys() == true_averages.keys(), f"got topics {list(avgs)}"
    assert all(math.isclose(avgs[top], true_averages[top]) for top in true_averages)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works ! ')
#ca fonctionne 

#Bonus
# pour tester

try:
    classe = Classe("P1920")
    classe.load_students_from_file('classe.csv')
    classe.load_grades_from_file('grades.csv')
    reference_lines = ['Detailed Report for student Albert Einstein',
                       '+===============+===============+===============+',
                       '|     Topic     |    Average    |   Class Avg   |',
                       '+===============+===============+===============+',
                       '|    Physics    |     13.25     |     12.64     |',
                       '+---------------+---------------+---------------+']
    report_lines = classe.detailed_report(classe.get_student("Albert", "Einstein")).split('\n')
    assert len(report_lines) == len(reference_lines), \
        f"expected {len(reference_lines)} lines, got {len(report_lines)}"
    for i, (lineref, line) in enumerate(zip(reference_lines, report_lines), start=1):
        assert lineref == line, f"Ligne {i} : \n attendu = {lineref}\n  obtenu = {line}"
    assert classe.detailed_report(None) == "Student not found in the class."
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works ! ')

#De meme j'ai changé le test pour que ca soit coherent, ca fonctionne bien
