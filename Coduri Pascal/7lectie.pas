var n1, n2: real;
var _result, pas: real;

begin
    writeln('Introduce primul numar: ');
    read(n1);
    writeln('Introduce al doilea numar: ');
    read(n2);
    writeln('Introduce pasul: ');
    read(pas);

    while n1 <= n2 do
        begin
            _result:= 1 / n1;
            writeln('x = ', n1, ' y = ', _result);
            n1:= n1 + pas;
        end;
end.