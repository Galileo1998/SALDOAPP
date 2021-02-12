from odoo import fields, models

class Movimiento(models.Model):
    _name = "sa.movimiento"
    _description = "Movimiento"
    _inherit = "mail.thread"

    name = fields.Char(string="Nombre", required=True)
    type_move = fields.Selection(selection=[("ingreso", "Ingreso"), ("gasto", "Gasto")], string="Tipo de movimiento", default="ingreso", required=True)
    date = fields.Datetime(string="Fecha")
    amount = fields.Float("Monto", track_visibility="onchange")
    receipt_image = fields.Binary("Foto del recibo")
    notas = fields.Html("Notas")

    currency_id = fields.Many2one("res.currency", default=44)

    user_id = fields.Many2one("res.users", string="Usuario")
    category_id = fields.Many2one("sa.category", "Categoria")
    tag_id = fields.Many2many("sa.tag", "sa_mov_sa_tag_rel", "move_id", "tag_id")

class Category(models.Model):
    _name = "sa.category"
    _description = "Categoria"

    name = fields.Char("Nombre")

    def ver_movimientos(self):
        return {
            "type": "ir.actions.act_window",
            "name":"Movimientos de categoria: "+self.name,
            "res_model": "sa.movimiento",
            "views": [[False, "tree"]],
            "target": "new",
            "domain": [["category_id", "=", self.id]]
        }

class Tag(models.Model):
    _name = "sa.tag"
    _description = "Tag"

    name = fields.Char("Nombre")

class ResUsers(models.Model):
    _inherit ="res.users"

    movimiento_ids = fields.One2many("sa.movimiento", "user_id")