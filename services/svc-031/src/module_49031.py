"""Service module 49031: business logic, no crypto."""


def calculate_total_49031(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49031():
    return 'module 49031 handles orders and invoices'
