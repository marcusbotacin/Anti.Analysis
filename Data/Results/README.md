# Results

I initially planned to make all results available. However, the databases became too big to be hosted here. This way, I opt to provide a minimal dataset as an example. If you are interested on the complete dataset, get in contact!

## Database schema

```
TABLE tricks (hash text, trick text, section text, addr text);
```

## Table Content

```
select count(distinct(hash)) from tricks;
394
```

## Query Example

```
sqlite> select distinct(hash) from tricks where trick like '%CPU%' and section like '%text%';
0410dead0e89a63589818cbde22197f8
0411aa52b25fd0264f2a985c14ba2575
041e5e2808641665e42d0ab29d8a9e04
041ec973067866871811287bd39f2d34
042306e4aef4260e284cad89fabd7705
```

