"""Service module 9780: business logic, no crypto."""


def calculate_total_9780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9780():
    return 'module 9780 handles orders and invoices'
