odoo.define('lumi_after_sale_detect.one2many_checkbox', function (require) {
    "use strict";
    var FieldOne2Many = require('web.relational_fields').FieldOne2Many;
    var registry = require('web.field_registry');
    var ListRenderer = require('web.ListRenderer');
    var core = require('web.core');
    // var AbstractField = require('web.AbstractField');
    var qweb = core.qweb;
    // var g_enquiry_bom_add_quote = false;
    var CronFieldOne2Many = FieldOne2Many.extend({
        // events: _.extend({
        //     'click .enquiry_bom_batch_reply_price': '_onBatchReplyPrice',
        //     'click .enquiry_bom_download_enquiry': '_onDownloadEnquiry',
        //     'click .enquiry_bom_upload_reply_price': '_onUploadEnquiry',
        //     'click .enquiry_bom_not_reply_price': '_onNotReplyPrice',
        //     'click .enquiry_bom_reject_enquiry': '_onRejectEnquiry',
        // }, AbstractField.prototype.events),

        _getRenderer: function () {
            if (this.view.arch.tag === 'tree') {
                return CronFieldListRenderer
            }
            return this._super.apply(this, arguments)
        },

        // _renderButtons: function () {
        //     this._super.apply(this, arguments)
        //     if (this.view.arch.tag === 'tree') {
        //         this.$buttons = $(qweb.render('EnquiryBomIdsTree.buttons', {
        //             g_enquiry_bom_add_quote: g_enquiry_bom_add_quote
        //         }));
        //     }
        // },
        // // 批量回价
        // _onBatchReplyPrice: function (ev) {
        //
        // },
        // // 下载询价
        // _onDownloadEnquiry: function (ev) {
        // },
        // // 上传回价
        // _onUploadEnquiry: function (ev) {
        // },
        // // 不回价
        // _onNotReplyPrice: function (ev) {
        // },
        // // 驳回
        // _onRejectEnquiry: function (ev) {
        // },
    });
    var CronFieldListRenderer = ListRenderer.extend({
        init: function (parent, state, params) {
            this._super.apply(this, arguments);
            if ('hasSelectors_one2Many' in params.arch.attrs && params.arch.attrs['hasSelectors_one2Many']) {
                this.hasSelectors = true
            }
        },
        // _renderRow: function (record) {
        //     var $row = this._super.apply(this, arguments);
        //     if (this.hasSelectors) {
        //         var arr = ['no_refund', 'reject', 'invalid'];
        //         if (arr.indexOf(record.data.state) > -1) {
        //             $row.find('input[type=checkbox]').attr('disabled', 'disabled')
        //         }
        //     }
        //     return $row;
        // },
    });
    registry.add('one2many_checkbox', CronFieldOne2Many);
});