from odoo import http
from odoo.http import request
import os

class EcadController(http.Controller):
    @http.route('/api/ecad/resolve/v1', type='json', auth='none', methods=['POST'], csrf=False, website=False)
    def resolve_v1(self, **kwargs):
        expected_key = os.getenv('RESOLVER_API_KEY')
        auth_header = request.httprequest.headers.get('Authorization')
        if not auth_header or auth_header != f"Bearer {expected_key}":
            return {"error": "Unauthorized: Invalid API Key"}
        
        api_user_id = os.getenv('RESOLVER_API_USER_ID')
        #env = request.env(user=int(api_user_id))
        
        
        intent = kwargs.get('intent')
        if not intent:
            return {
                'status': 'error',
                'message': 'No intent data provided'
            }
        try:
            api_user = request.env['res.users'].sudo().browse(int(api_user_id))
            #result = request.env['product.template'].ecad_resolve_v1(intent)
            #result = env['product.template'].ecad_resolve_v1(intent)
            result = request.env['product.template'].with_user(api_user).ecad_resolve_v1(intent)
            return result
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e),
                'api_version': '1.0'
            }