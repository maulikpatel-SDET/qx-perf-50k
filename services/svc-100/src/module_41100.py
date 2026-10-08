"""Service module 41100: business logic, no crypto."""


def calculate_total_41100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41100():
    return 'module 41100 handles orders and invoices'
