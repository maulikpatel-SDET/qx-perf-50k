"""Service module 22091: business logic, no crypto."""


def calculate_total_22091(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22091():
    return 'module 22091 handles orders and invoices'
