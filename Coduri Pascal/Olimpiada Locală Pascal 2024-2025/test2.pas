program test2;
uses Crt;
type Student=record
        nume, prenume:string[20];
        n1,n2,n3:0..10;
        end;
var f:file of student;
    v:student;
    i:byte;
BEGIN
  ClrScr;
  assign(f, 'test.txt');
  reset(f);
  write('Restantieri: ');
  while not eof(f) do begin
    read(f, v);
    with v do
      if (n1 in [0..4]) or (n2 in [0..4]) or 
         (n3 in [0..4]) then writeln(nume, ' ', prenume);
  end;
  close(f);
  readkey;
end.