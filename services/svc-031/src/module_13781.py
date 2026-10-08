"""Service module 13781: business logic, no crypto."""


def calculate_total_13781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13781():
    return 'module 13781 handles orders and invoices'
