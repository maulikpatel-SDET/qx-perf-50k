"""Service module 38780: business logic, no crypto."""


def calculate_total_38780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38780():
    return 'module 38780 handles orders and invoices'
