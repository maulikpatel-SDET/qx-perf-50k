"""Service module 22006: business logic, no crypto."""


def calculate_total_22006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22006():
    return 'module 22006 handles orders and invoices'
