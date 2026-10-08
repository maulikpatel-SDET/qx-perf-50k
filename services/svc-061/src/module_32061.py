"""Service module 32061: business logic, no crypto."""


def calculate_total_32061(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32061():
    return 'module 32061 handles orders and invoices'
