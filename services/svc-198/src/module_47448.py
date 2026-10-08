"""Service module 47448: business logic, no crypto."""


def calculate_total_47448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47448():
    return 'module 47448 handles orders and invoices'
