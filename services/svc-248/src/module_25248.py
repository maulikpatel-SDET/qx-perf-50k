"""Service module 25248: business logic, no crypto."""


def calculate_total_25248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25248():
    return 'module 25248 handles orders and invoices'
