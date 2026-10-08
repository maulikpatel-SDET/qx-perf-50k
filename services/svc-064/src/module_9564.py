"""Service module 9564: business logic, no crypto."""


def calculate_total_9564(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9564():
    return 'module 9564 handles orders and invoices'
