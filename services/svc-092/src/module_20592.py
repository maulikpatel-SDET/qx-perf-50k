"""Service module 20592: business logic, no crypto."""


def calculate_total_20592(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20592():
    return 'module 20592 handles orders and invoices'
