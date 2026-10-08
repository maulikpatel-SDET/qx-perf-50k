"""Service module 6439: business logic, no crypto."""


def calculate_total_6439(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6439():
    return 'module 6439 handles orders and invoices'
