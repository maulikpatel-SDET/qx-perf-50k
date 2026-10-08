"""Service module 18649: business logic, no crypto."""


def calculate_total_18649(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18649():
    return 'module 18649 handles orders and invoices'
