"""Service module 23248: business logic, no crypto."""


def calculate_total_23248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23248():
    return 'module 23248 handles orders and invoices'
