"""Service module 1594: business logic, no crypto."""


def calculate_total_1594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1594():
    return 'module 1594 handles orders and invoices'
