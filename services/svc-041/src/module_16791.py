"""Service module 16791: business logic, no crypto."""


def calculate_total_16791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16791():
    return 'module 16791 handles orders and invoices'
