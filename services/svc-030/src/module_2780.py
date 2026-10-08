"""Service module 2780: business logic, no crypto."""


def calculate_total_2780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2780():
    return 'module 2780 handles orders and invoices'
