"""Service module 45791: business logic, no crypto."""


def calculate_total_45791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45791():
    return 'module 45791 handles orders and invoices'
