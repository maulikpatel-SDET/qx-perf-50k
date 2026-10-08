"""Service module 14789: business logic, no crypto."""


def calculate_total_14789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14789():
    return 'module 14789 handles orders and invoices'
