t=('cor', 'pal', 'san', 'gre', 'cru',
   'fla', 'vas', 'cha', 'atl','bot',
   'atp', 'bah', 'spo', 'flu', 'spo',
   'ref', 'vit', 'ctb', 'ava', 'pta', 'atg')
print(f'os 5 primeiros sao {t [0:5]}')
print(f'os ultimos quatros sao{t[-4:]}')
print(f'os times na ordem {sorted(t)}')
print(f'o cha esta na {t.index("cha")+1} posicao')
