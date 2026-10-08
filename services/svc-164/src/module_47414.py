"""Service module 47414: business logic, no crypto."""


def calculate_total_47414(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47414():
    return 'module 47414 handles orders and invoices'
