"""Service module 11248: business logic, no crypto."""


def calculate_total_11248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11248():
    return 'module 11248 handles orders and invoices'
