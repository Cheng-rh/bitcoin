#!/usr/bin/python
# Created with pycharm.
# File Name: TestReader
# User: sssd
# Date: 2018/4/19 10:01
# Version: V1.0
# To change this template use File | Settings | File Templates.
# Description:    用来解析 bitcoin  block 中的一些信息

import config
import os
from handleDat.reader import BlockchainFileReader

base_path = config.BASE_PATH


def readDat():
    data_path = os.path.join(base_path, 'data', 'blk00000.dat')
    block = BlockchainFileReader(data_path)
    total_consumed = 0
    for i, block in enumerate(block):
        total_consumed += block.header.block_size + 8
        # 获取该区块中的交易记录
        transactions = block.transactions
        num_transactions = len(transactions)
        print('total transactions:', num_transactions)
        for transaction in transactions:
            transaction_version = transaction.version
            transaction_time = transaction.lock_time
            transaction_hash = transaction.txn_hash
            transaction_out_num = len(transaction.outputs)
            transaction_in_num = len(transaction.inputs)
            # 获取区块的收入列表
            pre_hash = transaction.inputs[0].previous_hash
            out_address = transaction.outputs[0].address
            pub_key = transaction.outputs[0].script_pub_key
            print('-------------- 开始解析第%d个交易')


        print(transactions)
        print('magic number', block.header.magic_number)
        print('previous hash', block.header.previous_hash)
        print('merkle hash', block.header.merkle_hash)
        print('total consumed', total_consumed)
        print('total transactions', len(block.transactions))


if __name__ == '__main__':
    readDat()
    pass
