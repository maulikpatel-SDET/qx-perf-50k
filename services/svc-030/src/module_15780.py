"""Service module 15780: business logic, no crypto."""


def calculate_total_15780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15780():
    return 'module 15780 handles orders and invoices'
