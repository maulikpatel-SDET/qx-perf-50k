"""Service module 6049: business logic, no crypto."""


def calculate_total_6049(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6049():
    return 'module 6049 handles orders and invoices'
