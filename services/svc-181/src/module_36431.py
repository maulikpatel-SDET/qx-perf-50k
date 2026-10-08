"""Service module 36431: business logic, no crypto."""


def calculate_total_36431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36431():
    return 'module 36431 handles orders and invoices'
