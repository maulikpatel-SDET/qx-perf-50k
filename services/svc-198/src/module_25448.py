"""Service module 25448: business logic, no crypto."""


def calculate_total_25448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25448():
    return 'module 25448 handles orders and invoices'
