# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright or licensing details.
import itertools

from odoo import models, fields

BG_COLOR_PLUS = {0: 'bg-secondary', 1: 'bg-warning'}
BG_COLOR_MINUS = {0: 'bg-warning', 1: 'bg-secondary'}


def _get_color(i, j, color):
    if 0 <= i <= 2:
        if 0 <= j <= 2 or 4 < j <= 6 or 8 < j <= 10 or 12 < j <= 14 or 16 < j <= 18:
            return color[0]
        elif 2 <= j <= 4 or 6 < j <= 8 or 10 < j <= 12 or 14 < j <= 16 or 18 < j <= 20:
            return color[1]
    elif 2 <= i <= 4:
        if 0 <= j <= 2 or 4 < j <= 6 or 8 < j <= 10 or 12 < j <= 14 or 16 < j <= 18:
            return color[1]
        elif 2 <= j <= 4 or 6 < j <= 8 or 10 < j <= 12 or 14 < j <= 16 or 18 < j <= 20:
            return color[0]
    elif 4 <= i <= 6:
        if 0 <= j <= 2 or 4 < j <= 6 or 8 < j <= 10 or 12 < j <= 14 or 16 < j <= 18:
            return color[0]
        elif 2 <= j <= 4 or 6 < j <= 8 or 10 < j <= 12 or 14 < j <= 16 or 18 < j <= 20:
            return color[1]
    elif 6 <= i <= 8:
        if 0 <= j <= 2 or 4 < j <= 6 or 8 < j <= 10 or 12 < j <= 14 or 16 < j <= 18:
            return color[1]
        elif 2 <= j <= 4 or 6 < j <= 8 or 10 < j <= 12 or 14 < j <= 16 or 18 < j <= 20:
            return color[0]
    elif 8 <= i <= 10:
        if 0 <= j <= 2 or 4 < j <= 6 or 8 < j <= 10 or 12 < j <= 14 or 16 < j <= 18:
            return color[0]
        elif 2 <= j <= 4 or 6 < j <= 8 or 10 < j <= 12 or 14 < j <= 16 or 18 < j <= 20:
            return color[1]
    elif 10 <= i <= 12:
        if 0 <= j <= 2 or 4 < j <= 6 or 8 < j <= 10 or 12 < j <= 14 or 16 < j <= 18:
            return color[1]
        elif 2 <= j <= 4 or 6 < j <= 8 or 10 < j <= 12 or 14 < j <= 16 or 18 < j <= 20:
            return color[0]
    elif 12 <= i <= 14:
        if 0 <= j <= 2 or 4 < j <= 6 or 8 < j <= 10 or 12 < j <= 14 or 16 < j <= 18:
            return color[0]
        elif 2 <= j <= 4 or 6 < j <= 8 or 10 < j <= 12 or 14 < j <= 16 or 18 < j <= 20:
            return color[1]
    elif 14 <= i <= 16:
        if 0 <= j <= 2 or 4 < j <= 6 or 8 < j <= 10 or 12 < j <= 14 or 16 < j <= 18:
            return color[1]
        elif 2 <= j <= 4 or 6 < j <= 8 or 10 < j <= 12 or 14 < j <= 16 or 18 < j <= 20:
            return color[0]
    elif 16 <= i <= 18:
        if 0 <= j <= 2 or 4 < j <= 6 or 8 < j <= 10 or 12 < j <= 14 or 16 < j <= 18:
            return color[0]
        elif 2 <= j <= 4 or 6 < j <= 8 or 10 < j <= 12 or 14 < j <= 16 or 18 < j <= 20:
            return color[1]
    elif 18 <= i <= 20:
        if 0 <= j <= 2 or 4 < j <= 6 or 8 < j <= 10 or 12 < j <= 14 or 16 < j <= 18:
            return color[1]
        elif 2 <= j <= 4 or 6 < j <= 8 or 10 < j <= 12 or 14 < j <= 16 or 18 < j <= 20:
            return color[0]
    return None


def _get_color_plus_minus(i, j, color):
    if i >= j:
        return color[0]
    return color[1]


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _create_matrix(self, header, matrix_should_be, num_lst):
        header_result = [{'name': f'{header[0]['name']} {matrix_should_be}'}]
        matrix_result = []
        color = BG_COLOR_PLUS
        if matrix_should_be == '-':
            color = BG_COLOR_MINUS
        elif matrix_should_be == '+/-':
            # should change the color pattern
            pass

        values = num_lst
        tmp = [{'name': "{:0.2f}".format(num)} for num in values]
        if matrix_should_be == '+/-':
            tmp = tmp[2:]
        header_result += tmp
        # Create the matrix with the 8-cell block pattern
        query_optimise_dict_for_j = {}
        for i in values:
            # i is SPHERE
            spd_id = self.env['product.attribute.value'].search(
                [('name', '=', str(i)), ('attribute_id.name', '=', 'Sphere')]).id
            if matrix_should_be == "+/-" and i in [0]:
                continue
            tmp = []
            tmp.append({'name': "{:0.2f}".format(i)})
            for j in values:
                # j is CYLINDER
                if matrix_should_be == "+/-" and j in [0, 0.25]:
                    continue
                j_id = query_optimise_dict_for_j.get(j, None)
                if j_id is None:
                    cyl_id = self.env['product.attribute.value'].search(
                        [('name', '=', str(j)), ('attribute_id.name', '=', 'Cylinder')]).id
                    query_optimise_dict_for_j[j] = cyl_id

                tmp.append({
                    # first is cylinder, second one is (sphere or row)
                    'ptav_ids': [cyl_id, spd_id],
                    'qty': 0,
                    'is_possible_combination': True,
                    'color': _get_color(i, j, color) if matrix_should_be in ['+', '-'] else _get_color_plus_minus(i, j,
                                                                                                                  color)
                    # Get color based on j
                })
            matrix_result.append(tmp)
        return header_result, matrix_result

    def _get_template_matrix(self, **kwargs):
        self.ensure_one()
        company_id = kwargs.get('company_id', None) or self.company_id or self.env.company
        currency_id = kwargs.get('currency_id', None) or self.currency_id
        display_extra = kwargs.get('display_extra_price', False)
        attribute_lines = self.valid_product_template_attribute_line_ids

        Attrib = self.env['product.template.attribute.value']
        first_line_attributes = attribute_lines[0].product_template_value_ids._only_active()
        attribute_ids_by_line = [line.product_template_value_ids._only_active().ids for line in attribute_lines]

        header = [{"name": self.display_name}] + [
            attr._grid_header_cell(
                fro_currency=self.currency_id,
                to_currency=currency_id,
                company=company_id,
                display_extra=display_extra
            ) for attr in first_line_attributes]

        result = [[]]
        for pool in attribute_ids_by_line:
            result = [x + [y] for y in pool for x in result]
        args = [iter(result)] * len(first_line_attributes)
        rows = itertools.zip_longest(*args)

        matrix = []
        for row in rows:
            row_attributes = Attrib.browse(row[0][1:])
            row_header_cell = row_attributes._grid_header_cell(
                fro_currency=self.currency_id,
                to_currency=currency_id,
                company=company_id,
                display_extra=display_extra)
            result = [row_header_cell]

            for cell in row:
                combination = Attrib.browse(cell)
                is_possible_combination = self._is_combination_possible(combination)
                cell.sort()
                result.append({
                    "ptav_ids": cell,
                    "qty": 0,
                    "is_possible_combination": is_possible_combination
                })
            matrix.append(result)
        # Check if product has Cylinder and Sphere as attribute to open matrix from  0 to 20

        product_name = self.valid_product_template_attribute_line_ids.product_tmpl_id.name
        count_att = len(self.env['product.attribute'].search(
            ['&', ('product_tmpl_ids', '=', product_name), '|', ('name', '=', 'Sphere'), ('name', '=', 'Cylinder')]))
        if count_att > 1:
            # selected matrix from range +,- or +/-
            matrix_should_be = '+/-'
            num_lst = [round(i * 0.25, 2) for i in range(0, int(20 / 0.25) + 1)]
            header, matrix = self._create_matrix(header, matrix_should_be, num_lst)

        return {
            "header": header,
            "matrix": matrix,
        }


class ProductTemplateAttributeValue(models.Model):
    _inherit = "product.template.attribute.value"

    def _grid_header_cell(self, fro_currency, to_currency, company, display_extra=True):
        """Generate a header matrix cell for 1 or multiple attributes.

        :param res.currency fro_currency:
        :param res.currency to_currency:
        :param res.company company:
        :param bool display_extra: whether extra prices should be displayed in the cell
            True by default, used to avoid showing extra prices on purchases.
        :returns: cell with name (or price if any price_extra is defined on self)
        :rtype: dict
        """
        header_cell = {
            'name': ' • '.join([attr.name for attr in self]) if self else " "
        }  # The " " is to avoid having 'Not available' if the template has only one attribute line.
        extra_price = sum(self.mapped('price_extra')) if display_extra else 0
        if extra_price:
            header_cell['currency_id'] = to_currency.id
            header_cell['price'] = fro_currency._convert(
                extra_price, to_currency, company, fields.Date.today())
        return header_cell
