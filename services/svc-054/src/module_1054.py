"""Service module 1054: business logic, no crypto."""


def calculate_total_1054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1054():
    return 'module 1054 handles orders and invoices'
