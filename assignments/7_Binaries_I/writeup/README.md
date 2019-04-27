# Writeup 7 - Binaries I

Name: Chaewoon Hong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Chaewoon Hong

## Assignment Writeup

### Part 1 (90 Pts)



```c

int main()
{


    int a;
    int b;
    
    b = 0x1ceb00da;
    a = 0xfeedface;
    
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    
    a = a ^ b;
    b = b ^ a;
    a = a ^ b;
    
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    
    return 0;
}

```

### Part 2 (10 Pts)

The program performs XOR on int a and int b. Through the XOR calls, a and b swap values.
