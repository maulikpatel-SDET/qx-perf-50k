"""Service module 3562: business logic, no crypto."""


def calculate_total_3562(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3562():
    return 'module 3562 handles orders and invoices'
