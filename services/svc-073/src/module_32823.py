"""Service module 32823: business logic, no crypto."""


def calculate_total_32823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32823():
    return 'module 32823 handles orders and invoices'
