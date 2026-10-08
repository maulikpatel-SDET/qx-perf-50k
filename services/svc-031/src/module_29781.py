"""Service module 29781: business logic, no crypto."""


def calculate_total_29781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29781():
    return 'module 29781 handles orders and invoices'
