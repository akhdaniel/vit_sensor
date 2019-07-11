from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class reading(models.Model):
    _name = 'vit.reading'
    _rec_name = 'sensor_id'
    _description = 'Sensor reading'

    sensor_id = fields.Many2one(comodel_name="vit.sensor", string="Sensor ID", required=True, )
    temperature = fields.Float(string="Temperature", required=False, )
    humidity = fields.Float(string="Humidity", required=False, )
    vibration = fields.Float(string="Vibration", required=False, )
    read_date = fields.Datetime(string="Read Date", required=False, )