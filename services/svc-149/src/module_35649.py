"""Service module 35649: business logic, no crypto."""


def calculate_total_35649(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35649():
    return 'module 35649 handles orders and invoices'
