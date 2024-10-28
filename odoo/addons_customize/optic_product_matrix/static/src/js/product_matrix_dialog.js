/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { Dialog } from '@web/core/dialog/dialog';
import { formatMonetary } from "@web/views/fields/formatters";
import { useHotkey } from "@web/core/hotkeys/hotkey_hook";
import { Component, onMounted, markup, useRef } from "@odoo/owl";
import { patch } from "@web/core/utils/patch";
import { ProductMatrixDialog } from "@product_matrix/js/product_matrix_dialog";

export class ProductMatrixDialogOptic extends Component {
    setup() {
        this.size = 'fullscreen';
        this.title = _t("Choose Product SAEID");
        console.log('hey saeid',this.props.product_template_id)

        const productMatrixRef = useRef('productMatrix');
        useHotkey("enter", () => this._onConfirm(), {
            bypassEditableProtection: true,
            area: () => productMatrixRef.el,
        });

        onMounted(() => {
            if (this.props.editedCellAttributes.length) {
                const inputs = document.getElementsByClassName('o_matrix_input');
                Array.from(inputs).filter((matrixInput) =>
                    matrixInput.attributes.ptav_ids.nodeValue === this.props.editedCellAttributes
                )[0].select();
            } else {
                document.getElementsByClassName('o_matrix_input')[0].select();
            }
        });
    }

    _format({ price, currency_id }) {
        if (!price) { return ""; }
        const sign = price < 0 ? '-' : '+';
        const formatted = formatMonetary(
            Math.abs(price),
            { currencyId: currency_id },
        );
        return markup(`&nbsp;${sign}&nbsp;${formatted}&nbsp;`);
    }

    _onConfirm() {
        const inputs = document.getElementsByClassName('o_matrix_input');
        let matrixChanges = [];
        for (let matrixInput of inputs) {
            if (matrixInput.value && matrixInput.value !== matrixInput.nodeValue) {
                matrixChanges.push({
                    qty: parseFloat(matrixInput.value),
                    ptav_ids: matrixInput.attributes.ptav_ids.nodeValue.split(",").map(
                        id => parseInt(id)
                    ),
                });
            }
        }
        if (matrixChanges.length > 0) {
            this.props.record.update({
                grid: JSON.stringify({
                    changes: matrixChanges,
                    product_template_id: this.props.product_template_id
                }),
                grid_update: true // to say that the changes to grid have to be applied to the SO.
            });
        }
        this.props.close();
    }
}

ProductMatrixDialogOptic.template = 'product_matrix.dialog';
ProductMatrixDialogOptic.props = {
    header: { type: Object },
    rows: { type: Object },
    editedCellAttributes: { type: String },
    product_template_id: { type: Number },
    record: { type: Object },
    close: { type: Function },
};
ProductMatrixDialogOptic.components = { Dialog };

patch(ProductMatrixDialog.prototype, ProductMatrixDialogOptic.prototype);