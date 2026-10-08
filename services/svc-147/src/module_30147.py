"""Service module 30147: business logic, no crypto."""


def calculate_total_30147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30147():
    return 'module 30147 handles orders and invoices'
