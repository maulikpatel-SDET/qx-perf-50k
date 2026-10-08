"""Service module 84: business logic, no crypto."""


def calculate_total_84(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_84():
    return 'module 84 handles orders and invoices'
