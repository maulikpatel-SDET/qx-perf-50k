"""Service module 35579: business logic, no crypto."""


def calculate_total_35579(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35579():
    return 'module 35579 handles orders and invoices'
