"""Service module 18780: business logic, no crypto."""


def calculate_total_18780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18780():
    return 'module 18780 handles orders and invoices'
