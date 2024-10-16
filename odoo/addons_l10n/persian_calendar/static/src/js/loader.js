/** @odoo-module **/

import { onWillStart } from "@odoo/owl";
import { loadBundle, loadJS } from "@web/core/assets";
import { patch } from "@web/core/utils/patch";
import { WebClient } from "@web/webclient/webclient";


//
//patch(WebClient.prototype, {
//    setup() {
//        super.setup();
//        onWillStart(async () => {
//            if(luxon.DateTime.now().locale == 'fa-IR'){
//                console.log(luxon.DateTime.now())
//                await loadBundle("persian_calendar.calendar_persian");
//            }
//        });
//    }
//})
// static/src/js/webclient_patch.js

// static/src/js/webclient_patch.js

// static/src/js/webclient_patch.js

patch(WebClient.prototype, {
    setup() {
        super.setup(); // Correctly call the superclass setup method

        onWillStart(async () => {
            try {
                const user = await this.orm.read("res.users", [this.env.services.user.userId], ["calendar_type"]);
                console.log(user[0]);
                const calendarType = user[0].calendar_type;

                if (calendarType === 'shamsi') {
                    console.log("Loading Persian calendar...");
                    await loadBundle("persian_calendar.calendar_persian");
                }
            } catch (error) {
                console.error("Error loading calendar type:", error);
            }
        });
    },
});

