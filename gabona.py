gabona_nev = input('Gabona: ')
if gabona_nev == '':
	exit()


gabona_félék = ['búza', 'árpa', 'zab', 'kukorica', 'rozs']

if gabona_nev in gabona_félék:
	print('megfelelő gabona')
else:
	print('Ismereteln gabona')
