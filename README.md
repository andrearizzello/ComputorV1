# ComputorV1

The purpose of this project is to have you code a program that solves simple equations.
The program takes a polynomial equation. 
That is, involving only the powers, no complicated functions.
The program must display its solution(s)

# Rules

- You are not allowed any mathematic function/library (beside additions and multiplications of real numbers) that you did not implement yourself
- The program should dipslay at least:
    - The reduced form of the equation.
    - The degree of the equation.
    - Its solution(s), as well as the sign of the discriminant when it makes sense...

# Tests

```shell
./computorV1.py <expression>

Examples:
5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
5 * X^0 + 4 * X^1 = 4 * X^0
1 * X^0 + 4 * X^1 = 0
8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0
5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
5 + 4 * X + X^2= X^2
```

## Project validated with `115/125`
