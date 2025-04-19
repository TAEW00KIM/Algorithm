select 
    BOOK_ID,
    date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from BOOK
where CATEGORY like '%인문%'
  and date_format(PUBLISHED_DATE, '%Y') = '2021'
order by PUBLISHED_DATE asc;