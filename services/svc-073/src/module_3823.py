"""Service module 3823: business logic, no crypto."""


def calculate_total_3823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3823():
    return 'module 3823 handles orders and invoices'
