"""Service module 20781: business logic, no crypto."""


def calculate_total_20781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20781():
    return 'module 20781 handles orders and invoices'
