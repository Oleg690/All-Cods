var
  f: TextFile;
begin
  AssignFile(f, 'file.txt');
  Rewrite(f);
  
  WriteLn(f, '253635338');
  
  CloseFile(f);
  
  writeln('file rewriten!');
end.
