#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime is O(1). because any value larger than 1 would run through the loop twice. making `a` = `n^4`. which will always be larget than the while loop `n^3`


b) Runtime is O(n^2), because there is a while loop nested inside of the for loop. so everytime n increases, so too does the number of times it must loop


c) Runtime is O(2^n), because this function is recursive and calls its self again and again until the number of `bunnies` is equal to `0`.

## Exercise II

1) Runtime ends up as O(2^n) because it recursively drops eggs to see which floor it will break on... so if starting at say the top floor of `n` stories, if `n=12` it would recursively call just like the bunnies exercise. until it reached the base case of 0. (its an egg drop, common sense says its going to break from 0 up.)

2) My in english solution solution: 
    a) `n` is total number of floors
    b) `f` is the minimum level that the egg will break
    c) if current floor is less than `f` the egg will not break
    d) if current floor is greater than `f` the egg will break

3) In code i imagine it looks like this:

```
def breaking_eggs(n, f):
    if f <= n:
        if f == 0:
            return f
        return 1 + breaking_eggs(n, f - 1)
```



