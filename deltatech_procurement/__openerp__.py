# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2015 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Deltatech Procurement",
    "version" : "1.0",
    "author" : "Dorin Hongu",
    "website" : "",
    "description": """
 
Features:
 - New fields in sale and purchase order: procurement_count, invoiced_rate
 - New buttons in sale and purchase order for display procurement order
 - New messages in log for procurement run. 
 - New object - Required product
 - New menu for Stock Outgoing, Stock Internal Transfer, Stock Incoming
 - Trecerea e la make_to_order la make_to_stock


    """,
    "category" : "Generic Modules/Stock",
    "depends" : ["base","stock","purchase",'procurement'],
 
    "data" : ['purchase_view.xml','required_product_view.xml','sale_view.xml','stock_view.xml','procurement_view.xml',
               'security/ir.model.access.csv',],
    "active": False,
    "installable": True,
}


