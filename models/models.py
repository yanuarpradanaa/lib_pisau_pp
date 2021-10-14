from odoo import models, fields, api

class lib_custom(models.Model):
    _inherit = 'op.media.unit'

#    active = fields.Boolean(string='Active ?', )
    unit_type = fields.Selection([('Pisau Plong','Pisau Plong'),
                                  ('Klise Emboss','Klise Emboss'),
                                  ('Klise Hotprint','Klise Hotprint'),
                                  ('Pisau + Klise','Pisau + Klise'),
                                  ])

class lib_custom2(models.Model):
    _inherit = 'op.media.movement'

    unit_type = fields.Selection(related='media_unit_id.unit_type', store= True)


class Authors(models.Model):
    _inherit = 'op.author'
    
    active = fields.Boolean(string='Active ?')

#class Lib_card(models.Model):
#    _inherit = 'op.library.card'

#    active = fields.Boolean(string="Active")
