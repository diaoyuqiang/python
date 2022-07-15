#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
from math import degrees, acos, cos, sin, atan2


class navPose:
    def __init__(self, _x=0, _y=0, _yaw=0, _h=0, _timestamp=None):
        self.x = _x
        self.y = _y
        self.yaw = _yaw
        self.h = _h
        self.np_array = np.array([_x, _y])
        self.timestamp = _timestamp

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_yaw(self, yaw):
        self.yaw = yaw

    @classmethod
    def deltaYaw(cls, p1_yaw, p2_yaw):
        curtDirection_npArray = np.array([cos(p1_yaw), sin(p1_yaw)])  # 向量角度的矩阵
        dstDirection_npArray = np.array([cos(p2_yaw), sin(p2_yaw)])
        # .T: 矩阵转置(行列互换)
        cos_value = np.dot(curtDirection_npArray, dstDirection_npArray.T)  # 两个向量的夹角余弦值
        # The cosine of an angle is always in the range [-1.0, 1.0]
        cos_value = 1 if cos_value > 1 else cos_value
        cos_value = -1 if cos_value < -1 else cos_value
        return acos(cos_value)  # 返回余弦值得弧度

    @classmethod
    def deltaDistance(cls, p1, p2):
        line_npArray = p1.np_array - p2.np_array
        return np.linalg.norm(line_npArray)  # 二范数即为线段的距离

    @classmethod
    def fromPoseStamped(cls, ps):
        ori = ps.pose.orientation
        import tf
        # 四元数转欧拉角
        yaw_rad = tf.transformations.euler_from_quaternion(
            [ori.x, ori.y, ori.z, ori.w])[2]
        return navPose(ps.pose.position.x, ps.pose.position.y, yaw_rad, _timestamp=ps.header.stamp.to_sec())

    @classmethod
    def fromPoseStamped_entershelf(cls, ps):
        ori = ps.pose.orientation
        import tf
        # 四元数转欧拉角
        yaw_rad = tf.transformations.euler_from_quaternion(
            [ori.x, ori.y, ori.z, ori.w])[2]
        return navPose(ps.pose.position.x + 0.035, ps.pose.position.y, yaw_rad, _timestamp=ps.header.stamp.to_sec())

    @classmethod
    def is_clockwise(cls, curt_yaw, tgt_yaw):
        a = np.array([cos(curt_yaw), sin(curt_yaw)])
        b = np.array([cos(tgt_yaw), sin(tgt_yaw)])

        # ax * by - ay * bx
        # -:Clockwise +:Anti-clockwise
        return np.linalg.det(np.array([a, b]))  # 返回向量的行列式

    def __repr__(self):
        return 'navPose[{:.3f}, {:.3f}, {:.3f}red, {:.3f}deg]'.format(
            self.x, self.y, self.yaw, degrees(self.yaw))

    def __add__(self, other):
        return navPose(self.x + other.x, self.y + other.y,
                       self.yaw + other.yaw)

    def __sub__(self, other):
        return navPose(self.x - other.x, self.y - other.y, self.yaw - other.yaw)
