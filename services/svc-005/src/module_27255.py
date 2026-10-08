"""Service module 27255: business logic, no crypto."""


def calculate_total_27255(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27255():
    return 'module 27255 handles orders and invoices'
