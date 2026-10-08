"""Service module 22: business logic, no crypto."""


def calculate_total_22(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22():
    return 'module 22 handles orders and invoices'
