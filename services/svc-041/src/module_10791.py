"""Service module 10791: business logic, no crypto."""


def calculate_total_10791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10791():
    return 'module 10791 handles orders and invoices'
