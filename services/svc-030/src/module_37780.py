"""Service module 37780: business logic, no crypto."""


def calculate_total_37780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37780():
    return 'module 37780 handles orders and invoices'
