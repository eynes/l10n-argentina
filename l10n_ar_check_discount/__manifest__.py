###############################################################################
#
#    Copyright (c) 2019 Eynes/E-MIPS
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    "name": "L10N AR Check Discount",
    "category": "Accounting & Finance",
    "version": "11.0.1.0.0",
    "author": "Eynes/E-MIPS",
    "license": "AGPL-3",
    "description": "Module Description",
    "depends": [
        "l10n_ar_account_check",
        "l10n_ar_perceptions_basic",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/account_check_view.xml",
        "views/check_discount_view.xml",
        "views/check_discount_settings_view.xml",
        "views/menuitems.xml",
    ],
    "installable": True,
    "application": True,
}
