"""Service module 21780: business logic, no crypto."""


def calculate_total_21780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21780():
    return 'module 21780 handles orders and invoices'
