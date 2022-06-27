from datetime import datetime
from http import HTTPStatus
from os import access
from flask import request
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, jwt_required
from flask_restful import Resource
from mysql.connector.errors import Error
from mysql_connection import get_connection
import mysql.connector

import boto3
from config import Config


# 클래스 생성
class TagSearchResource(Resource) :
    def get(self) :

        # 1. 클라이언트로부터 데이터를 받아온다.
        keyword = request.args['keyword']
        offset = request.args['offset']
        limit = request.args['limit']

        # 2. DB 에서 해당 키워드가 들어있는 태그에 해당되는 포스팅 정보 가져온다.


        return