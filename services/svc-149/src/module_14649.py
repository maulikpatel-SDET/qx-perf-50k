"""Service module 14649: business logic, no crypto."""


def calculate_total_14649(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14649():
    return 'module 14649 handles orders and invoices'
