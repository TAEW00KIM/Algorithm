select
    count(F.ID) as FISH_COUNT,
    N.FISH_NAME as FISH_NAME
from FISH_INFO F
join FISH_NAME_INFO N on F.FISH_TYPE = N.FISH_TYPE
group by FISH_NAME
order by FISH_COUNT desc;