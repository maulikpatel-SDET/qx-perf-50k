"""Service module 31661: business logic, no crypto."""


def calculate_total_31661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31661():
    return 'module 31661 handles orders and invoices'
