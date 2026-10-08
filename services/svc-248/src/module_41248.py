"""Service module 41248: business logic, no crypto."""


def calculate_total_41248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41248():
    return 'module 41248 handles orders and invoices'
