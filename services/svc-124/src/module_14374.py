"""Service module 14374: business logic, no crypto."""


def calculate_total_14374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14374():
    return 'module 14374 handles orders and invoices'
