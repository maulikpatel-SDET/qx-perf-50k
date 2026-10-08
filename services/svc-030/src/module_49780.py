"""Service module 49780: business logic, no crypto."""


def calculate_total_49780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49780():
    return 'module 49780 handles orders and invoices'
