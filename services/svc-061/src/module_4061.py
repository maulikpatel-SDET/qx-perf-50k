"""Service module 4061: business logic, no crypto."""


def calculate_total_4061(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4061():
    return 'module 4061 handles orders and invoices'
