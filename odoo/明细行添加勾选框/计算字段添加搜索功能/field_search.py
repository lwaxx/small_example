class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'

    name = fields.Char(string='Name')
    value = fields.Integer(string='Value')
    calculated_field = fields.Float(string='Calculated Field', compute='_compute_calculated_field')

    @api.depends('name', 'value')
    def _compute_calculated_field(self):
        for record in self:
            record.calculated_field = record.value / len(record.name)

    def _search_calculated_field(self, operator, value):
        domain = []
        for record in self:
            if eval(str(record.calculated_field) + operator + str(value)):
                domain.append(record.id)
        return [('id', 'in', domain)]
