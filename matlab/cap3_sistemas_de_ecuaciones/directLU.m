%directLU: Calcula la factorización LU de A, dependientdo el método
%elegido, Doolittle, crout o cholesky se elige 0,1 o 2 respectivamente en
%met.

function [L, U] = directLU(A,met)
    n=length(A);
    U=eye(n);
    L=U;
    for k=1:n
        sum1=0;
        for p=1:k-1
            sum1=sum1+L(k,p)*U(p,k);
        end
        if met==0
            U(k,k)=(A(k,k)-sum1)/L(k,k);
        elseif met==1
            L(k,k)=(A(k,k)-sum1)/U(k,k);
        else
            U(k,k)=sqrt(A(k,k)-sum1);
            L(k,k)=U(k,k);
        end
        for i=k+1:n
            sum2=0;
            for p=1:k-1
                sum2=sum2+L(i,p)*U(p,k);
            end
            L(i,k)=(A(i,k)-sum2)/U(k,k);
        end
        for j=k+1:n
            sum3=0;
            for p=1:k-1
                sum3=sum3+L(k,p)*U(p,j);
            end
            U(k,j)=(A(k,j)-sum3)/L(k,k);
        end
    end
end