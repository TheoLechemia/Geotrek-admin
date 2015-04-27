from geotrek.tourism import models as tourism_models
from geotrek.tourism.views import TouristicContentViewSet, TouristicEventViewSet
from geotrek.trekking.management.commands.sync_rando import Command as BaseCommand


class Command(BaseCommand):
    def sync(self):
        super(Command, self).sync()

        for lang in self.languages:
            self.sync_geojson(lang, TouristicContentViewSet, 'touristiccontents')
            self.sync_geojson(lang, TouristicEventViewSet, 'touristicevents')
            self.sync_pdfs(lang, tourism_models.TouristicContent)
            self.sync_pdfs(lang, tourism_models.TouristicEvent)

        if self.verbosity >= '1':
            self.stdout.write("Sync tourism pictograms")

        self.sync_static_file('tourism/touristicevent.svg')
        self.sync_pictograms(tourism_models.InformationDeskType)
        self.sync_pictograms(tourism_models.TouristicContentCategory)
        self.sync_pictograms(tourism_models.TouristicContentType)
        self.sync_pictograms(tourism_models.TouristicEventType)

        self.sync_attachments(tourism_models.TouristicContent)
        self.sync_attachments(tourism_models.TouristicEvent)