
分布式文件下载上传
##### [介绍文档]

* 支持版本: python 3.6+

### 下载安装

* 安装依赖:

```shell
pip install fast-down-upload
```

* 下载上传说明
```shell
支持操作系统:(MAC,LINUX)
下载默认路径:/root/local_videos/
上传默认支持:aliyun oss
```

### 分布式下载上传DEMO


```python
    import fast_down_upload.configs as configs
    from fast_down_upload.StartDownUpload import public_downupload_task,start_customer_downupload_task

    # redis连接配置
    configs.redis_host = '127.0.0.1'
    configs.redis_password = ''
    configs.redis_port = 6379
    configs.redis_db = 0

    # ALIYUN OSS配置
    configs.aliyun_access_key_id = ''
    configs.aliyun_access_key_secret = ''
    configs.aliyun_endpoint = ''
    configs.aliyun_bucket_name = ''

    #发布下载上传任务
    for i in range(1,21):
        down_dict = {'down_url': 'https://video1.matafy.com/dyvideo/201811/6609568770908228877.mp4', 'file_name': 'test'+str(i),'file_dir': 'douyin', 'file_type': '', 'callback': None}
        public_downupload_task(down_dict)


    #消费下载上传任务
    start_customer_downupload_task(threads_num=100)

```
