"""Service module 1823: business logic, no crypto."""


def calculate_total_1823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1823():
    return 'module 1823 handles orders and invoices'
