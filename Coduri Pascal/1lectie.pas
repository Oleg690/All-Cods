var num1, num2, s: integer;

begin
    write('Introduceti primul numar: ');
        readln(num1);
    write('Introduceti al doilea numar: ');
        readln(num2);
    
    

    if num1 < num2 then writeln('Rezultatul adunarii numerelor este: ',num1+num2);
            else s:= num1 - num2;
                        writeln('Diferenta numerelor: ', s);

end.