var n1,n2,n3,i:integer;

begin
  write('Introduceti de cate ori veti vrea sa se repete actiunea: ');
  readln(n3);
  for i := 1 to n3 do
    begin
      write('Introduceti primul numar: ');
        readln(n1);
      write('Introduceti al doilea numar: ');
        readln(n2);
      writeln('Rezultatul scaderii numerelor este: ',n1-n2);
      
      writeln('Rezultatul adunarii numerelor este: ',n1+n2);
      
      writeln('Rezultatul impartirii numerelor este: ',n1/n2);

      writeln('Rezultatul inmultirii numerelor este: ',n1*n2);
      
      if n1*n2 > 1000 then writeln('Ai operat cu numere mari')
                      else
                        writeln('Ai operat cu numere mici')
    end;
end.