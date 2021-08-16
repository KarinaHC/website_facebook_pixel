# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    has_facebook_pixel = fields.Boolean(
        string='Facebook Pixel',
        compute=compute_has_facebook_pixel,
        inverse=inverse_has_facebook_pixel,)

    facebook_pixel_key = fields.Char(
        related='website_id.facebook_pixel_key',
        readonly=False,)

    @api.depends('website_id')
    def compute_has_facebook_pixel(self):
        self.has_facebook_pixel = bool(self.facebook_pixel_key)

    def inverse_has_facebook_pixel(self):
        if not self.has_facebook_pixel:
            self.facebook_pixel_key = False
