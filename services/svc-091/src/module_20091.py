"""Service module 20091: business logic, no crypto."""


def calculate_total_20091(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20091():
    return 'module 20091 handles orders and invoices'
