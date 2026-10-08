"""Service module 14564: business logic, no crypto."""


def calculate_total_14564(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14564():
    return 'module 14564 handles orders and invoices'
