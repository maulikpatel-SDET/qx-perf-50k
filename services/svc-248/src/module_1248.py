"""Service module 1248: business logic, no crypto."""


def calculate_total_1248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1248():
    return 'module 1248 handles orders and invoices'
