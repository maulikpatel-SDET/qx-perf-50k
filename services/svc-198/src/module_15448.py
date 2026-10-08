"""Service module 15448: business logic, no crypto."""


def calculate_total_15448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15448():
    return 'module 15448 handles orders and invoices'
