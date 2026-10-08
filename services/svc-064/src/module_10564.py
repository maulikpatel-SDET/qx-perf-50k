"""Service module 10564: business logic, no crypto."""


def calculate_total_10564(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10564():
    return 'module 10564 handles orders and invoices'
