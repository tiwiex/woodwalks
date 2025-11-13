import frappe

def get_context(context):
    context.products = frappe.get_all(
        "Item",
        fields=[
            "item_name",
            "item_code",
            "description",
            "image",
            "route"
        ],
        order_by="creation desc"
    )
    
    context.title = "Woodwalks - Premium Products"
    context.description = "Discover our collection of premium handcrafted products"
