%RuKu4: obtiene la solucición del sistema de m EDO y'=f(t,y) para t en
%el intervalo [a,b] y una división de puntos N, y condiciones iniciales 
%y(0)=y0. Mediante el runge kutta de cuarto orden 

function [yout,time] = RuKu4(a,b,N,m,y0)
    
    K=zeros(m,4);
    h=(b-a)/N;
    time=a:h:b;
    yout=zeros(m,length(time));
%    syms t y1 y2 %cambiar depende del número de ecuaciones (ym)
    syms t y
%     var=[t,y1,y2];
    var=[t,y];
%     f1=-0.5*y1;
%     f2=4-0.3*y2-0.1*y1;
%     f=[f1,f2];
%     f=1+y/t+(y/t)^2;
%      f=(sec(t)+cos(t*y))/2;
      f=8*cos(t*y)+t;
      %f=(y^2)/(t+1);
    for k=1:length(time)
        yout(:,k)=y0;
        for j=1:4
            for i=1:m
                if j==1
                    K(i,j) = eval(subs(f(i),var,[time(k),y0]));
                elseif j==2 || j==3
                    K(i,j) = eval(subs(f(i),var,[time(k)+0.5*h,y0+0.5*h*(K(:,j-1)')]));
                else
                    K(i,j) = eval(subs(f(i),var,[time(k)+h,y0+h*(K(:,j-1)')]));
                end
            end
        end
        y0=y0+(1/6)*(K(:,1)'+2*K(:,2)'+2*K(:,3)'+K(:,4)')*h;
    end
    
end
