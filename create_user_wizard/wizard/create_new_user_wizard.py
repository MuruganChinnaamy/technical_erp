from openerp import models, fields, api, _
from openerp.exceptions import ValidationError

# wizard is created for new user creation

class create_new_user_wizard(models.TransientModel):
    _name = 'create.new.user.wizard'
    _order = "groups_ids"

    client_id = fields.Many2one('res.company', string="Primary Client", required=True)
    groups_ids = fields.Many2one('res.groups', string="User Type", required=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    email = fields.Char(string="Email Address", required=True)
    login = fields.Char(string="Login", required=True)
    password = fields.Char(string="Password")
    confirm_password = fields.Char(string=" Confirm Password")
    is_user_settings = fields.Boolean(string="Open User Settings")
    
    
    
    @api.depends('confirm_password')
    @api.onchange('confirm_password')
    def onchange_confirm_password(self):
        warning = False
        if self.confirm_password and not self.confirm_password == self.password:
            self.password = self.confirm_password = False
            warning = {
                        'title': _('ValidationError!'),
                        'message' : _("Password and confirm password should be unique!")
            }
        return {'warning': warning}
            

    @api.multi
    def button_create(self):
        groups_ids = []
    
        employee_grp = self.env['res.groups'].search([('name', '=', 'Employee')])
        if employee_grp:
            groups_ids.append(employee_grp.id)
        contact_creation_grp = self.env['res.groups'].search([('name', '=', 'Contact Creation')])
        if contact_creation_grp:
            groups_ids.append(contact_creation_grp.id)
        if self.groups_ids:
            groups_ids = groups_ids + self.groups_ids.ids
    
        user_dict = {
            'name': self.first_name,
            'login': self.login,
            'password': self.password,
            'company_ids': (1,self.client_id.id),
            'company_id': self.client_id.id,
            'groups_id': [(6, 0, groups_ids)],
            'in_group_6':True,
        }
        is_already_exists = self.env['res.users'].search([('login', '=', self.login)])
        if is_already_exists:
            warning = {
                        'title': _('ValidationError!'),
                        'message' : _("Entered login is already exists! kindly enter different one!")
            }
            return {'warning': warning}            
       
        else:            
            new_user = self.env['res.users'].sudo().create(user_dict)
            user_id = new_user

        if self.is_user_settings:
            return {
                'name': 'view_users_form',
                'view_type': 'form',
                'view_mode': 'tree',
                'views': [(self.env.ref('base.view_users_form').id, 'form')],
                'res_model': 'res.users',
                'view_id': self.env.ref('base.view_users_form').id,
                'type': 'ir.actions.act_window',
                'res_id': user_id.id,
                'target': 'current',
                'context': self._context.copy(),
            }
    
class res_groups(models.Model):
    _name = 'res.groups'
    _inherit = "res.groups" 
    _rec_name = 'name'
    _order = "id"

