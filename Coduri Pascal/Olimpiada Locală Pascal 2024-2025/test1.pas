program test1;
uses Crt;
type Student=record
        nume, prenume:string[20];
        n1,n2,n3:0..10;
        end;
var f:file of student;
    v:student;
    i,n:byte;
BEGIN
  ClrScr;
  write('Numarul de studenti: ');
  readln(n);
  assign(f, 'test.txt');
  rewrite(f);
  for i:=1 to n do begin
    writeln('Studentul ', i);
    with v do begin
      write('Nume: '); readln(nume);
      write('Prenume: '); readln(prenume);
      write('Notele: '); readln(n1, n2, n3);
    end;
    write(f, v);
  end;
  close(f);
  readkey;
end.