"""Service module 18594: business logic, no crypto."""


def calculate_total_18594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18594():
    return 'module 18594 handles orders and invoices'
