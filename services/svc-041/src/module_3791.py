"""Service module 3791: business logic, no crypto."""


def calculate_total_3791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3791():
    return 'module 3791 handles orders and invoices'
