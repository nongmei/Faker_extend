# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as CreditCardProvider
from .. import CreditCard
from collections import OrderedDict


class Provider(CreditCardProvider):

    # 大陆信用卡
    prefix_icbc = ["427018", "451804", "6253098", "427029", "628286", "628288", "62458071", "427039", "622230"]
    prefix_abc = ["625964", "356896", "356895", "559051", "625362", "558895", "628266", "557080", "436718"]
    prefix_ccb = ["403361", "520083", "622839", "520082", "625996", "519413", "552599", "404117", "625998"]
    prefix_boc = ["514957", "622760", "553131", "512316", "409665", "512315", "409666", "628313", "514958"]
    prefix_bcm = ["0053783", "521899", "622253", "520169", "622656", "628218", "955591", "522964", "955590", "622250"]
    prefix_cmbc = ["622623", "622600", "622602", "545393", "421870", "356857", "356856", "464580", "622621", "517636"]
    prefix_cmb = ["545948", "552587", "545623", "479228", "356888", "552534", "439188", "622581", "356887", "545619"]
    prefix_cib = ["625084", "625961", "625082", "622572", "527414", "549633", "625087", "548738", "625962", "622901"]
    prefix_ceb = ["622685", "356838", "622659", "356837"]
    prefix_citic = ["514906", "622918", "376969", "403393", "622767", "404158", "558916", "376966", "622689", "622680"]
    prefix_hxb = ["523959", "528709", "625969", "625967", "622636", "628318", "622638", "625968"]
    prefix_spdb = ["625831", "625833", "625970", "625971", "377187"]
    prefix_gdb = ["491037", "625072", "622557", "625806", "685800", "625808", "528931", "520382", "548844", "491032"]
    prefix_pingan = ["622526", "622525", "483536", "628296", "622157", "356869", "625360", "435744", "356868", "625823"]
    prefix_egb = ["625191"]
    prefix_cbhb = ["625122"]

    credit_card_types = OrderedDict((
        (u'工商银行',     CreditCard(u'工商银行',        prefix_icbc, 16)),
        (u'建设银行',     CreditCard(u'建设银行',        prefix_ccb, 16)),
        (u'农业银行',     CreditCard(u'农业银行',            prefix_abc, 16)),
        (u'中国银行',     CreditCard(u'中国银行',     prefix_boc, 16)),
        (u'交通银行',    CreditCard(u'交通银行',    prefix_bcm, 16)),
        (u'民生银行',   CreditCard(u'民生银行',     prefix_cmbc, 16)),
        (u'招商银行',    CreditCard(u'招商银行',    prefix_cmb, 16)),
        (u'兴业银行',    CreditCard(u'兴业银行',    prefix_cib, 16)),
        (u'光大银行',    CreditCard(u'光大银行',    prefix_ceb, 16)),
        (u'中信银行',    CreditCard(u'中信银行',    prefix_citic, 16)),
        (u'华夏银行',    CreditCard(u'华夏银行',    prefix_hxb, 16)),
        (u'浦发银行',    CreditCard(u'浦发银行',    prefix_spdb, 16)),
        (u'广发银行',    CreditCard(u'广发银行',    prefix_gdb, 16)),
        (u'平安银行',    CreditCard(u'平安银行',    prefix_pingan, 16)),
        (u'恒丰银行',    CreditCard(u'恒丰银行',    prefix_egb, 16)),
        (u'渤海银行',    CreditCard(u'渤海银行',    prefix_cbhb, 16))
    ))
