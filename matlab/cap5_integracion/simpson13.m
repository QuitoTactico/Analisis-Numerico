%simpson13: Calcula la integral definida en el intervalo [a,b] para la
%función f, por el método del simpson 1/3 compuesto, con n puntos, con n par.
function [val] = simpson13(a,b,n)
    syms x
    f=1.5*x^2+4*x+3500; %escriba la función a integrar
    h=abs(b-a)/n;
    f0=eval(subs(f,a));
    fn=eval(subs(f,b));
    sum=f0+fn;
    for i=1:n-1
        fi=eval(subs(f,a+i*h));
        if mod(i,2)==0
            sum=sum+2*fi;
        else
            sum=sum+4*fi;
        end
    end
    val=sum*h/3;
end