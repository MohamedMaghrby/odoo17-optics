from odoo import models, fields, api, _

MATRIX_LENGTH = 10
STEPS = 2


class MatrixInput(models.TransientModel):
    _name = "matrix.input"
    _description = "Matrix input"

    @api.model
    def _create_dynamic_fields(self):
        dynamic_fields = {}
        for i in range(0, MATRIX_LENGTH, STEPS):
            field_name = f'field_{i}'
            dynamic_fields[field_name] = fields.Integer(string=f"{i}")
            # Dynamically set the field to the model
            setattr(self.__class__, field_name, dynamic_fields[field_name])
        return dynamic_fields

    @api.model
    def create(self, vals):
        self._create_dynamic_fields()  # Create dynamic fields on instance creation
        return super(MatrixInput, self).create(vals)

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        fields_dict = super(MatrixInput, self).fields_get(allfields=allfields, attributes=attributes)
        dynamic_fields = self._create_dynamic_fields()
        fields_dict.update(dynamic_fields)
        return fields_dict
