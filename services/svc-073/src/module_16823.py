"""Service module 16823: business logic, no crypto."""


def calculate_total_16823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16823():
    return 'module 16823 handles orders and invoices'
