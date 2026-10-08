"""Service module 20147: business logic, no crypto."""


def calculate_total_20147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20147():
    return 'module 20147 handles orders and invoices'
