"""Service module 14280: business logic, no crypto."""


def calculate_total_14280(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14280():
    return 'module 14280 handles orders and invoices'
