"""Service module 448: business logic, no crypto."""


def calculate_total_448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_448():
    return 'module 448 handles orders and invoices'
