"""Service module 22823: business logic, no crypto."""


def calculate_total_22823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22823():
    return 'module 22823 handles orders and invoices'
