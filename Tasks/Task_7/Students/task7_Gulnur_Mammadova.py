n=int (input('a four-digit integer: '))
a=n//1000;
b=n//100%10;
c=n//10%10;
d=n%10;
S=a*b*c*d;
print (S);
