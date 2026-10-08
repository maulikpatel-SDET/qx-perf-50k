"""Service module 5661: business logic, no crypto."""


def calculate_total_5661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5661():
    return 'module 5661 handles orders and invoices'
