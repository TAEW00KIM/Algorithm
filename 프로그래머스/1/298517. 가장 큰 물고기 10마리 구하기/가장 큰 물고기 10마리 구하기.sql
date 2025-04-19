select ID, LENGTH
from FISH_INFO
where LENGTH is not null
order by length desc, ID asc
limit 10;