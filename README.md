***Enhancing Urban EV Charging Networks: A Case Study of Bhubaneswar***

Debani Prasad Mishra\
*Department of Electrical & Electronics Engineering*\
*IIIT Bhubaneswar\
*Odisha, India

[debani@iiit-bh.ac.in]{.underline}

Subham Kumar Bisoyi\
*Department of Electrical & Electronics Engineering*\
*IIIT Bhubaneswar\
*Odisha, India\
[b323044@iiit-bh.ac.in]{.underline} [\
]{.underline}Animesh Sharma\
*Department of Electrical & Electronics Engineering*\
*IIIT Bhubaneswar\
*Odisha, India\
[b323007@iiit-bh.ac.in]{.underline}

Kumar Gaurav\
*Department of Electrical & Electronics Engineering*\
*IIIT Bhubaneswar\
*Odisha, India\
[b323018@iiit-bh.ac.in]{.underline}

***Abstract*---** ***As electric vehicles (EVs) continue to gain
popularity across India---particularly in emerging urban centers like
Bhubaneswar---the demand for an efficient and well-distributed charging
network is becoming increasingly critical. This research introduces a
structured approach to strategically placing EV charging stations
throughout Bhubaneswar, Odisha. The methodology integrates geospatial
tools like QGIS for mapping and analysis, while using Gaussian Mixture
Models (GMM) to identify high-demand clusters. It further applies
advanced optimization techniques, including Particle Swarm Optimization
(PSO) and the Shortest Distance Method (SDM), to refine location
choices. Key practical factors---such as proximity to power
infrastructure, adequate spacing between stations, and regional service
coverage---are also incorporated. The result is a scalable, data-driven
model tailored to meet Bhubaneswar's specific transportation and energy
needs.***

***Keywords--- electric vehicle charging station; optimal location;
gaussian mixture model; particle swarm optimization; shortest distance
method.***

#  Introduction 

Bhubaneswar, home to over 1.2 million people, is experiencing a
noticeable surge in electric vehicle (EV) adoption as more residents
shift toward sustainable mobility. However, the city's existing
infrastructure is struggling to keep pace. At present, there are only 18
public EV charging stations available to serve more than 2,300 EVs,
resulting in an average of over 140 vehicles per station. This figure is
well above the globally recommended range of 10 to 50 EVs per charging
point, highlighting a significant infrastructure gap.

This imbalance is especially evident in busy urban areas like Master
Canteen, Khandagiri, and Vani Vihar, where long queues and extended wait
times at charging points have become increasingly common. In contrast,
cities such as Bangalore and Delhi have made considerable progress,
maintaining healthier EV-to-charger ratios---approximately 1:60 in
Bangalore and 1:43 in Delhi, thereby offering a smoother user
experience.

To address this growing disparity and support Bhubaneswar's green
mobility goals, this study adopts a multi-method approach aimed at
identifying 20 optimal new locations for EV charging stations across the
city

The approach integrates:

-   **Gaussian Mixture Model (GMM)** to cluster areas based on EV demand

-   **Particle Swarm Optimization (PSO)** for determining optimal site
    > placement

-   **Shortest Distance Method (SDM)** to ensure accessibility and
    > coverage across key urban zones

-   **QGIS** for detailed geospatial visualization and analysis

#  Methodology

A.  *Gaussian Mixture Method for Demand Zone Analysis in Bhubaneswar*

Gaussian Mixture Model (GMM) is a robust probabilistic clustering method
that models a dataset as a weighted combination of multiple Gaussian
(normal) distributions. It is particularly well-suited for identifying
latent and overlapping structures within complex spatial data---an
essential requirement in electric vehicle (EV) infrastructure planning
\[1\]. In real-world urban environments, factors like population
density, vehicular movement, and user trip behaviors often follow
non-linear and overlapping patterns that cannot be effectively captured
using traditional clustering techniques such as K-means, which rely on
rigid, hard boundaries.GMM overcomes this limitation by employing soft
clustering, where each data point is assigned a probability of belonging
to each cluster, rather than being forced into a single one. This
probabilistic nature allows GMM to reflect real-world uncertainty and
spatial ambiguity more accurately---critical for modeling demand
hotspots where usage patterns may shift throughout the day or vary based
on transient events like holidays or traffic disruptions \[2\].

The clustering process is powered by the Expectation-Maximization (EM)
algorithm, an iterative optimization technique that alternates between
estimating the expected cluster memberships (E-step) and updating the
Gaussian parameters (means, variances, and mixing coefficients) to
maximize the likelihood of the data (M-step) \[3\]. Through this
process, GMM automatically determines the optimal number of Gaussian
components that best represent the data\'s underlying structure. Each
component corresponds to a potential demand zone, with its own spatial
center, spread,

  ---------------------------------------------------------------------------
  **S.No**   **Name**                 **Location**         **Coordinates**
  ---------- ------------------------ -------------------- ------------------
  1          Tata Power -- Dion       Lewis Road,          20.2245° N,
             Automotives              Samantarapur, Old    85.8330° E
                                      Town                 

  2          Tata Power -- MG         Pahala, NH-16        20.3347° N,
             Bhubaneswar                                   85.8038° E

  3          TML Tirupati Enterprises Bhagabanpur          20.2961° N,
                                      Industrial Area      85.8194° E

  4          Tata Power -- Regalia    Bhagabanpur          20.2961° N,
             Mall (DN Square)         Industrial Estate    85.8194° E

  5          Tata Power -- GUGNANI    CRP -- DAV Road,     20.2961° N,
             TYRES                    Nilakantha Nagar,    85.8194° E
                                      Nayapalli            

  6          Tata Power -- DN Wisdom  K-2, Kalinganagar    20.2961° N,
             Tree                                          85.8194° E

  7          Tata Power -- BMC        Saheed Nagar         20.2961° N,
             Bhawani Mall                                  85.8194° E

  8          Tata Power -- MLCP       Plot No.150(P),      20.2961° N,
             Saheed Nagar             Saheed Nagar         85.8194° E

  9          Tata Power -- GUGNANI    Mancheswar           20.2961° N,
             AUTOCARS                 Industrial Estate,   85.8194° E
                                      Sector A, Block C    

  10         Tata Power -- CSM        OCAC Building,       20.2961° N,
             Technologies             Acharya Vihar,       85.8194° E

  11         Tata Power -- DN Group   VIP Colony, IRC      20.2961° N,
             Corporate                Village, Nayapalli   85.8194° E

  12         Kazam -- Rasulgarh       Rasulgarh            20.2961° N,
                                                           85.8194° E

  13         Tata Power -- Audi       Utkal Signature,     20.2961° N,
             Bhubaneswar              NH16                 85.8194° E

  14         HPCL -- Regional Office  7RRW M8H, Saheed     20.2961° N,
                                      Nagar                85.8194° E

  15         Charger -- Geetanjali    Service Road West,   20.2961° N,
                                      Acharya Vihar        85.8194° E

  16         GLIDA DLF Bhubaneswar -- Idco Info Park       20.2961° N,
             Statiq                                        85.8194° E

  17         Statiq -- Nexus          Unit No. 32,         20.2961° N,
             Esplanade                721,Rasulgarh        85.8194° E

  18         Statiq -- Yellowings ITC ITC Cuttack          20.2961° N,
             Cuttack Station                               85.8194° E
  ---------------------------------------------------------------------------

1.  [Current Locations of EV Charging Stations]{.smallcaps}

and weight \[4\]. Rather than forcing strict cluster boundaries, GMM
estimates the probability distribution of demand across the urban
landscape. The final solution---often taken as the weighted average or
centroid of the Gaussian means---represents high-demand regions that are
central, statistically significant, and likely to support infrastructure
placement. This approach enables planners to prioritize station
locations that best reflect aggregate user behavior while accounting for
uncertainty and data noise \[5\].

Compared to conventional clustering models, GMM excels in environments
where the data is non-uniform, noisy, or spatially complex. For example,
in EV infrastructure planning, charging demand may cluster near
commercial zones during the day and shift toward residential areas at
night. GMM's flexibility in adapting to variations in variance, density,
and orientation of clusters allows it to model such transitions more
effectively than rigid methods \[6\]. It is particularly effective when
used with spatiotemporal data collected from real-world sensors,
surveys, and trip logs.Studies have demonstrated that GMM-based
clustering yields significantly higher accuracy and predictive
reliability, especially in high-dimensional urban datasets \[7\] . When
integrated with downstream optimization algorithms like Particle Swarm
Optimization (PSO), GMM provides a nuanced and informative input space,
enhancing the overall performance of the optimization process. PSO, in
turn, benefits from this probabilistic representation by directing
search efforts toward the most relevant and statistically supported
regions, thereby improving both solution quality and computational
efficiency \[8\].

In summary, GMM serves as a foundational tool in modern EV
infrastructure planning, enabling adaptive, data-driven decisions in
dynamic urban contexts. Its ability to handle ambiguity, represent
overlapping clusters, and model demand with high fidelity makes it
indispensable in the broader pipeline of intelligent mobility and energy
systems design.

A GMM models the data as a mixture of several Gaussian distributions.
The probability density of a data point x, which is a D-dimensional
feature vector, is expressed through the likelihood function
$p\left( \left. \ x \right|\lambda \right)$:

$$p\left( \left. \ x \right|\lambda \right) = \sum_{k = 1}^{M}{\binom{n}{k}\omega_{k}p_{k}(x)}$$

Here, $M$ represents the number of Gaussian components. Each component
$p_{k}(x)$ is a Gaussian distribution defined by a mean vector
$\mu_{k}$, a $D \times D$ covariance matrix $\Sigma_{k}$, and a mixture
weight $\omega_{k}$.

The form of each Gaussian component is:

$$p_{k}(x) = \frac{1}{(2\pi)^{D/2}\left| \Sigma_{k} \right|^{1/2}}exp\left\{ - \frac{1}{2}\left( x - \mu_{k} \right)^{T}\Sigma_{k}^{- 1}\left( x - \mu_{k} \right) \right\}$$

The mixture weights $\omega_{k}$ are constrained to sum to 1:
$\sum_{k = 1}^{M}\mspace{2mu}\omega k = 1$. The model parameters are
denoted as $\lambda = \left\{ \omega_{k},\mu_{k},\Sigma_{k} \right\}$,
with $k$ ranging from 1 to $M$.

For a dataset of $N$ independent observations $x_{i}$, where
$i = 1,\ldots,N$, the likelihood of the data given the parameters
$\theta$ is:

$$p(x \mid \theta) = L(\theta \mid x) = \prod_{i = 1}^{N}\mspace{2mu}\sum_{k = 1}^{M}\mspace{2mu}\alpha_{k}pk\left( x_{i} \mid \theta_{k} \right)$$

The optimal parameters $\theta$ are found using the Maximum Likelihood
Estimate (MLE), which maximizes the likelihood:

$$\theta^{*} = arg\max_{\theta}\mspace{2mu} L(\theta \mid x)$$

The likelihood function $p(x \mid \lambda)$ must be carefully chosen to
highlight features that enhance the distinction between likelihood
ratios, thereby improving the GMM\'s clustering effectiveness.

**Clustering Inputs and Methodology:**

The clustering approach using Gaussian Mixture Model (GMM) was designed
around six input variables that represent key spatial and behavioral
indicators relevant to EV infrastructure planning:

-   **EV Count** -- This variable estimates the average daily number of
    electric vehicles in a particular locality. It directly reflects
    potential charging demand. High EV Count areas are prioritized for
    infrastructure deployment due to their consistent usage patterns.

-   **Traffic Score** -- Represents the density and intensity of
    vehicular traffic across urban regions. High traffic areas imply
    frequent road usage, which correlates with increased EV activity and
    battery usage, making these zones more likely to require charging
    support.

-   **Footfall Score** -- Captures pedestrian activity in a given zone.
    Areas with high footfall typically host commercial or transit
    facilities where EVs are likely to park or idle, presenting ideal
    conditions for charger placement.

-   **Distance From Grid** -- Measures proximity to the existing
    electrical grid. Areas closer to the grid are more favorable due to
    lower installation costs and simpler connectivity, making this a
    critical infrastructural constraint in site selection.

-   **Latitude and Longitude** -- These geospatial coordinates help map
    the physical location of each area, enabling spatially aware
    clustering. This prevents over-concentration of stations and ensures
    even distribution across the city.

-   **GMM Clustering Logic** -- GMM applies a soft clustering approach,
    allowing each area to belong probabilistically to multiple clusters.
    This captures overlapping demand patterns more effectively than hard
    clustering. The model iteratively determines the optimal number and
    parameters of Gaussian components, ultimately identifying zones with
    the highest likelihood of EV charging demand.

These variables were first normalized to ensure uniformity in scale and
were then processed through the GMM algorithm. GMM assigns each data
point (or location) to a probabilistic cluster by evaluating
similarities across both behavioural patterns (like demand or usage
intensity) and geographical context. Unlike rigid clustering algorithms
that enforce strict boundaries, GMM allows for overlap, making it ideal
for cities where urban functions often blend together \[4\].

The GMM analysis produced four distinct clusters, each representing a
different type of location based on the input features:

**Cluster 0:** Areas with high EV counts, significant traffic, and close
proximity to the grid, making them ideal urban locations for charging
stations.

**Cluster 1:** Locations with moderate EV presence and footfall, and a
moderate distance from the grid, indicating balanced charging demand.

**Cluster 2:** Regions with low EV counts and traffic, and greater
distance from the grid, marking them as low-priority rural or peripheral
areas.

**Cluster 3:** Areas with high footfall, moderate EV presence, and
proximity to the grid, suitable for commercial or transit-focused
locations.

The table below summarizes the locations analyzed, their assigned
clusters, EV counts, and distances from the grid:

2.  CLUSTER SUMMARY TABLE

  -----------------------------------------------------------------------------
  ***Cluster***   **Zone/Location**           **EV Count**   **Distance from
                                                             Grid (km)**
  --------------- --------------------------- -------------- ------------------
  *0*             Saheed Nagar                105            1.2

  *0*             Vani Vihar                  85             1.5

  *0*             Jaydev Vihar                72             2.0

  *0*             Satya Nagar                 57             1.8

  *0*             Tankapani Road              51             2.7

  *0*             Sishu Bhawan                47             2.1

  *1*             Nayapalli                   78             3.4

  *1*             Palasuni                    54             3.9

  *1*             Pokhariput                  50             4.3

  *1*             Badagada                    44             3.0

  *2*             Jagamara                    56             5.7

  *2*             Mancheswar                  46             4.9

  *2*             Kalinga Stadium             45             5.2

  *3*             KIIT                        60             6.8

  *3*             Chandrasekharpur            58             6.4
  -----------------------------------------------------------------------------

## Optimization with Particle Swarm Optimization (PSO)

Particle Swarm Optimization (PSO) is a computational technique inspired
by the social behavior of birds and fish, where individual particles
explore a problem space by adjusting their positions based on their own
and their neighbors\' best experiences.

Particle Swarm Optimization (PSO) is a powerful metaheuristic algorithm
inspired by the social behavior patterns observed in birds flocking and
fish schooling. In this method, individual particles---representing
potential solutions---continuously update their positions within the
solution space by considering both their own best-known positions and
those of neighboring particles . This social-cognitive learning
mechanism allows the swarm to converge rapidly toward optimal or
near-optimal solutions, even in high-dimensional and multi-objective
problem spaces \[9\] .In the context of electric vehicle (EV)
infrastructure planning, PSO proves exceptionally valuable for solving
complex problems involving dynamic constraints such as optimal placement
of charging stations, real-time load distribution, and adaptive energy
management. It balances conflicting objectives---such as minimizing user
distance, ensuring cost-effectiveness, and maximizing grid
performance---while also ensuring compliance with policy and practical
implementation limits \[10\].

The optimization process is initiated by constructing a spatially rich
dataset, incorporating layers like traffic density, road connectivity,
power grid reach, and land-use zoning through Geographic Information
Systems (GIS) such as QGIS. Each particle in the swarm represents a
potential configuration of charging station locations, and the fitness
function evaluates these configurations based on a set of performance
metrics, including average user distance to stations, demand-weighted
proximity, load balancing across grid zones, and route accessibility
\[11\] . This ensures that the proposed configurations are not only
mathematically optimal but also practically viable and policy-aligned
.To improve the model's realism, a Gaussian Mixture Model (GMM) is
integrated to simulate user mobility patterns and identify probabilistic
demand hotspots. Unlike static zoning, GMM-based clustering adapts to
dynamic population flows, assigning higher priority (or weight) to
locations with higher predicted demand. This results in a more
responsive and intelligent PSO search behavior that naturally gravitates
toward high-traffic areas, improving the system\'s real-world efficiency
\[12\].

Furthermore, PSO is adapted to fine-tune charging protocols, including
dynamic adjustments of Constant Current Constant Voltage (CCCV)
parameters. By optimizing the interplay between current and voltage
delivery, PSO ensures minimized charging times while maintaining battery
health, thus improving user experience and extending battery life \[13\]
.A significant enhancement to this framework is the integration of the
Spatial Durbin Model (SDM). SDM accounts for spatial autocorrelation and
spillover effects, meaning the installation of a new charging station in
one region can impact not only local demand but also influence the
performance and utility of stations in adjacent zones \[14\] . By
embedding SDM-derived spatial feedback into the PSO fitness function,
the algorithm becomes sensitive to regional interdependencies, enabling
it to avoid over-saturating one zone while neglecting nearby underserved
regions. This spatial intelligence enhances the macro-level
decision-making capabilities of the system \[15\].

+---------------------------+------------------------------------------+
| PSO ALGORITHM             |                                          |
| PSEUDOCODE**:**           |                                          |
+===========================+==========================================+
| INPUT f, swarm_size,      | FOR i = 1 TO max_iter:                   |
| max_iter                  |                                          |
|                           | FOR particle IN swarm:                   |
| INIT swarm positions,     |                                          |
| velocities                | fitness = f(particle.pos)                |
|                           |                                          |
| best_global = best        | IF fitness \< particle.best_fitness:     |
| position in swarm         |                                          |
|                           | particle.best_pos = particle.pos         |
|                           |                                          |
|                           | particle.best_fitness = fitness          |
|                           |                                          |
|                           | IF fitness \< best_global.fitness:       |
|                           |                                          |
|                           | best_global = particle.pos               |
|                           |                                          |
|                           | UPDATE particle.velocity                 |
|                           |                                          |
|                           | UPDATE particle.pos                      |
+---------------------------+------------------------------------------+

In summary, the collaborative integration of PSO, QGIS, GMM, and SDM
enables a comprehensive and scalable optimization framework. It handles
both micro-level efficiencies--- such as individual station performance,
user wait times, and routing convenience---and macro-level objectives,
like equitable access, long-term scalability, and grid impact
management. This multi-disciplinary approach exemplifies how swarm
intelligence, spatial analytics, and machine learning can be combined to
create smart, adaptive, and sustainable EV charging ecosystems.

Top 5 PSO Combinations (All 33 Stations)

**Combination 1 (Fitness 0.6598)**

\[\'Saheed Nagar\', \'Charger -- Geetanjali\', \'Tata Power -- BMC
Bhawani Mall\', \'Tata Power -- Dion Automotives\', \'HPCL -- Regional
Office\', \'Palasuni\', \'Sishu Bhawan\', \'Tata Power -- DN Group
Corporate\', \'Vani Vihar\', \'Tata Power -- MG Bhubaneswar\', \'Tata
Power -- Regalia Mall (DN Square)\', \'Kazam -- Rasulgarh\', \'Tata
Power -- CSM Technologies\', \'Statiq -- Yellowings ITC Cuttack
Station\', \'Tata Power -- DN Wisdom Tree\', \'Tata Power -- GUGNANI
TYRES\', \'Jagamara\', \'Tata Power -- Audi Bhubaneswar\', \'Jaydev
Vihar\', \'Tankapani Road\', \'Tata Power -- MLCP Saheed Nagar\',
\'Pokhariput\', \'KIIT\', \'Nayapalli\', \'GLIDA DLF Bhubaneswar --
Statiq\', \'Statiq -- Nexus Esplanade Mall\', \'Kalinga Stadium\',
\'Mancheswar\', \'Chandrasekharpur\', \'Satya Nagar\', \'TML Tirupati
Enterprises\', \'Badagada\', \'Tata Power -- GUGNANI AUTOCARS\'\]

**Combination 2 (Fitness 0.6486)**

\[\'Tata Power -- BMC Bhawani Mall\', \'Vani Vihar\', \'Saheed Nagar\',
\'Nayapalli\', \'Statiq -- Yellowings ITC Cuttack Station\', \'Tata
Power -- DN Group Corporate\', \'Kazam -- Rasulgarh\', \'Charger --
Geetanjali\', \'KIIT\', \'Jagamara\', \'Tata Power -- Regalia Mall (DN
Square)\', \'Tata Power -- MLCP Saheed Nagar\', \'Kalinga Stadium\',
\'GLIDA DLF Bhubaneswar -- Statiq\', \'Jaydev Vihar\', \'Tata Power --
MG Bhubaneswar\', \'Tata Power -- CSM Technologies\', \'TML Tirupati
Enterprises\', \'Tankapani Road\', \'Tata Power -- GUGNANI TYRES\',
\'Sishu Bhawan\', \'HPCL -- Regional Office\', \'Tata Power -- Audi
Bhubaneswar\', \'Pokhariput\', \'Tata Power -- Dion Automotives\',
\'Palasuni\', \'Tata Power -- DN Wisdom Tree\', \'Statiq -- Nexus
Esplanade Mall\', \'Badagada\', \'Mancheswar\', \'Satya Nagar\', \'Tata
Power -- GUGNANI AUTOCARS\', \'Chandrasekharpur\'\]

**Combination 3 (Fitness 0.6480)**

\[\'Saheed Nagar\', \'Nayapalli\', \'Statiq -- Nexus Esplanade Mall\',
\'Tata Power -- BMC Bhawani Mall\', \'Tata Power -- Audi Bhubaneswar\',
\'Jagamara\', \'Vani Vihar\', \'Statiq -- Yellowings ITC Cuttack
Station\', \'Tata Power -- Regalia Mall (DN Square)\', \'Charger --
Geetanjali\', \'Tankapani Road\', \'Tata Power -- Dion Automotives\',
\'Sishu Bhawan\', \'Chandrasekharpur\', \'Badagada\', \'Kazam --
Rasulgarh\', \'HPCL -- Regional Office\', \'Tata Power -- CSM
Technologies\', \'Pokhariput\', \'Tata Power -- MLCP Saheed Nagar\',
\'Kalinga Stadium\', \'Tata Power -- GUGNANI TYRES\', \'GLIDA DLF
Bhubaneswar -- Statiq\', \'Tata Power -- DN Group Corporate\', \'Tata
Power -- MG Bhubaneswar\', \'Mancheswar\', \'Jaydev Vihar\', \'KIIT\',
\'Tata Power -- DN Wisdom Tree\', \'Tata Power -- GUGNANI AUTOCARS\',
\'Palasuni\', \'Satya Nagar\', \'TML Tirupati Enterprises\'\]

**Combination 4 (Fitness 0.6479)**

\[\'Saheed Nagar\', \'Tata Power -- Regalia Mall (DN Square)\', \'Sishu
Bhawan\', \'Tata Power -- BMC Bhawani Mall\', \'GLIDA DLF Bhubaneswar --
Statiq\', \'Vani Vihar\', \'Nayapalli\', \'HPCL -- Regional Office\',
\'Tata Power -- DN Group Corporate\', \'Tata Power -- MLCP Saheed
Nagar\', \'Mancheswar\', \'Jagamara\', \'Kazam -- Rasulgarh\', \'Tata
Power -- CSM Technologies\', \'Tata Power -- Dion Automotives\',
\'Pokhariput\', \'Charger -- Geetanjali\', \'Tankapani Road\', \'Satya
Nagar\', \'KIIT\', \'Tata Power -- GUGNANI AUTOCARS\', \'Tata Power --
Audi Bhubaneswar\', \'Palasuni\', \'Tata Power -- GUGNANI TYRES\',
\'Jaydev Vihar\', \'Tata Power -- MG Bhubaneswar\',
\'Chandrasekharpur\', \'Badagada\', \'Tata Power -- DN Wisdom Tree\',
\'TML Tirupati Enterprises\', \'Statiq -- Nexus Esplanade Mall\',
\'Kalinga Stadium\', \'Statiq -- Yellowings ITC Cuttack Station\'\]

**Combination 5 (Fitness 0.6462)**

\[\'Saheed Nagar\', \'Vani Vihar\', \'GLIDA DLF Bhubaneswar -- Statiq\',
\'Charger -- Geetanjali\', \'Tata Power -- MG Bhubaneswar\', \'Tankapani
Road\', \'Jaydev Vihar\', \'Nayapalli\', \'Kalinga Stadium\',
\'Jagamara\', \'Tata Power -- Dion Automotives\', \'Satya Nagar\',
\'Tata Power -- GUGNANI AUTOCARS\', \'Tata Power -- Regalia Mall (DN
Square)\', \'Tata Power -- Audi Bhubaneswar\', \'Tata Power -- BMC
Bhawani Mall\', \'Tata Power -- CSM Technologies\', \'Palasuni\',
\'Badagada\', \'Tata Power -- MLCP Saheed Nagar\', \'TML Tirupati
Enterprises\', \'Sishu Bhawan\', \'Statiq -- Nexus Esplanade Mall\',
\'Tata Power -- GUGNANI TYRES\', \'KIIT\', \'Chandrasekharpur\',
\'Mancheswar\', \'Statiq -- Yellowings ITC Cuttack Station\', \'Tata
Power -- DN Wisdom Tree\', \'Tata Power -- DN Group Corporate\',
\'Pokhariput\', \'HPCL -- Regional Office\', \'Kazam -- Rasulgarh\'\]

## Accessibility Filtering with Shortest Distance Method (SDM)

Shortest Distance Method (SDM) plays a pivotal role in refining electric
vehicle (EV) charging infrastructure planning by addressing the critical
aspect of user accessibility. While clustering algorithms like Gaussian
Mixture Model (GMM) identify high-demand regions, and optimization
techniques such as Particle Swarm Optimization (PSO) determine optimal
charging station placements based on multiple constraints, SDM acts as a
spatial validation mechanism \[16\] . It ensures that the selected
charging station locations are not only theoretically optimal but also
practically reachable and spatially efficient from the perspective of
everyday EV users .The core objective of SDM is to evaluate how
conveniently users can access proposed stations, minimizing both travel
distance and travel time. This is achieved by implementing a
mixed-integer optimization framework, which explicitly considers the
geometric and topological properties of the urban layout. Instead of
relying on straight-line (Euclidean) distance, SDM incorporates
real-world transportation data, such as road network geometry, traffic
flow, and route constraints, to calculate the shortest path distance
between each demand node (which could represent a user, a neighborhood,
or a hotspot) and potential charging station sites \[17\].

This process helps to minimize overall user access costs, which includes
not only physical distance but also time, energy expenditure, and route
complexity. Additionally, the SDM framework incorporates constraints
that prevent the spatial clustering of charging stations in already
saturated regions, thereby encouraging a more balanced and equitable
distribution of infrastructure across both urban cores and peripheral or
underserved areas \[18\]. Another significant feature of SDM is its
ability to support multi-scale demand modeling. Demand is assessed both
at a macro level (e.g., traffic zones, commercial districts) and at a
micro level (e.g., individual travel patterns and trip logs), enabling a
more granular understanding of where and when charging is needed \[19\].
This dual-resolution approach provides a highly accurate proxy for
estimating anticipated charging requirements, facilitating service
coverage evaluations that reflect real-world behaviour.

+---------------------------+------------------------------------------+
| SDM ALGORITHM PSEUDOCODE: |                                          |
+===========================+==========================================+
| INPUT sets, coords        | for i \< j in sites:                     |
|                           |                                          |
| dist(a, b):               | sum += dist(sites\[i\], sites\[j\])      |
|                           |                                          |
| return distance(a, b)     | return sum                               |
|                           |                                          |
| total(sites):             | best_dist = ∞                            |
|                           |                                          |
| sum = 0                   | best_set = NULL                          |
|                           |                                          |
|                           | for s in sets:                           |
|                           |                                          |
|                           | d = total(s)                             |
|                           |                                          |
|                           | if d \< best_dist:                       |
|                           |                                          |
|                           | best_dist = d                            |
|                           |                                          |
|                           | best_set = s                             |
+---------------------------+------------------------------------------+

To further improve spatial equity, SDM includes a threshold-based
accessibility analysis, which flags underserved or inaccessible zones.
If the shortest distance from a given demand point to the nearest
station exceeds a pre-defined limit---often derived from policy
guidelines or user comfort tolerances---those areas are classified as
coverage gaps \[20\]. These gaps are then fed back into the optimization
loop, serving as corrective feedback to PSO. As a result, subsequent
iterations of site selection take these deficiencies into account,
continuously improving the network's reach and inclusivity \[21\]. By
integrating SDM into the broader EV infrastructure planning pipeline,
the system transitions from being merely optimized on paper to being
actionable and user-centric in practice. The synergy of PSO\'s global
optimization capabilities, GMM\'s demand clustering accuracy, and SDM\'s
accessibility analysis leads to a charging network design that is
technically robust, socially equitable, and operationally viable \[22\]
. This ensures that infrastructure serves all urban regions
fairly---supporting high-demand, high-density areas as well as more
sparsely populated suburban or rural zones---thereby promoting broader
EV adoption and enhancing the user experience.

**Output -**

Combination 1 (Fitness 0.6598) distance: 2324.07 km

Combination 2 (Fitness 0.6565) distance: 2324.07 km

Combination 3 (Fitness 0.6532) distance: 2324.07 km

Combination 4 (Fitness 0.6499) distance: 2324.07 km

Combination 5 (Fitness 0.6466) distance: 2324.07 km

## Geospatial Mapping with QGIS

QGIS (Quantum Geographic Information System) was used as the primary
platform for generating, analyzing, and visualizing spatial data
throughout this study. As a powerful open-source GIS tool, QGIS offers a
wide range of geoprocessing functions and customization options, making
it ideal for both academic and practical applications in urban planning.
In this research, it enabled the digitization and layering of key
spatial datasets such as road networks, land use zones, population
distribution, electric grid coverage, and Points of Interest (POIs). Its
support for diverse formats like shapefiles (.shp), GeoJSON, raster
layers, and CSV files---ensured smooth integration of both vector and
tabular data.

Advanced features like attribute queries, spatial joins, and heat
mapping were instrumental in identifying demand clusters and optimal
locations for EV charging stations. Plugins such as "MMQGIS" and
"Heatmap" enriched the analysis by supporting spatial clustering and
density visualization. QGIS also excels in cartographic design, which
helped create clear, publication-quality maps highlighting demand zones,
infrastructure gaps, and proposed station sites \[23\].

Custom symbology, labeling, and dynamic layer control improved the
clarity and impact of these visuals, making them accessible to both
technical and non-technical audiences. Tools for adding layout elements
like legends, scale bars, and north arrows contributed to the
professional presentation of the final maps.

To enhance visual clarity and add real-world context, Mapbox was
integrated into QGIS using the XYZ Tile feature.

This brought in high-resolution, modern basemaps that accurately
reflected Bhubaneswar's streets, blocks, and landmarks. By using Mapbox
as a backdrop, overlays such as EV station markers and road networks
aligned precisely with real-world geography, making the maps more
intuitive and informative. This integration supported a visually rich
and data-driven approach to planning EV infrastructure in Bhubaneswar.

1.  ![](./image1.jpg){width="3.352777777777778in"
    height="2.029166666666667in"}[Bhubaneswar EV Charging Station
    Planning Map]{.smallcaps}

#  Conclusion

![](./image2.jpeg){width="2.097916666666667in"
height="5.023611111111111in"}This study establishes a structured and
technically grounded approach to EV charging infrastructure planning in
Bhubaneswar. By integrating spatial mapping with QGIS, demand clustering
via GMM, and site optimization through PSO and SDM, the framework
addresses not only location selection but also practical concerns such
as grid accessibility, route coverage, and urban demand intensity.

Our findings highlight that thoughtful siting of EV stations, especially
in growth-prone and underrepresented areas, can drastically improve user
convenience, reduce queuing delays, and contribute to environmental
sustainability. Moreover, the methodology is scalable and adaptable to
other urban centers across India.

As Odisha looks to accelerate its electric mobility mission, this model
serves as a replicable, data-driven roadmap for smart city planners,
urban transport engineers, and policy-makers aiming to future-proof
their city's transportation infrastructure.

# **[Best combination by total pairwise distance:]{.underline}** {#best-combination-by-total-pairwise-distance .unnumbered}

• Tata Power -- BMC Bhawani Mall

• Vani Vihar

• Saheed Nagar

• Nayapalli

• Statiq -- Yellowings ITC Cuttack Station

• Tata Power -- DN Group Corporate

• Kazam -- Rasulgarh

• Charger -- Geetanjali

• KIIT

• Jagamara

• Tata Power -- Regalia Mall (DN Square)

• Tata Power -- MLCP Saheed Nagar

• Kalinga Stadium

• GLIDA DLF Bhubaneswar -- Statiq

• Jaydev Vihar

• Tata Power -- MG Bhubaneswar

• Tata Power -- CSM Technologies

• TML Tirupati Enterprises

• Tankapani Road

• Tata Power -- GUGNANI TYRES

• Sishu Bhawan

• HPCL -- Regional Office

• Tata Power -- Audi Bhubaneswar

• Pokhariput

• Tata Power -- Dion Automotives

• Palasuni

• Tata Power -- DN Wisdom Tree

• Statiq -- Nexus Esplanade Mall

• Badagada

• Mancheswar

• Satya Nagar

• Tata Power -- GUGNANI AUTOCARS

• Chandrasekharpur

**Total pairwise distance: 2324.07 km**

[Acknowledgment]{.smallcaps}

We express our profound gratitude to Dr. Debani Prasad Mishra for his
valuable guidance for the successful completion of the research work.

##### References {#references .unnumbered}

1.  N. Shahraki et al., \"Optimal locations of electric public charging
    stations using real world vehicle travel patterns,\" *Transportation
    Research Part D: Transport and Environment*, vol. 41, pp.
    165--176, 2015.
    doi: [10.1016/j.trd.2015.09.011](https://doi.org/10.1016/j.trd.2015.09.011).

2.  Z.-K. Huang and K.-W. Chau, \"A new image thresholding method based
    on Gaussian mixture model,\" *Applied Mathematics and Computation*,
    vol. 205, no. 2, pp. 899--907, 2008.

3.  S.C. Kim and T.J. Kang, "Texture classification and segmentation
    using wavelet packet frame and Gaussian mixture model," Pattern
    Recognition, vol. 40, no. 4, pp. 1207-1221, 2007.

4.  I. Frade, A. Ribeiro, G. Gonçalves, and A. Antunes, "Optimal
    location of charging stations for electric vehicles in a
    neighborhood in Lisbon, Portugal," Transportation Research Record:
    Journal of the Transportation Research Board, vol. 2252, pp. 91-98,
    2011.

5.  Y. Zhang, Q. Zhang, A. Farnoosh, S. Chen, and Y. Li, \"GIS-based
    multi-objective particle swarm optimization of charging stations for
    electric vehicles,\" *Energy*, vol. 169, pp. 844--883, 2019.

6.  R. Adam, K. Qian, and R. Brehm, \"Electric vehicle user behavior
    prediction using Gaussian mixture models and soft information,\"
    in *2021 10th IEEE PES Innovative Smart Grid Technologies Asia (ISGT
    Asia)*, 2021, doi: 10.1109/ISGTAsia49270.2021.9715580.

7.  A. Y. Ng, M. I. Jordan, and Y. Weiss, \"On spectral clustering:
    Analysis and an algorithm,\" *Advances in Neural Information
    Processing Systems*, vol. 14, pp. 849--856, 2002.

8.  Z. Miljanic, V. Radulovic, and B. Lutovac, "Efficient Placement of
    Electric Vehicles Charging Stations using Integer Linear
    Programming," IEEE Transactions on Smart Grid, 2020.

9.  M. S. Mastoi, S. Zhuang, J. S. Ro, H. M. Munir, M. Haris, M.
    Hassan, M. Usman, and S. S. H. Bukhari, "An in-depth analysis of
    electric vehicle charging station infrastructure, policy
    implications, and future trends," *Energy Reports*, vol. 8, pp.
    11504--11529, 2022.

10. G. Pistoia, *Electric and Hybrid Vehicles: Power Sources, Models,
    Sustainability, Infrastructure and the Market*. Elsevier, 2010, pp.
    517--542.

11. M. E. Kabir, C. Assi, H. Alameddine, J. Antoun, and J. Yan, \"Demand
    aware deployment and expansion method for an electric vehicles fast
    charging network,\" *IEEE Transactions on Smart Grid*, vol. 10, no.
    1, pp. 172--183, 2019.

12. S. Wang et al., \"Stochastic collaborative planning method for
    electric vehicle charging stations,\" *IEEE Transactions on Smart
    Grid*, vol. 7, no. 3, pp. 1327--1334, May 2016.

13. Q. Sun, X. Bai, F. Liu, L. Liu, X. Ji, and J. Hardy,
    \"Multi-objective planning for electric vehicle charging stations
    considering TOU price,\" *IEEE Transactions on Smart Grid*, vol. 9,
    no. 3, pp. 1861--1870, May 2018.

14. P. Jog, S. Shete, R. Kumawat, and D. Palwalia, \"Electric vehicle
    charging station infrastructure: A review,\" *IEEE Transactions on
    Industry Applications*, vol. 57, no. 2, pp. 234--241, Mar.-Apr.
    2021.

15. Y. Xu et al., \"Robust scheduling of EV charging load using
    stochastic optimization model,\" *Energy*, vol. 153, pp.
    1046--1058, 2018.
    doi: [10.1016/j.energy.2018.04.106](https://doi.org/10.1016/j.energy.2018.04.106).

16. W. Khan, F. Ahmad, and M. S. Alam, \"Fast EV charging station
    integration with grid ensuring optimal quality power
    exchange,\" *Engineering Science and Technology, an International
    Journal*, vol. 22, pp. 143--152, 2019.
    doi: [10.1016/j.jestch.2018.08.005](https://doi.org/10.1016/j.jestch.2018.08.005).

17. X. Xi et al., \"Simulation--optimization model for location of a
    public electric vehicle charging infrastructure,\" *Transportation
    Research Part D: Transport and Environment*, vol. 22, pp.
    60--69, 2013.
    doi: [10.1016/j.trd.2013.03.005](https://doi.org/10.1016/j.trd.2013.03.005).

18. A. K. Kalakanti and S. Rao, \"Charging station planning for electric
    vehicles,\" *Systems*, vol. 10, no. 1, p. 6, 2022.
    doi: [10.3390/systems10010006](https://doi.org/10.3390/systems10010006).

19. A. K. M. Yousuf et al., \"Electric vehicle charging station
    infrastructure: A comprehensive review of technologies, challenges,
    and mitigation strategies,\" *Energy Reports*, vol. 7, pp.
    2682--2696, 2021.
    doi: [10.1016/j.egyr.2021.05.045](https://doi.org/10.1016/j.egyr.2021.05.045).

20. P. Sadeghi-Barzani et al., \"Optimal fast charging station placing
    and sizing,\" *Applied Energy*, vol. 125, pp. 289--299, 2014.
    doi: [10.1016/j.apenergy.2014.03.077](https://doi.org/10.1016/j.apenergy.2014.03.077).

21. F. Xie et al., \"Long-term strategic planning of inter-city fast
    charging infrastructure for battery electric
    vehicles,\" *Transportation Research Part E: Logistics and
    Transportation Review*, vol. 109, pp. 261--276, 2018.
    doi: [10.1016/j.tre.2017.11.014](https://doi.org/10.1016/j.tre.2017.11.014).

22. E. Sortomme et al., \"Coordinated charging of plug-in hybrid
    electric vehicles to minimize distribution system losses,\" *IEEE
    Transactions on Smart Grid*, vol. 2, no. 1, pp. 198--205, 2011.
    doi: [10.1109/TSG.2010.2090913](https://doi.org/10.1109/TSG.2010.2090913).

23. S. S. Ali et al., \"An overview of electric vehicle charging data
    acquisition and grid connection standards for power system studies
    and EV-grid integration,\" *Energies*, vol. 13, no. 23, p.
    6141, 2020.
    doi: [10.3390/en13236141](https://doi.org/10.3390/en13236141).

24. L. Wang et al., \"Optimal planning of charging stations for electric
    vehicles based on fuzzy Delphi and hybrid multi-criteria decision
    making approaches,\" *Transportation Research Part C: Emerging
    Technologies*, vol. 97, pp. 102--117, 2018.
    doi: [10.1016/j.trc.2018.10.019](https://doi.org/10.1016/j.trc.2018.10.019)
