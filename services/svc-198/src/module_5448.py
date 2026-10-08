"""Service module 5448: business logic, no crypto."""


def calculate_total_5448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5448():
    return 'module 5448 handles orders and invoices'
