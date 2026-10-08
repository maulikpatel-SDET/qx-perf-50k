"""Service module 5091: business logic, no crypto."""


def calculate_total_5091(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5091():
    return 'module 5091 handles orders and invoices'
