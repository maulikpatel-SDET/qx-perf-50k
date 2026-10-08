"""Service module 49158: business logic, no crypto."""


def calculate_total_49158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49158():
    return 'module 49158 handles orders and invoices'
