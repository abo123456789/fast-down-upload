# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2019/10/19 22:25
"""
上传视频到阿里云oss
"""
import traceback
from typing import Callable

import oss2, os
from py_log import get_logger

from fast_down_upload import configs as config

logger = logger = get_logger(__name__,formatter_template=1)

auth = oss2.Auth(config.aliyun_access_key_id, config.aliyun_access_key_secret)
endpoint = config.aliyun_endpoint
bucket_name = config.aliyun_bucket_name
bucket = oss2.Bucket(auth, config.aliyun_endpoint, config.aliyun_bucket_name)


class UploadloadVideo(object):

    def __init__(self,source_url:str, file_name:str='', file_dir:str='video',file_type:str='',callback: Callable = None):
        """
            :param down_url: 上传文件原始url
            :param file_name: 上传的资源名称
            :param file_dir: 上传的资源文件夹名称
            :param file_type: 上传的资源后缀名 mp4
            :param callback: 上传完成后执行的回调函数
            """
        self.source_url = source_url
        self.file_dir = file_dir
        self.callback = callback
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = os.path.basename(source_url).split('.')[0]
        if file_type:
            self.file_type =file_type
        else:
            if len(self.file_name.split('.'))==2:
                    self.file_type = self.file_name.split('.')[1]
            else:
                self.file_type = 'mp4'
        self.video_path = f'/root/local_videos/{self.file_dir}/{self.file_name}.{self.file_type}'
        logger.info(f'file_name:{self.file_name},file_dir:{self.file_dir},video_path:{self.video_path}')

    def upload_video(self):
        try:
            logger.info(f'{self.file_name}.{self.file_type}-- 上传开始 --')
            logger.info(f'video_path:{self.video_path},file_dir:{self.file_dir},{self.file_name+"."+self.file_type}')
            with open(self.video_path, 'rb') as fileobj:
                fileobj.seek(0, os.SEEK_SET)
                # Tell方法用于返回当前位置。
                fileobj.tell()
                bucket.put_object('{}/{}'.format(self.file_dir, self.file_name+'.'+self.file_type), fileobj)

                logger.info(f'{self.file_name}.{self.file_type}-- 上传结束 --')
        except:
            ems = traceback.format_exc()
            logger.error(ems)
            raise RuntimeError(ems)
        finally:
            self.delete_video()
            if self.callback:
                self.callback()

    def delete_video(self):
        """
        删除在服务器的视频,字幕,备份,节约内存.
        :return:
        """
        if os.path.exists(self.video_path):
            os.remove(self.video_path)
            logger.info(f'{self.file_name}>>> remove success!!! <<<')


if __name__ == '__main__':
    print('上传')
    url = 'https://video1.matafy.com/dyvideo/201811/6609568770908228877.mp4'
    def upload_callback():
        print('excute download callback')
    uploadloadVideo = UploadloadVideo(source_url=url,file_name='',file_dir='douyin',file_type='',callback=upload_callback)
    uploadloadVideo.upload_video()