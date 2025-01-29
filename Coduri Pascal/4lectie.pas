var n, nota, suma, i: integer;
var media: real;

begin
    suma:= 0;
    writeln('Introduceti numarul de note: ');
    readln(n);
    writeln('Introduceti notele: ');
    for i:= 1 to n do 
    begin
        readln(nota);
        suma:= suma + nota;
    end;
    writeln('Suma este ', suma);
    media:= suma / n;
    writeln('Media este ', media);
end.