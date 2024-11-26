import asyncio
import os

from tortoise import Tortoise, run_async

from schedulers.ton_contract_online_confirm import online_confirm


async def trigger():
    # 初始化数据库连接
    await init_data_con()
    # 定时任务业务调用
    await online_confirm()

async def init_data_con():
    await Tortoise.init(
        # 私网
        db_url=os.getenv('ms.db.url','mysql://codatta:W1PkWn2hfOAy@codatta-test-intl.rwlb.singapore.rds.aliyuncs.com/omnitags_db_orm'),
        # 公网
        # db_url='mysql://codatta:W1PkWn2hfOAy@codatta-test.rwlb.singapore.rds.aliyuncs.com/omnitags_db_orm',
        modules={'models': ['dao.models']}
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(trigger())
