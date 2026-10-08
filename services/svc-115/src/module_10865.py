"""Service module 10865: business logic, no crypto."""


def calculate_total_10865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10865():
    return 'module 10865 handles orders and invoices'
