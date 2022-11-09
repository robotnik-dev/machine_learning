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
Anmerkung: ln(gewicht) nehmen wenn die Kosten Wahrscheinlichkeiten sind

# Vorlesung 2.11.22
## Themen
- Log Odds
- Grid Maps
- Bayes Filter
- Gauß Filter

# Vorlesung 9.11.22
## Partikel Filter(Localization)
particles = {(vec x_i, w_i)} - i= 1..N  
p_i = sum_i(w_i*delta_xi(x))  
## Sampling
Gleichverteilung bei Diskreten Werten
formal: x = 1/12 * sum(uniform(1,100)) -> N = 12  

## Resampling
Beudetung: Dort wo die Hypothese im Correction step gut war(höheres Gewicht) Werden mehr Partikel genommen

## Herangehensweise
1. messung
2. bewerten von Partikeln
3. neue Partikel setzen

- correction step
1. got measurement: z
2. evaluate particles(pi)-> calculate: weight(wi) Plausibilität des Particles überprüfen
3. resampling: set new particles(pi)
- prediction step
1. move particles(pi)  
p(x_t|x_t-1)  
x_t = x_t + u_t + n; n = rauschen(noise)  

## Roulette wheel Sampling (resampling)
1. create p1 with x1 (+ noise)  
zufällig
sinnvoll beim kidnapped robot problem
## Stochastic Universal Sampling(resampling)
statistisches resampling -> weniger RNG  
Im gleichen Abstand wieder gewählt

## Rao-Blackwellisation
p(a,b) = p(a) * p(b|a) -> p(x,m) = p(x) * p(m|x)  
x: Zustand, m: Karte  
Bayes rule kann angewandt werden um p(a) unabghängig von p(b|a) zu berechnen -> schnellere Berechnung  
fast SLAM: jeder Partikel führt seine eigene Karte mit sich(landmarks, gridmap)  

# Vision
## Computer Vision
data-> features -> result (classification, text, caption)  

## AI approach
data -> result

## Features
Keypoints(corner detection)  
codieren als vector (SIFT - Feature)  
Bild besteht aus der Vereinigungsmenge aller Vektoren  

## k-means / binarisieren
Cluster center finden. k muss am anfang festgelegt werden.  
gut für das binarisieren (k=2) 0 und 255  
gefundene cluster center benutzen als threshold für das binarisieren