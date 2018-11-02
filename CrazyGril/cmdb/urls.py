#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
urlpatterns = patterns('',

url(r'^image_build', 'cmdb.views.image_build', name='image_build'),
url(r'^asset_info', 'cmdb.views.asset_info', name='asset_info'),
url(r'^asset_add', 'cmdb.views.asset_add', name='asset_add'),
url(r'^asset_edit', 'cmdb.views.asset_edit', name='asset_edit'),
url(r'^asset_del', 'cmdb.views.asset_del', name='asset_del'),
url(r'^asset_show', 'cmdb.views.asset_show', name='asset_show'),
url(r'^idc_info', 'cmdb.views.idc_info', name='idc_info'),
url(r'^idc_add', 'cmdb.views.idc_add', name='idc_add'),
url(r'^idc_cancel', 'cmdb.views.idc_cancel', name='idc_cancel'),
url(r'^group_connect', 'cmdb.views.group_connect', name='group_connect'),
url(r'^group_add', 'cmdb.views.group_add', name='group_add'),
url(r'^ajax_tran_data', 'cmdb.views.ajax_tran_data', name='ajax_tran_data'),
url(r'^idc_show', 'cmdb.views.idc_show', name='idc_show'),
url(r'^idc_edit', 'cmdb.views.idc_edit', name='idc_edit'),
url(r'^idc_del', 'cmdb.views.idc_del', name='idc_del'),
url(r'^idc_dels', 'cmdb.views.idc_dels', name='idc_dels'),
url(r'^group_edit', 'cmdb.views.group_edit', name='group_edit'),
url(r'^ajax_change_group', 'cmdb.views.ajax_change_group', name='ajax_change_group'),
url(r'^group_del', 'cmdb.views.group_del', name='group_del'),
url(r'^get_mongo_infos', 'cmdb.views.get_mongo_infos', name='get_mongo_infos'),
url(r'^wechat', 'cmdb.views.wechat', name='wechat'),
url(r'^alert_tem', 'cmdb.views.alert_tem', name='alert_tem'),
url(r'^create_alertTS', 'cmdb.views.create_alertTS', name='create_alertTS'),
url(r'^dingding_man', 'cmdb.views.dingding_man', name='dingding_man'),
url(r'^wechat_man', 'cmdb.views.wechat_man', name='wechat_man'),


url(r'^wac_man', 'cmdb.views.wac_man', name='wac_man'),

# group_back
# url(r'^group_add', 'cmdb.views.group_add', name='group_add'),
# group_back

)

