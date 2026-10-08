"""Service module 8268: business logic, no crypto."""


def calculate_total_8268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8268():
    return 'module 8268 handles orders and invoices'
