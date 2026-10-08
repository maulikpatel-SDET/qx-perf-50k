"""Service module 23564: business logic, no crypto."""


def calculate_total_23564(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23564():
    return 'module 23564 handles orders and invoices'
