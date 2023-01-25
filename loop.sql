select * from authors;
create table authorscopy as select * from authors; 
delete from authorscopy;
select * from authorscopy;

DO $$
 DECLARE
     authors_num  authorscopy.authors_id %TYPE;
     w authorscopy.writer%TYPE;
	 p authorscopy.penciler%TYPE;
	 c authorscopy.cover_artist%TYPE;
	 i authorscopy.imprint%TYPE;

 BEGIN
     authors_num := 10;
     w := 'Richard';
	 p := 'Michael';
	 c := 'Bob';
	 i := 'Marvel Universe #';
     FOR counter IN 1..20
         LOOP
            INSERT INTO authorscopy (authors_id, writer, penciler, cover_artist, imprint)
             VALUES (counter + authors_num, w||' '||counter||'-th',p||' '||counter+4||'-th',c||' '||counter+2||'-th', i||counter);
         END LOOP;
 END;
 $$
