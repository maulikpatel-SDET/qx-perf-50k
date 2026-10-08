"""Service module 12516: business logic, no crypto."""


def calculate_total_12516(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12516():
    return 'module 12516 handles orders and invoices'
