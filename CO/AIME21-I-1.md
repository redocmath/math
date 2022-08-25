# AIME 2021 I Problem 1
`Combinatorics` `Easy`

Problem
---
Zou and Chou are practicing their 100-meter sprints by running $6$ races against each other. Zou wins the first race, and after that, the probability that one of them wins a race is $\frac23$ if they won the previous race but only $\frac13$ if they lost the previous race. The probability that Zou will win exactly $5$ of the $6$ races is $\frac mn$, where $m$ and $n$ are relatively prime positive integers. Find $m+n$.

Idea
---
Zou가 2~5번째 경기에서 지는 경우의 확률은 같고 6번째 경기만 예외적으로 확률이 다름을 확인한다

Solution
---
Zou가 2~5번째 경기 중 하나에서 질 확률 = $(\frac13)^2 \times (\frac23)^3 \times 4 = \frac{32}{3^5}$

Zou가 6번째 경기에서 질 확률 = $\frac13 \times (\frac23)^4 = \frac{16}{3^5}$

$\therefore P=\frac{48}{3^5}=\frac{16}{81}$

$\therefore Ans=16+81=97$