"""Service module 39448: business logic, no crypto."""


def calculate_total_39448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39448():
    return 'module 39448 handles orders and invoices'
