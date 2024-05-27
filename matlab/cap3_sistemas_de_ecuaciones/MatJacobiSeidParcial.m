function [s, E] = MatJacobiSeid(x0, A, b, Tol, niter, met)
    c = 0;
    error = Tol + 1;
    D = diag(diag(A));
    L = -tril(A, -1);
    U = -triu(A, 1);
    E = []; % Inicializar el vector de errores

    fprintf('Condiciones iniciales: x0 = [%s]\n', sprintf('%.4f ', x0));
    fprintf('Iteración\tSoluciones\t\tError\n');
    while error >= Tol && c < niter
        if met == 0
            T = inv(D) * (L + U);
            C = inv(D) * b;
            x1 = T * x0 + C;
        elseif met == 1
            T = inv(D - L) * U;
            C = inv(D - L) * b;
            x1 = T * x0 + C;
        end

        error = norm(x1 - x0, inf) / norm(x1, inf); % Cálculo del error según la norma infinita
        E = [E; error]; % Guardar el error en el vector
        fprintf('%d\t\t[%s]\t%f\n', c, sprintf('%.4f ', x1), error);
        
        x0 = x1;
        c = c + 1;
    end

    if error < Tol
        s = x0;
        fprintf('La solución aproximada es [%s] con una tolerancia de %f\n', sprintf('%.4f ', s), Tol);
    else 
        fprintf('Fracasó en alcanzar la tolerancia de %f en %d iteraciones\n', Tol, niter);
    end
end
