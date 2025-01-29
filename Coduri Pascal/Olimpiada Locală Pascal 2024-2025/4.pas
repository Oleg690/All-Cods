var
  total, number, counter, loopTimes: integer;
begin 
  write('n=');
  readln(loopTimes);

  while loopTimes - 1 >= counter do
  begin
    write('nr=');
    readln(number);
    
    if number mod 2 = 1 then total:= total + number; counter := counter + 1;
  end;
  
  writeln(total);
end.
  