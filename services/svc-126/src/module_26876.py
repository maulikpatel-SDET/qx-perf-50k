"""Service module 26876: business logic, no crypto."""


def calculate_total_26876(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26876():
    return 'module 26876 handles orders and invoices'
