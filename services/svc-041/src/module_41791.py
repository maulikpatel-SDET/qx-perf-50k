"""Service module 41791: business logic, no crypto."""


def calculate_total_41791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41791():
    return 'module 41791 handles orders and invoices'
