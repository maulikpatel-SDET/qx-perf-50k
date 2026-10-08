"""Service module 17592: business logic, no crypto."""


def calculate_total_17592(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17592():
    return 'module 17592 handles orders and invoices'
