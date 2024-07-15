from app.settings import settings
from fastapi_utils.inferring_router import InferringRouter
from app.service.partner import get_partner_detail
from fastapi_utils.cbv import cbv
from .base_response import make_response
from .base import UnauthenticatedBaseApi
from fastapi.encoders import jsonable_encoder
import logging

partner_api = InferringRouter()

# Initialize logger
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

@cbv(partner_api)
class Partner(UnauthenticatedBaseApi):
    @partner_api.get('/partner/{partner_id}')
    async def get_detail_partner(self, partner_id):
        try:
            resp = get_partner_detail(partner_id)
            logger.info(f"get by id /partner/{partner_id} endpoint is being hit")
            return make_response(message="success", payload=jsonable_encoder(resp))
        except Exception as e:
            logger.error(f"get by id /partner/{partner_id} endpoint is being hit (error) : {e}")
            return make_response(payload={'details': str(e)}, message='failed', code=400)
