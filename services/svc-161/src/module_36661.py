"""Service module 36661: business logic, no crypto."""


def calculate_total_36661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36661():
    return 'module 36661 handles orders and invoices'
