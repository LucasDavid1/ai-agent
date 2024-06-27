from django.db import migrations
from django.utils import timezone

from chat.models import Artist, Band, Album


def create_initial_data(apps, schema_editor):
    freddie = Artist.objects.create(name='Freddie Mercury', instrument='Vocals', country='UK')
    brian = Artist.objects.create(name='Brian May', instrument='Guitar', country='UK')
    roger = Artist.objects.create(name='Roger Taylor', instrument='Drums', country='UK')
    john = Artist.objects.create(name='John Deacon', instrument='Bass Guitar', country='UK')

    queen = Band.objects.create(name='Queen', formation_year=1970, genre='Rock')
    queen.members.add(freddie, brian, roger, john)

    Album.objects.create(
        title='A Night at the Opera',
        release_date=timezone.datetime(1975, 11, 21).date(),
        genre='Rock',
        band=queen
    )
    Album.objects.create(
        title='News of the World',
        release_date=timezone.datetime(1977, 10, 28).date(),
        genre='Rock',
        band=queen
    )

    mick = Artist.objects.create(name='Mick Jagger', instrument='Vocals', country='UK')
    keith = Artist.objects.create(name='Keith Richards', instrument='Guitar', country='UK')
    charlie = Artist.objects.create(name='Charlie Watts', instrument='Drums', country='UK')
    ronnie = Artist.objects.create(name='Ronnie Wood', instrument='Guitar', country='UK')

    stones = Band.objects.create(name='The Rolling Stones', formation_year=1962, genre='Rock')
    stones.members.add(mick, keith, charlie, ronnie)

    Album.objects.create(
        title='Sticky Fingers',
        release_date=timezone.datetime(1971, 4, 23).date(),
        genre='Rock',
        band=stones
    )
    Album.objects.create(
        title='Exile on Main St.',
        release_date=timezone.datetime(1972, 5, 12).date(),
        genre='Rock',
        band=stones
    )


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]