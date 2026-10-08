"""Service module 12564: business logic, no crypto."""


def calculate_total_12564(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12564():
    return 'module 12564 handles orders and invoices'
