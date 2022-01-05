aliens = []

for alien_number in range(30):
    alien = {'color':'red','point':5,'speed':'slow'}
    aliens.append(alien)

for alien in aliens[:5]:
    print(alien)
    
print('......')
print(f'\nThe totle number alien is {len(aliens)}.')
