from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class sensor(models.Model):
    _name = 'vit.sensor'
    _rec_name = 'name'

    name = fields.Char("Name", required=True)
    description = fields.Char("Description", required=True)
    location = fields.Char("GPS Location", help="Lat,Lon")



