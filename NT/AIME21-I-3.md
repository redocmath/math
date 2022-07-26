# AIME 2021 I Problem 3
`Number Theory`, `easy`

Problem
---
Find the number of positive integers less than $1000$ that can be 
expressed as the difference of two integral powers of $2.$  

Idea
---
두 정수 $x, y$에 대해 $x>y$라 가정하면 $n=2^x-2^y < 1000$으로 둘 수 있다.  
이때 $n=2^y(2^{x-y}-1)$으로 나타낼 수 있는데 $2^y$는 짝수, $2^{x-y}$는 홀수이므로 중복이 나타날 수 없다.

Solution
---
$0 \leq y < x \leq 10$임을 이용해 경우의 수를 계산한다.
| y | range of x |
|:-:|:----------:|
| 0 | 1~9 |
| 1 | 2~9 |
| 2 | 3~9 |
| 3 | 4~9 |
| 4 | 5~9 |
| 5 | 6~10 |
| 6 | 7~10 |
| 7 | 8~10 |
| 8 | 9~10 |
| 9 | 10 |

$\therefore Ans=9+8+7+6+5+5+4+3+2+1=50$