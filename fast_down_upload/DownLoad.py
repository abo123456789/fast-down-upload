# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2019/10/19 22:25
# -*-coding:utf-8 -*-
"""
下载视屏到本地
"""
import traceback
from typing import Callable

from retrying import retry
from loguru import logger
import os
import requests
from tomorrow3 import threads as tomorrow_threads


class DownloadVideo(object):
    def __init__(self,down_url:str, file_name:str='', file_dir:str='video',file_type:str='',callback: Callable = None):
        """
        :param down_url: 待下载的资源url
        :param file_name: 保存的资源名称
        :param file_dir: 保存的资源文件夹名称
        :param file_type: 保存的资源后缀名 mp4
        :param callback: 下载完成后执行的回调函数
        """
        self.down_url = down_url
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = os.path.basename(down_url).split('.')[0]
        if file_type:
            self.file_type =file_type
        else:
            if len(self.file_name.split('.'))==2:
                    self.file_type = self.file_name.split('.')[1]
            else:
                self.file_type = 'mp4'
        self.file_dir = file_dir
        self.callback = callback
        self.video_path = f'/root/local_videos/{self.file_dir}'
        if os.path.isdir(self.video_path):
            pass
        else:
            os.mkdir(self.video_path)
        logger.info(f'down_url:{self.down_url}')
        logger.info(f'file_name:{self.file_name},file_dir:{self.file_dir},video_path:{self.video_path}')

    @retry(stop_max_attempt_number=3)
    def _send_request(self):
        resp = requests.get(self.down_url, timeout=6)
        return resp

    def download_video(self):
        '''
        下载视频到本地
        :return:
        '''
        try:
            if self.down_url:
                if len(self.file_name.split('.'))==1:
                    saveFile = f'{self.video_path}/{self.file_name}.{self.file_type}'
                else:
                    saveFile = f'{self.video_path}/{self.file_name}'
                logger.info(f'saveFile:{saveFile}')
                resp = self._send_request()
                with open(saveFile, "wb") as sub:
                    sub.write(resp.content)
                    logger.info('%s下载完毕' % saveFile)
            else:
                logger.info(f'########获取{self.videoId}下载地址失败########')
        except:
            s = traceback.format_exc()
            logger.error(s)
        # finally:
        #     if self.callback:
        #         self.callback()

if __name__ == '__main__':
    print('下载')
    down_url = 'https://video1.matafy.com/dyvideo/201811/6609568770908228877.mp4'
    # down_url = 'https://inews.gtimg.com/newsapp_bt/0/10562505649/1000'
    def download_callback():
        print('excute download callback')

    download_video = DownloadVideo(down_url,file_name='',file_dir='douyin',file_type='',callback=download_callback)
    download_video.download_video()
