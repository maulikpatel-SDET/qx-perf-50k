"""Service module 13780: business logic, no crypto."""


def calculate_total_13780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13780():
    return 'module 13780 handles orders and invoices'
