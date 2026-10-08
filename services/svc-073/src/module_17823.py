"""Service module 17823: business logic, no crypto."""


def calculate_total_17823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17823():
    return 'module 17823 handles orders and invoices'
