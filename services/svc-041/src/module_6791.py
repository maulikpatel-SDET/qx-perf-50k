"""Service module 6791: business logic, no crypto."""


def calculate_total_6791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6791():
    return 'module 6791 handles orders and invoices'
