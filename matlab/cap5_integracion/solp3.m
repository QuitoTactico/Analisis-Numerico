clear all
clc
x0=[1 1 1]';
x1=[2 2 2]';
T=[0 -0.5+6/100 -0.1; 0.3 0 -0.2; 0.2 0.1 0];
C=x1-T*x0;
Tol=0.5e-1;
niter=100;
format long
c=0;
    error=Tol+1;
    Xt(:,c+1)=x0;
    n(1)=c;
    E(c+1)=error;
while error>Tol && c<niter
            x1=T*x0+C;
            E(c+2)=norm((x1-x0),inf);
        error=E(c+2);
        x0=x1;
        c=c+1;
        n(c+1)=c;
        Xt(:,c+1)=x0;
end

disp('\n')
    disp(['      n                X1                   X2                   X3                   X4                   Error'])
    D=[n' Xt' E'];
    table(D)


    radio=max(abs(eig(T)))

    T2=[0 -0.5+6/100 -0.1; 0.3 0 -0.2; 0.2 0.1 10];
    radio2=max(abs(eig(T2)))


    x=[2 4 6 8];
    y=[0 6 12 15];

    [Tabla] = Newtonint(x,y)
[pol] = Newtonor(x,diag(Tabla,+1))

 xpol=x(1):0.001:x(end);
 p=pol(1)*xpol.^3+pol(2)*xpol.^2+pol(3)*xpol+pol(4);
 figure
 plot(x,y,'r*',xpol,p,'b')

 %aproximadamente en 5.3 años se hace rentable 