"""Service module 45387: business logic, no crypto."""


def calculate_total_45387(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45387():
    return 'module 45387 handles orders and invoices'
