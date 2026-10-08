"""Service module 3248: business logic, no crypto."""


def calculate_total_3248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3248():
    return 'module 3248 handles orders and invoices'
