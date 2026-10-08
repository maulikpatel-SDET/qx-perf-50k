"""Service module 29594: business logic, no crypto."""


def calculate_total_29594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29594():
    return 'module 29594 handles orders and invoices'
