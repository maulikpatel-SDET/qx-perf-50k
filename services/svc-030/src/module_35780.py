"""Service module 35780: business logic, no crypto."""


def calculate_total_35780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35780():
    return 'module 35780 handles orders and invoices'
