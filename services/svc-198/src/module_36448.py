"""Service module 36448: business logic, no crypto."""


def calculate_total_36448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36448():
    return 'module 36448 handles orders and invoices'
