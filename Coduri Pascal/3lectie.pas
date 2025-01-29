var num1, num2, restult: real; 
var semn: char;

begin
    write('Primul Numar = ');
        readln(num1);
    write('Al doilea Numar = ');
        readln(num2);
    write('Semnul = ');
        readln(semn);

    case semn of
    '+': writeln(num1, ' + ', num2, ' = ', num1+num2);
    '-': writeln(num1, ' - ', num2, ' = ', num1-num2);
    '*': writeln(num1, ' * ', num2, ' = ', num1*num2);
    '/': writeln(num1, ' / ', num2, ' = ', num1/num2);
    else
        writeln('Ati introdus semnul gresit');
    end;
end.