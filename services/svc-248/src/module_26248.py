"""Service module 26248: business logic, no crypto."""


def calculate_total_26248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26248():
    return 'module 26248 handles orders and invoices'
