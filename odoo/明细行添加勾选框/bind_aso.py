# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class LumiBindAsoWizaed(models.TransientModel):
    """绑定弹窗"""
    _name = 'bind.aso.wizard'

    ...

    def batch_update_selected(self):
        """批量修改明细行字段"""
        uncertain_order_id = self.uncertain_order_id
        uol_product_id_map = {}
        uol_line_ids = self.line_ids.filtered(lambda l: l.selected is False).mapped('uol_line_id.id')
        for line_id in uncertain_order_id.line_ids.filtered(
                lambda rec: rec.new_deal_qty == 0 and not rec.is_return_and_pay):
            if line_id.id in uol_line_ids:
                continue
            if line_id.product_id.default_code in uol_product_id_map:
                uol_product_id_map[line_id.product_id.default_code].append(line_id.id)
            else:
                uol_product_id_map[line_id.product_id.default_code] = [line_id.id]

        selected_lines = self.line_ids.filtered(lambda l: l.selected)
        if selected_lines:
            # 执行批量修改操作
            selected_default_code = selected_lines[0].product_id.default_code
            for line in selected_lines:
                product_default_code = selected_lines[0].uol_line_id.product_id.default_code
                if line.product_id.default_code == selected_default_code:
                    line.uol_line_id = uol_product_id_map[product_default_code][-1] if uol_product_id_map.get(
                                        product_default_code) else False
                    if uol_product_id_map.get(product_default_code):
                        uol_product_id_map[product_default_code].pop()

            # 取消选中状态
            selected_lines.write({'selected': False})
        return self.return_self_view()

    def batch_unlink_selected(self):
        """批量删除明细行选中字段"""
        selected_lines = self.line_ids.filtered(lambda l: l.selected)
        if selected_lines:
            selected_lines.unlink()
        return self.return_self_view()

    def action_select_lines(self):
        """全选"""
        for line in self.line_ids:
            line.selected = True
        return self.return_self_view()

    def action_deselect_lines(self):
        """取消选中"""
        for line in self.line_ids:
            line.selected = False
        return self.return_self_view()

    def return_self_view(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'bind.aso.wizard',
            'name': _('绑定'),
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': self.env.ref('after_sale_detect.bind_aso_form').id,
            'views': [(self.env.ref('after_sale_detect.bind_aso_form').id, 'form')],
            'target': 'new',
            'res_id': self.id,
        }


class LumiBindAsolineWizard(models.TransientModel):
    """绑定弹窗明细"""
    _name = 'bind.aso.line.wizard'

    # 是否选中
    selected = fields.Boolean(string='是否选中')
    ...



