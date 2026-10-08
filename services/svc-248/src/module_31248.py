"""Service module 31248: business logic, no crypto."""


def calculate_total_31248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31248():
    return 'module 31248 handles orders and invoices'
