program Test4;
uses
  Crt;
var
  f: Text;
begin
  ClrScr;
  Assign(f, 'test.txt');
  Rewrite(f);
  try
    for var i := 1 to 10 do
      begin 
        Write(f, 'Randul ', i, ': ');
        for var j := 0 to 9 do
        begin
          Write(f, IntToStr(i - 1));
              Write(f, ', ');
        end;
        WriteLn(f);
      end;
  finally
    Close(f); 
  end;
end.
