/** @odoo-module **/

import {CalendarController} from "@web/views/calendar/calendar_controller";
import {patch} from "@web/core/utils/patch";
import {session} from "@web/session";
import { CalendarCommonRenderer } from "@web/views/calendar/calendar_common/calendar_common_renderer";
import { renderToString } from "@web/core/utils/render";

class CalendarControllerJalali extends CalendarController {
    get today() {
        return DateTime.now().jalaliDate.dayFa;
    }

    get currentYear() {
        return this.date.jalaliDate.yearFa;
    }

    get dayHeader() {
        return `${this.date.jalaliDate.dayFa} ${this.date.jalaliDate.monthLong} ${this.date.jalaliDate.yearFa}`;
    }

    get weekHeader() {
        const { rangeStart, rangeEnd } = this.model;
        if (rangeStart.year != rangeEnd.year) {
            return `${rangeStart.jalaliDate.monthLong} ${rangeStart.jalaliDate.yearFa} - ${rangeEnd.jalaliDate.monthLong} ${rangeEnd.jalaliDate.yearFa}`;
        } else if (rangeStart.month != rangeEnd.month) {
            return `${rangeStart.jalaliDate.monthLong} - ${rangeEnd.jalaliDate.monthLong} ${rangeStart.jalaliDate.yearFa}`;
        }
        return `${rangeStart.jalaliDate.monthLong} ${rangeStart.jalaliDate.yearFa}`;
    }

    get currentMonth() {
        return `${this.date.jalaliDate.monthLong} ${this.date.jalaliDate.yearFa}`;
    }

    get currentWeek() {
        return this.date.jalaliDate.weekNumberFa;
    }


}
if(session.calendar === "jalali"){
patch(CalendarController.prototype, CalendarControllerJalali.prototype)

const { DateTime } = luxon;

patch(CalendarCommonRenderer.prototype, {

    getHeaderHtml(date) {
        const scale = this.props.model.scale;
        var {
            weekdayShort: weekdayShort,
            weekdayLong: weekdayLong,
            day,
        } = DateTime.fromJSDate(date);
        const jdate = new persianDate(date);
        day = jdate.toLocale('en').date();
        return renderToString(this.constructor.headerTemplate, {
            weekdayShort,
            weekdayLong,
            day,
            scale,
        });
    }
});
}
