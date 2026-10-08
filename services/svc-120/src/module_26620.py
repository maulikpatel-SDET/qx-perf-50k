"""Service module 26620: business logic, no crypto."""


def calculate_total_26620(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26620():
    return 'module 26620 handles orders and invoices'
