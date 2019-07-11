from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class temperature(models.Model):
    _name = 'vit.temperature'
    _rec_name = 'sensor_id'
    _description = 'Temperature Sensor reading'

    sensor_id = fields.Many2one(comodel_name="vit.sensor", string="Sensor ID", required=True, )
    value = fields.Float(string="Value",  required=False, )
    read_date = fields.Datetime(string="Read Date", required=True, )