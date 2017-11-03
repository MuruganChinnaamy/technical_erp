from openerp import api, fields, tools, models
import datetime
import calendar
import time





class hr_holidays(models.Model):
    _name = "hr.holidays"
    _description = "Leave"
    _inherit = ['hr.holidays']

    
    @api.multi
    def holidays_confirm2(self):
        res = super(hr_holidays, self).holidays_confirm(self, self._cr, self._uid, context=None)
        
        print"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        
        return res
        
        
        print "NNNNNNNNNNNNNNNNNNn"
        template = self.pool['ir.model.data'].get_object(self._cr, self._uid, 'demo', 'leave_email_template')
        for rec in self:
            print "SSSSSSSSSSSSSSSSSSSSSSSAAAAAAAA"
            date_start = datetime.datetime.strptime(rec.date_from, "%Y-%m-%d %H:%M:%S")
            month_start_date = date_start.replace(day=1, hour=00, minute=00, second=00)
            end_day = monthrange(month_start_date.year, month_start_date.month) 
            month_end_date = date_start.replace(day=end_day[1], hour=23, minute=59, second=59)            
            leaves = self.env['hr.holidays'].search([('date_from', '>=', str(month_start_date)),
                                                     ('date_from','<=',str(month_end_date)),
                                                     ('holiday_status_id','=', rec.holiday_status_id.id),
                                                     ('employee_id', '=', rec.employee_id.id),
                                                     ('state', '=', 'validate'),
                                                     ('holiday_type', '=', 'employee')])
            print len(leaves),"SSSSSSSSSSSSSSSSSS"

            if len(leaves)>=1:
                msg_id = self.pool['mail.template'].send_mail(self._cr, self._uid, template.id, rec.id, True, True, context=self._context)
        # return self.write(self._cr, self._uid, self._ids, {'state': 'confirm'})

    

from openerp.osv import fields, osv
from openerp.tools.translate import _
    

class hr_holidays(osv.osv):
    _inherit = "hr.holidays"
    
    
    def holidays_confirm(self, cr, uid, ids, context=None):
        
        template = self.pool.get('ir.model.data').get_object(cr, uid, 'demo2', 'leave_email_template1')
        for rec in self.browse(cr, uid, ids, context=context):
            print "SSSSSSSSSSSSSSSSSSSSSSSAAAAAAAA"
            date_start = datetime.datetime.strptime(rec.date_from, "%Y-%m-%d %H:%M:%S")
            month_start_date = date_start.replace(day=1, hour=00, minute=00, second=00)
            end_day = calendar.monthrange(month_start_date.year, month_start_date.month) 
            month_end_date = date_start.replace(day=end_day[1], hour=23, minute=59, second=59)            
            leaves = self.pool.get('hr.holidays').search(cr, uid, [('date_from', '>=', str(month_start_date)),
                                                     ('date_from','<=',str(month_end_date)),
                                                     ('holiday_status_id','=', rec.holiday_status_id.id),
                                                     ('employee_id', '=', rec.employee_id.id),
                                                     ('state', '=', 'validate'),
                                                     ('holiday_type', '=', 'employee')])
            print len(leaves),"SSSSSSSSSSSSSSSSSS"
#             if leaves:
#                 if 2>=1:
            msg_id = self.pool.get('mail.template').send_mail(cr, uid, template.id, rec.id, True, True, context=context)
        # return self.write(self._cr, self._uid, self._ids, {'state': 'confirm'})

        
        
        return self.write(cr, uid, ids, {'state': 'confirm'})    
    