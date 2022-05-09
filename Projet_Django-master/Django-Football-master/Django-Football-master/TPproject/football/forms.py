from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class ClubForm(ModelForm):
    class Meta:
        model = models.Club
        fields = ('nom_club', 'pays_club', 'date_parution_club', 'nombre_LDC','resume')
        labels = {
            'nom_club' : _('Nom du club'),
            'pays_club' : _('Pays du club') ,
            'date_parution_club' : _('Date de parution du club'),
            'nombre_LDC' : _('Ligue des champions gagner'),
            'resume' : _('Résumé')
        }

class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueur
        fields = ('nom_joueur', 'pays_joueur', 'date_naissance_joueur', 'nombre_LDC','resume', 'club')
        labels = {
            'nom_joueur': _('Nom du joueur'),
            'pays_joueur': _('Origine du joueur'),
            'date_naissance_joueur': _('Date de naissance du joueur'),
            'nombre_LDC': _('Ligue des champions gagner'),
            'resume': _('Résumé'),
            'club' : _("Club de foot:")
        }