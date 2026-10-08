"""Service module 31351: business logic, no crypto."""


def calculate_total_31351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31351():
    return 'module 31351 handles orders and invoices'
