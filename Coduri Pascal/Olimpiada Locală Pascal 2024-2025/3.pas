var
  f: TextFile;
  line: string;
  counter, num: integer;
begin
  AssignFile(f, 'file.txt');
  Reset(f);
  
  while not Eof(f) do
  begin
    ReadLn(f, line);
    num:= StrToInt(line);
  end;
  
  CloseFile(f);
  
  for var i:= 1 to 9 do if IntToStr(num)[i] = '3' then counter := counter + 1;
  
  writeln('Numărul 3 s-a găsit de ', counter, ' ori');
end.