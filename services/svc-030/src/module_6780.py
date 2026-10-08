"""Service module 6780: business logic, no crypto."""


def calculate_total_6780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6780():
    return 'module 6780 handles orders and invoices'
