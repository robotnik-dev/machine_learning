# Machnine Learning module BHT for learning purposes
# Literatur
[Probabilistic Robotics](https://docs.ufpr.br/~danielsantos/ProbabilisticRobotics.pdf)
# Vorlesung 19.10.22

## SLAM
V-SLAM  
keine Stereo Kamera  
Aus RGB Daten Depth Image!

### Versions
grid-based  
landmark-based  

Pfade - Integrale
Graphen based SLAM - Optimierung von Graphen

### Localization
uniform distirbution -> np.random.uniform  
t0 Belief -> uniform distiŕibution **prior**  
messen  
t1 **posterior** -> correction step  
bewegen - **Motion model**  
t2 prediction step  
messen ...  
### Motion Model
![](images/probabilistic.png)
![](images/motion_model.png)

### Observation Model
![](images/obervation_model.png)


# Axiome
- Sicheres Ereignis P = 1
- Unmögliches Ereigniss P = 0
- Summe aller Wahrscheinlichkeiten = 1
- Additionstheorem  
$$p(x \lor y) = p(x) + p(y) - p(x \land y) => p(x,y)$$
ODER
$$p(x \lor y) = p(x \land y) = 0$$
$$p(\lnot x) = 1 - p(x)$$
- Produktregel  
wahrscheinlichkeit x unter Bedingung, dass yi eingetreten ist  (Wahrscheinlichkeitbaum)  
$$p(x, yi) = p(x | y) * p(yi) = p(yi | x) * p(x)$$
- Bayes Rule  
$$p(x | y) =\frac{p(x | y) * p(x)}{p(y)}$$
p(x|y) -> posterior  
p(y|x) -> Likelyhood (Messung)  
p(x) -> prior  
p(y) -> Evidence (Normierung)  
![](images/bayesrule.png)
- Satz der totalen Wahrscheinlichkeit  
gesamt wahrscheinlichkeit ist die Summer aller vorherigen Wahrscheinlichkeiten (bsp. Lokalisierung )  
$$p(x) = \sum(p(x,yi)) = \sum(p(x|yi) * p(yi))$$

# Vorlesung 26.10.22
## Graphentheorie

## Definition
Knoten = V Vertices  
Kanten = E Edges  

Ein Graph G(V, E) ist ein Tupel der Menge $$V \neq \empty$$
der Knoten und der Menge E der Knoten.

Knoten:  
- Isoliert
- Eigengewicht = loop

Kanten:  
- Parallel

Graphen:  
- ungewichtet, gewichtet
- zusammenhängend, nicht zusammenhängend
- gerichtet, nicht gerichtet

Grad eines Knoten:  
Anzahl der Elemente(Kanten), die den Knoten beeinflussen
$$|\delta(a)|$$

Teilgraphen  
Teilmenge des ganzen Graphen

Aufgespannter Teilgraph  
Zusammenhang zwischen Teilgraphen (**alle Knoten**)  

### Kantenzüge, Wege, Kreise
Kantenzug  
Beliebige Kombination von Kanten die zu einem Ziel führen

Wege  
Beliebige Kombination aus Kanten zum Ziel wobei jeder Knoten nur einmal besucht werden darf

Kreis  
Ist ein Weg bei dem Start- und Endknoten gleich sind

### Zusammenhängender Graph
Falls es für alle Knoten(v,e ∈ V) einen v-w-Weg gibt

## Darstellung im Computer
Die Kante e=(v,w) verbindet die Knoten v und w
Die Knoten sind adjazent.
Sie sind Endpunkte der Kante e und damit inzident

### Adjazenzmatrix
Matrix aller Knoten mit den Kosten zu den jeweiligen Knoten

### Inzidenzmatrix
Matrix (1 oder 0) existiert Kante Verbindung zu Knoten:  
spalten = Kanten  
Reihen = Knoten  


$$\begin{equation*}

\begin{pmatrix}
1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & 1 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 \\
1 & 1 & 0 & 0 & 1 & 0 & 0 & 1 \\
0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\

\end{pmatrix}
\end{equation*}
$$

### Adjazenzliste
Liste aus allen benachbarten Kanten eines Knotens

## Elementare Datenstrukturen
- Stack
- Queue

## Suchen
- Breitensuche
- Tiefensuche


Dijkstra und A* Algortihmen
- ln(gewicht) nehmen wenn die Kosten Wahrscheinlichkeiten sind