"""Service module 25934: business logic, no crypto."""


def calculate_total_25934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25934():
    return 'module 25934 handles orders and invoices'
