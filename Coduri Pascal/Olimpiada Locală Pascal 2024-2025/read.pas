var
  f: TextFile;
  line: string;
begin
  AssignFile(f, 'file.txt');
  Reset(f);
  
  while not Eof(f) do
  begin
    ReadLn(f, line);
    WriteLn(line);
  end;
  
  CloseFile(f);
end.