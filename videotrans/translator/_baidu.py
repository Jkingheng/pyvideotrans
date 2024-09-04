# -*- coding: utf-8 -*-
import hashlib
import time

import requests

from videotrans.configure import config
from videotrans.configure._except import LogExcept
from videotrans.translator._base import BaseTrans
from videotrans.util import tools


class Baidu(BaseTrans):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def _get_content(self,data):
        text ="\n".join(data)
        salt = int(time.time())
        strtext = f"{config.params['baidu_appid']}{text}{salt}{config.params['baidu_miyue']}"
        md5 = hashlib.md5()
        md5.update(strtext.encode('utf-8'))
        sign = md5.hexdigest()

        requrl = f"http://api.fanyi.baidu.com/api/trans/vip/translate?q={text}&from=auto&to={self.target_language}&appid={config.params['baidu_appid']}&salt={salt}&sign={sign}"

        config.logger.info(f'[Baidu]请求数据:{requrl=}')
        resraw = requests.get(requrl,proxies={"http":"","https":""})
        res = resraw.json()
        config.logger.info(f'[Baidu]返回响应:{res=}')

        if "error_code" in res or "trans_result" not in res or len(res['trans_result']) < 1:
            config.logger.info(f'Baidu 返回响应:{resraw}')
            raise LogExcept(res['error_msg'])

        result = [tools.cleartext(tres['dst']) for tres in res['trans_result']]
        if not result or len(result) < 1:
            raise LogExcept(f'{res}')
        return "\n".join(result)