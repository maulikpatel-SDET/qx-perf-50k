"""Service module 35661: business logic, no crypto."""


def calculate_total_35661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35661():
    return 'module 35661 handles orders and invoices'
