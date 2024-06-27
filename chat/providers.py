from django.db.models import Q

from chat.models import Artist, Band, Album


def create_artist(name, instrument, country):
    return Artist.objects.create(name=name, instrument=instrument, country=country)


def create_band(name, formation_year, genre, member_ids):
    band = Band.objects.create(name=name, formation_year=formation_year, genre=genre)
    members = Artist.objects.filter(id__in=member_ids)
    band.members.add(*members)
    return band


def create_album(title, release_date, genre, band_id):
    return Album.objects.create(title=title, release_date=release_date, genre=genre, band_id=band_id)


def search_music(query):
    return Album.objects.filter(
        Q(title__icontains=query) |
        Q(band__name__icontains=query) |
        Q(band__members__name__icontains=query)
    ).distinct()


def search_artists(query=None, instrument=None, country=None):
    filters = Q()
    if query:
        filters |= Q(name__icontains=query) | \
                   Q(instrument__icontains=query) | \
                   Q(country__icontains=query)
    if instrument:
        filters &= Q(instrument__icontains=instrument)
    if country:
        filters &= Q(country__icontains=country)
    return Artist.objects.filter(filters).distinct()


def search_bands(query=None, genre=None, formation_year=None):
    filters = Q()   
    if query:
        filters |= Q(name__icontains=query) | \
                   Q(members__name__icontains=query)
    if genre:
        filters &= Q(genre__icontains=genre)
    if formation_year:
        filters &= Q(formation_year=formation_year)
    return Band.objects.filter(filters).distinct()


def get_band_albums(band_id):
    return Album.objects.filter(band_id=band_id)


def get_albums_by_genre(genre):
    return Album.objects.filter(genre__icontains=genre)


def get_artist_bands(artist_id):
    return Band.objects.filter(members__id=artist_id)
