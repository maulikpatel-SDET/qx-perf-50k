"""Service module 13592: business logic, no crypto."""


def calculate_total_13592(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13592():
    return 'module 13592 handles orders and invoices'
