"""Service module 24780: business logic, no crypto."""


def calculate_total_24780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24780():
    return 'module 24780 handles orders and invoices'
