"""Service module 3594: business logic, no crypto."""


def calculate_total_3594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3594():
    return 'module 3594 handles orders and invoices'
