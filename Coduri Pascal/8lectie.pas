var n1, n2: real;
var _result, pas: real;

begin
    writeln('Introduce primul numar: ');
    read(n1);
    writeln('Introduce al doilea numar: ');
    read(n2);
    writeln('Introduce pasul: ');
    read(pas);

    repeat 
        _result:= 2*n1-4;
        writeln('x = ', n1, ' y = ', _result);
        n1:= n1 + pas;
    until n1 >= n2 + 1
end.