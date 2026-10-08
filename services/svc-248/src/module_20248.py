"""Service module 20248: business logic, no crypto."""


def calculate_total_20248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20248():
    return 'module 20248 handles orders and invoices'
