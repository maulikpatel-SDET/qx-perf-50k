"""Service module 46061: business logic, no crypto."""


def calculate_total_46061(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46061():
    return 'module 46061 handles orders and invoices'
