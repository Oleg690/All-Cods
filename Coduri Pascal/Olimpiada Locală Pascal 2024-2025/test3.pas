program Test3;
uses
  Crt;
var
  f: Text;
  i: Word;
  numbers: Word;
begin
  ClrScr;
  Assign(f, 'test.txt');
  Rewrite(f);
  try
    numbers := 999;
    for i := 1 to numbers do
    begin
      Write(f, IntToStr(i));
          Write(f, ', ');
      if (i mod 3) = 0 then
        
        WriteLn(f);
    end;
  finally
    Close(f); 
  end;
end.
