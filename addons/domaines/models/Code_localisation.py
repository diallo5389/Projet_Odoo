import webbrowser

def launch_google_maps(origin, destination):
    google_maps_url = f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&travelmode=driving&t=h"
    webbrowser.open(google_maps_url)

origin = "9.606829338375274,-13.653976070546209"
destination = "9.608764925938203,-13.64730695645336"

# Utilisation de la fonction pour lancer Google Maps avec les coordonnées de départ et d'arrivée en mode "Satellite"
launch_google_maps(origin, destination)

# from odoo import models, fields, api

# class VotreModele(models.Model):
#     _name = 'votre.modele'

#     # Définissez vos champs ici

#     @api.multi
#     def ouvrir_google_maps(self):
#         # URL avec les coordonnées spécifiques (latitude et longitude)
#         url = 'https://www.google.com/maps?q={latitude},{longitude}'.format(
#             latitude=self.latitude_field,
#             longitude=self.longitude_field
#         )

#         # Ouvrir l'URL dans un navigateur ou dans l'application si disponible
#         self.env['ir.actions.act_url'].sudo().browse(0).with_context(
#             {'url': url}).post()