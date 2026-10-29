# TP - Classes

dans ce TP on se définit deux classes, `Student` et `Classe`, pour gérer les notes d'une promotion

 

Notes importantes
- dans ce TP on utilise les ***types***: on indique fréquemment le type des paramètres, en écrivant par exemple  
  `add_grade(course: str, grade: float)` au lieu de `add_grade(course, grade)`  
  ou encore `def foo(s: str) -> bool:` au lieu de `def foo(s):`

- une classe est définie par des **attributs** (des données) et des **méthodes**; une méthode est une fonction écrite spécialement pour s'appliquer à une instance de la classe, et elle a **toujours `self` comme premier paramètre**; cela permet l'appel `instance.methode(arguments)`  
  par exemple, pour ajouter `add_grade` à `Student`, vous écrirez quelque chose comme

  ```python
  class Student:
      ...
      def add_grade(self, course: str, grade: float):
          # votre code
          pass
  ```

Les notions au coeur de ce TP
- définir une classe: `__init__`, attributs, méthodes, `self`
- les **méthodes spéciales** `__repr__` et `__len__`, appelées par `repr()` et `len()`
- choisir le bon **conteneur** pour stocker les données (`dict`, `defaultdict(list)`)
- une classe qui **contient** des objets d'une autre classe (`Classe` contient des `Student`)
- valider les données et lever des **exceptions** (`ValueError`)
- lire un fichier CSV et formater du texte (alignements `:^15`, `:>6.2f`)

 

## échauffement : la notion de classe

avant de se lancer dans le TP, on s'assure qu'on a bien en tête ce qu'est une classe

Rappel


- une **classe** est un plan de construction ; une **instance** (ou objet) est un exemplaire construit à partir de ce plan  
  `p = Point(3, 4)` crée une instance de la classe `Point`
- `Point(3, 4)` appelle la méthode spéciale **`__init__`**, qui initialise les **attributs** de l'instance, en écrivant `self.x = ...`
- `self` désigne *l'instance sur laquelle on travaille* ; deux instances de la même classe ont chacune leurs propres attributs
- les **méthodes spéciales** (celles dont le nom est entouré de `__`) sont appelées indirectement par Python:

  | vous écrivez | Python appelle |
  |---|---|
  | `Point(3, 4)` | `__init__` |
  | `repr(p)`, ou l'affichage d'`p` dans la console | `__repr__` |
  | `len(t)` | `__len__` |
 

### Echauffement 1 : une première classe

**Énoncé :** écrivez une classe `Point` qui
- se construit avec `Point(x, y)`
- possède une méthode `norm()` qui retourne la distance à l'origine
- s'affiche sous la forme `Point(3, 4)`

```{code-cell} ipython3

# votre code

class Point:
    pass
```

```{code-cell} ipython3

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
```

<details>
<summary><b>Indice 1 : le constructeur</b></summary>

`__init__(self, x, y)` doit ranger ses paramètres dans des attributs de `self`: `self.x = x`
</details>

<details>
<summary><b>Indice 2 : norm et repr</b></summary>

`norm()` n'a pas besoin d'autre paramètre que `self`, puisqu'elle lit `self.x` et `self.y`  
pour la distance, pensez à Pythagore (ou à `math.hypot`)  
`__repr__` doit **retourner** une chaine (pas l'afficher avec `print`)
</details>

### échauffement 2 : à propos de `self`

```{code-cell} ipython3
p = Point(3, 4)
```

**Questions :**
1. `p.norm()` et `Point.norm(p)` donnent-ils le même résultat ?
2. que se passe-t-il si on écrit `def norm():` dans la classe, sans `self`, puis qu'on appelle `p.norm()` ?
3. que s'affiche-t-il avec `print(p)` si la classe n'a pas de `__repr__` ?

### échauffement 3 : le piège de l'attribut partagé

que va afficher le code suivant ? réfléchissez avant de l'exécuter

```{code-cell} ipython3
class Bad:
    items = []

    def add(self, x):
        self.items.append(x)

a, b = Bad(), Bad()
a.add(1)
print(b.items)
```

**Questions :**
1. pourquoi `b` voit-il l'élément ajouté à `a` ?
2. comment corriger la classe pour que chaque instance ait sa propre liste ?

### échauffement 4 : une classe qui contient des valeurs

**Énoncé :** écrivez une classe `Tirelire` qui
- se construit sans argument, avec une liste de pièces vide
- possède une méthode `deposit(value: float)` qui ajoute une pièce ; une valeur négative ou nulle doit lever une `ValueError`
- possède une méthode `total()` qui retourne la somme des pièces
- permet d'écrire `len(t)` pour obtenir le **nombre de pièces**
- s'affiche sous la forme `Tirelire(2 coins, total=1.50)`

```{code-cell} ipython3
# votre code

class Tirelire:
    pass
```

```{code-cell} ipython3
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
```

<details>
<summary><b>Indice 1 : le conteneur</b></summary>

où doit-on créer la liste de pièces pour que deux tirelires soient indépendantes ? (voir l'échauffement 3)
</details>

<details>
<summary><b>Indice 2 : len et la validation</b></summary>

`len(t)` appelle `t.__len__()`, qui doit retourner un entier  
pour la validation, on teste la valeur au début de `deposit`, et on fait `raise ValueError("...")` si elle est incorrecte
</details>


***

 

## la classe `Student`

nous allons commencer par créer une classe `Student` qui permet d'instancier des étudiants; le noyau de la classe est le suivant

```{code-cell} ipython3
# votre code

from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        pass

    def __repr__(self):
        pass
```

### constructeur et `__repr__`

- `__init__` doit conserver le prénom et le nom
- `__repr__` doit retourner une chaine qui contient le prénom, le nom, et les notes de l'élève; par exemple  
  `Student(Achille Talon, Grades: {})`

```{code-cell} ipython3
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
```

<details>
<summary><b>Indice</b></summary>

dans `__init__`, rangez au minimum `first_name` et `last_name` dans des attributs  
pour les notes, on y reviendra à l'étape suivante, mais vous pouvez déjà créer l'attribut dans `__init__`
</details>


### gestion des notes

#### `add_grade`

nous souhaitons maintenant ajouter des notes à cet élève; implémentez la méthode `add_grade(course: str, grade: float)`  
une note doit être comprise entre 0 et 20; sinon la méthode doit lever une `ValueError`

**Note :** pour stocker les notes de l'élève il faut un attribut; prenez le temps de réfléchir au conteneur le plus approprié

```{code-cell} ipython3
 

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
```

<details>
<summary><b>Indice 1 : le conteneur</b></summary>

on veut associer **à chaque matière** une **liste de notes** : quel type de conteneur associe une clé à une valeur ?  
et puisqu'une matière n'a pas de notes au départ, pensez à `defaultdict(list)` : la liste est créée automatiquement la première fois qu'on utilise la clé
</details>

<details>
<summary><b>Indice 2 : la validation</b></summary>

un test chainé `0 <= grade <= 20` fonctionne en Python
</details>

#### `followed_topics`

maintenant, nous aimerions savoir quelles matières suit un élève *via* la méthode `followed_topics()`, qui renvoie un itérable (une liste par exemple)

```{code-cell} ipython3
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
```

<details>
<summary><b>Indice</b></summary>

les matières suivies sont les clés du conteneur des notes
</details>

#### `compute_average`

nous voudrions calculer la moyenne de l'élève pour une matière donnée; implémentez la méthode `compute_average(course: str)`  
si l'élève n'a pas de note dans la matière demandée, la méthode lève une `ValueError`

Attention au defaultdict !
un `defaultdict` a un comportement surprenant: **lire** une clé absente, comme dans `self.grades["French"]`, **crée** cette clé !  
que se passerait-il alors dans `followed_topics()` ? c'est ce que le test ci-dessous vérifie

```{code-cell} ipython3
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
```

<details>
<summary><b>Indice 1 : le cas sans note</b></summary>

testez **d'abord** si la matière est suivie, avec `course in self.grades` : l'opérateur `in` sur un dictionnaire ne crée pas la clé
</details>

<details>
<summary><b>Indice 2 : la moyenne</b></summary>

`sum(...) / len(...)` sur la liste des notes de la matière
</details>

### `report`

finalement, il ne manque plus qu'à afficher à l'écran le bulletin de l'élève, en codant la méthode `report()` qui **renvoie** la chaine de caractères qui s'affiche comme suit

```text
Report for student Albert Einstein
+===============+===============+
|     Topic     |    Average    |
+===============+===============+
|   Chemistry   |     11.33     |
+---------------+---------------+
|    English    |     14.00     |
+---------------+---------------+
|    Physics    |     13.25     |
+---------------+---------------+
|    French     |     11.50     |
+---------------+---------------+
|  Mathematics  |     12.80     |
+---------------+---------------+
|  Scubadiving  |     12.50     |
+---------------+---------------+
```

```{code-cell} ipython3
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
```

<details>
<summary><b>Indice 1 : construire la chaine</b></summary>

construisez une **liste de lignes**, puis assemblez-la à la fin avec `"\n".join(lines)`  
l'en-tête (4 lignes) est toujours le même ; ensuite, il y a **deux lignes par matière**: la ligne de données, puis la ligne de séparation en `+---`
</details>

<details>
<summary><b>Indice 2 : l'alignement</b></summary>

les spécifications de format des f-strings permettent d'aligner:
- `{topic:^15}`: centré sur 15 caractères
- `{average:>6.2f}`: aligné à droite sur 6 caractères, avec 2 décimales

les colonnes font 15 caractères de large, entre les `|`
</details>
 

***

 

## la classe `Classe`

nous allons maintenant gérer un ensemble d'élèves dans l'objet `Classe`

```{code-cell} ipython3
# votre code

class Classe:
    def __init__(self, classname: str):
        pass

    def add_student(self, student: Student):
        pass

    def __len__(self):
        return 0

    def __repr__(self):
        return ""
```

### premières méthodes

implémentez les méthodes dont les prototypes sont donnés dans la cellule précédente
- `len(classe)` doit retourner le nombre d'élèves
- `repr(classe)` doit contenir le nom de la classe et les élèves; par exemple  
  `Class(P20, Students: [Student(Matthieu Mazière, Grades: {})])`

**Note :** nous aurons besoin par la suite de savoir rapidement si un élève est dans la classe et d'y accéder; évitez donc de stocker les élèves dans une simple liste

```{code-cell} ipython3
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
```

<details>
<summary><b>Indice 1 : le conteneur</b></summary>

On veut retrouver un élève à partir de son prénom et de son nom, **sans parcourir toute la liste**  
quel conteneur permet un accès direct à partir d'une clé ? et que peut-on utiliser comme clé, sachant que deux élèves peuvent avoir le même prénom, ou le même nom ?  
(un tuple `(first_name, last_name)` est hashable, donc utilisable comme clé)
</details>

<details>
<summary><b>Indice 2 : le repr</b></summary>

si vous stockez les élèves dans un dictionnaire, pensez à `list(d.values())` pour afficher uniquement les élèves
</details>

Stocker les élèves dans une liste fonctionne aussi, mais `get_student` doit alors parcourir toute la liste (complexité linéaire), alors qu'avec un dictionnaire l'accès est direct
</details>

### Accès à un élève

Nous aimerions pouvoir accéder très facilement à un élève de la classe; pour cela, codez la méthode `get_student(first_name: str, last_name: str)` qui retourne l'élève, ou `None` s'il n'est pas dans la classe

```{code-cell} ipython3
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
```

<details>
<summary><b>Indice</b></summary>

La méthode `get` d'un dictionnaire retourne `None` quand la clé est absente
</details>

### Initialisons la classe à partir d'un fichier

On se place dans le cas où l'effectif d'une classe est défini dans un fichier csv; chaque ligne de ce fichier contient le prénom et le nom d'un élève. Implémentez la méthode `load_students_from_file(filename: str)` qui permet de remplir la classe pour tester.

```{code-cell} ipython3
# pour tester

try:
    classe = Classe("P1920")
    classe.load_students_from_file('classe.csv')
    if len(classe) != 3:
        raise Exception('OOPS - There is an issue in your load_students_from_file method')
    assert classe.get_student("Enrico", "Fermi") is not None
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works ! ')
```

<details>
<summary><b>Indice 1 : lire le fichier</b></summary>

on ouvre le fichier avec `open(filename, 'r', encoding='utf-8')`, de préférence dans un `with`, et on itère directement sur le fichier : on obtient une ligne à chaque tour.
Le 'r' indique qu'on oubre le fichier en mode'read' seulement et l'encoding précise l'encodage utilisé pour interpréter les caractères du fichier, notamment les accents et les caractères spéciaux. Par défault c'est utf-8 mais sur certain config ce n'est pas le cas donc par experience, on va assumer le pire ... 
</details>

<details>
<summary><b>Indice 2 : découper une ligne</b></summary>

`line.strip().split(',')` retire le retour à la ligne, puis découpe suivant les virgules  
puis il suffit de créer un `Student` et de l'ajouter avec la méthode déjà écrite
</details>


### Saisie de notes pour les élèves

Nous allons maintenant rentrer les notes des élèves pour les différentes matières; cette saisie se fait aussi *via* un fichier csv, dont chaque ligne est découpée comme suit

`Prénom,Nom,Matière,Note1,Note2,...,NoteN`

le nombre de notes dépend de la matière, et tous les élèves ne suivent pas les mêmes cours; implémentez la méthode `load_grades_from_file(filename: str)` qui affecte à chaque élève ses notes

**Note :** si on souhaite attribuer une note à un élève qui n'est pas dans la classe, il ne faut **pas** lever d'exception, mais seulement **imprimer un message d'avertissement** qui contient le nom de l'élève

```{code-cell} ipython3
# pour tester

import io
import contextlib

try:
    classe = Classe("P1920")
    classe.load_students_from_file('classe-test.csv')
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        classe.load_grades_from_file('grades-test.csv')
    assert "Personne" in buffer.getvalue(), "no warning printed for the unknown student"
    assert classe.get_student("Albert", "Einstein").compute_average("Physics") == 15.
    assert classe.get_student("Albert", "Einstein").compute_average("Mathematics") == 13.
    assert classe.get_student("Enrico", "Fermi").compute_average("Scubadiving") == 9.5
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works ! ')
```

<details>
<summary><b>Indice 1 : découper la ligne</b></summary>

les trois premiers morceaux sont le prénom, le nom et la matière ; **tous les autres** sont des notes, sous forme de chaines  
`list(map(float, parts[3:]))` les convertit en flottants
</details>

<details>
<summary><b>Indice 2 : l'élève inconnu</b></summary>

`get_student` retourne `None` pour un élève absent: c'est le moment d'afficher l'avertissement, puis de passer à la ligne suivante (`continue`)  
pour chaque note, il suffit ensuite de réutiliser `add_grade`
</details>

### catalogue des matières suivies par les élèves de la classe

implémentez la méthode `catalog()` qui renvoie un dictionnaire dont les clés sont les noms des matières, et les valeurs le nombre d'élèves qui suivent chaque cours

```{code-cell} ipython3
# pour tester

try:
    classe = Classe("P1920")
    classe.load_students_from_file('classe-test.csv')
    classe.load_grades_from_file('grades-test.csv')
    true_catalog = {'Physics': 3, 'Mathematics': 2, 'Scubadiving': 1}
    assert classe.catalog() == true_catalog, f"got {classe.catalog()}"
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works ! ')
```

<details>
<summary><b>Indice</b></summary>

on parcourt les élèves, puis les matières de chaque élève (`followed_topics()`), et on incrémente un compteur par matière  
pour éviter de tester à chaque fois si la clé existe déjà, vous pouvez utiliser `dict.get(key, 0)`, ou un `defaultdict(int)`, ou encore un `collections.Counter`
</details>

### Calcul des moyennes par matière

Nous allons maintenant calculer la moyenne de la classe par matière; codez la méthode `compute_averages()` qui retourne un dictionnaire dont les clés sont les matières, et les valeurs la moyenne de la classe. On convient que la moyenne de la classe pour une matière est la **moyenne des moyennes** des élèves qui suivent cette matière

```{code-cell} ipython3
# pour tester

try:
    import math
    classe = Classe("P1920")
    classe.load_students_from_file('classe-test.csv')
    classe.load_grades_from_file('grades-test.csv')
    true_averages = {'Physics': (15 + 11 + 18) / 3,
                     'Mathematics': (13 + 15) / 2,
                     'Scubadiving': 9.5}
    avgs = classe.compute_averages()
    assert avgs.keys() == true_averages.keys(), f"got topics {list(avgs)}"
    assert all(math.isclose(avgs[top], true_averages[top]) for top in true_averages)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works ! ')
```

<details>
<summary><b>Indice</b></summary>

même principe que `catalog()`, mais il faut cette fois conserver **deux** informations par matière: la somme des moyennes, et le nombre d'élèves  
(et ne pas oublier la division à la fin)  
la méthode `compute_average(course)` de `Student` fait déjà le travail pour chaque élève
</details>
 

## Bonus 

Répercutez les informations de la classe sur le bulletin de l'élève: écrivez la méthode `detailed_report(student: Student | None)` de la classe `Classe`, qui renvoie un bulletin avec en plus **la moyenne de la classe** pour chaque matière

si l'élève est `None`, la méthode retourne la chaine `"Student not found in the class."`

```text
Detailed Report for student Albert Einstein
+===============+===============+===============+
|     Topic     |    Average    |   Class Avg   |
+===============+===============+===============+
|    Physics    |     15.00     |     14.67     |
+---------------+---------------+---------------+
|  Mathematics  |     13.00     |     14.00     |
+---------------+---------------+---------------+
```

```{code-cell} ipython3
# pour tester

try:
    classe = Classe("P1920")
    classe.load_students_from_file('classe-test.csv')
    classe.load_grades_from_file('grades-test.csv')
    reference_lines = ['Detailed Report for student Albert Einstein',
                       '+===============+===============+===============+',
                       '|     Topic     |    Average    |   Class Avg   |',
                       '+===============+===============+===============+',
                       '|    Physics    |     15.00     |     14.67     |',
                       '+---------------+---------------+---------------+',
                       '|  Mathematics  |     13.00     |     14.00     |',
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
```

<details>
<summary><b>Indice</b></summary>
c'est `report()` avec une colonne de plus: la moyenne de la classe pour chaque matière, qu'on obtient avec `compute_averages()`  
attention à ne l'appeler **qu'une fois**, en dehors de la boucle sur les matières
</details>

D'autres idées pour aller plus loin: afficher aussi le nombre d'élèves qui suivent chaque cours, ou le **rang** de l'élève dans la classe pour chaque matière