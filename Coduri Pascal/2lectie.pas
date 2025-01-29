var x, y: real;

begin
    write('x = ');
        readln(x);
    
    if x > 5 then y:= 2*x + 3
            else y:= sqrt(x);

    write(y:4:2);

end.