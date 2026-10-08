"""Service module 12594: business logic, no crypto."""


def calculate_total_12594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12594():
    return 'module 12594 handles orders and invoices'
