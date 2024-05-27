%trapecio: Calcula la integral definida en el intervalo [a,b] para la
%función f, por el método del trapecio compuesto, con n puntos.
function [val] = trapecio(a,b,n)
    syms x
    f=exp(x)-2*x; %escriba la función a integrar
    h=abs(b-a)/n;
    f0=eval(subs(f,a));
    fn=eval(subs(f,b));
    sum=f0+fn;
    for i=1:n-1
        fi=eval(subs(f,a+i*h));
        sum=sum+2*fi;
    end
    val=sum*h/2;
end