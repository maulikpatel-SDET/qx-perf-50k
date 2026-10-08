"""Service module 18544: business logic, no crypto."""


def calculate_total_18544(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18544():
    return 'module 18544 handles orders and invoices'
