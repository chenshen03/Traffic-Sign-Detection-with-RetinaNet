#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: CHEN Shen

import json
import os
import shutil


def gene_gt(annos_path, output_path, transform=False, image_ext='jpg'):
    """
    利用预测得到的annotations，生成每张图片对应的ground_truth文件
    :param annos_path: annotation路径
    :param output_path: 输出路径
    :param transform: 是否将ground truth转换到1280*1024的情况
    :param image_ext: 图片的扩展名
    """
    assert os.path.exists(annos_path)
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.mkdir(output_path)

    anns = json.load(open(annos_path, 'r'))
    for imgid in anns['imgs']:
        img_name = imgid + image_ext
        gt_name = imgid + '.txt'
        with open(os.path.join(output_path, gt_name), 'w') as fout:
            print imgid
            for bboxs in anns['imgs'][imgid]['objects']:
                res = ""
                category = bboxs['category']
                bbox = bboxs['bbox']
                x_min = bbox['xmin']
                x_max = bbox['xmax']
                y_min = bbox['ymin']
                y_max = bbox['ymax']
                if transform == True:
                    x_min *= (1280/512)
                    x_max *= (1280/512)
                    y_min *= (1024/512)
                    y_max *= (1024/512)
                res += (img_name+" "+category+" "+str(x_min)+" "+str(y_min)+" "+str(x_max)+" "+str(y_max)+"\n")
                fout.write(res)


if __name__ == '__main__':
    annos_path = './data/valid_target.json'
    output_path = './result/ground_truth'
    gene_gt(annos_path, output_path, True)
