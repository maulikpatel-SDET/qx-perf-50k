"""Service module 40780: business logic, no crypto."""


def calculate_total_40780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40780():
    return 'module 40780 handles orders and invoices'
