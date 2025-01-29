var 
  result: real;
  x1, y1, x2, y2: real;
begin
  write('Enter x1: '); readln(x1);
  write('Enter y1: '); readln(y1);
  write('Enter x2: '); readln(x2);
  write('Enter y2: '); readln(y2);
  
  writeln(sqrt(sqr(x2 - x1) + sqr(y2 - y1)));
end.