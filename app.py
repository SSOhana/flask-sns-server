from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config
from resources.follow import FollowResource
from resources.like import LikeResource
from resources.posting import PostingInfoResource, PostingResource
from resources.tag import TagSearchResource

from resources.user import UserLoginResource, UserLogoutResource, UserRegisterResource, jwt_blacklist

app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(Config)

# JWT 토큰 라이브러리 만들기
jwt = JWTManager(app)

# 로그아웃 된 토큰이 들어있는 set을, jwt 에 알려준다.
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

api = Api(app)

# 경로와 리소스(API 코드)를 연결한다.
api.add_resource(UserRegisterResource, '/users/register')           # 회원가입 API
api.add_resource(UserLoginResource, '/users/login')                 # 로그인 API
api.add_resource(UserLogoutResource, '/users/logout')               # 로그아웃 API

api.add_resource(PostingResource, '/posting')                       # 포스팅 API

api.add_resource(FollowResource, '/follow/<int:follow_id>')         # 친구맺기 API
api.add_resource(TagSearchResource, '/posting/search/tag')          # 태그 검색 API
api.add_resource(LikeResource, '/like/<int:posting_id>')            # 좋아요 생성 API
api.add_resource(PostingInfoResource, '/posting/<int:posting_id>')  # 포스팅 수정 API

if __name__=="__main__" :
    app.run()