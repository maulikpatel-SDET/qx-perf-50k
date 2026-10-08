"""Service module 48448: business logic, no crypto."""


def calculate_total_48448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48448():
    return 'module 48448 handles orders and invoices'
