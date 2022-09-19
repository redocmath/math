# KMO Round 1 (PKMO for Middle School) Problem 9
`Number Theory` `Easy`

Problem
---
양의 정수 $m, n$이 다음 조건을 만족할 때, $m + n$의 값을 구하여라.  
(조건) $m,n$의 최대공배수를 $G$, 최소공배수를 $L$이라 할 때, $LG = 270000$, $L - G = m + 2n$


Idea
---
조건의 두 번째 식을 주목하면 $G | L - G$, $G | m + 2n$ 임을 알 수 있다. $m = Ga$, $n = Gb$라 두고 식을 전개한다.


Solution
---
$LG = mn = 270000 = 3^3 2^4 5^4 = abG^2$  
$L - G = G(ab - 1) = G(a + 2b) = m + 2n$  
$ab - a - 2b - 1 = 0$  
$(a - 2)(b - 1) = 3 \dots (*)$ 

(*)에 의해 a, b의 가능성은 두 가지인데, $a,b$에 3의 배수가 없으면 $G^2$는 제곱수가 될 수 없으므로 $a = 3$, $b = 4$가 유일하다.

첫 식에 이를 대입해보면 $3^3 2^4 5^4 = 3 \times 4 \times G^2$이므로 즉 $G = 2 \times 3 \times 5^2 = 150$.

$\therefore m+n = 150 \times 7 = 1050$

$\therefore Ans = 1050$