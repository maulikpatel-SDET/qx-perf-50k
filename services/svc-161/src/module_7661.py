"""Service module 7661: business logic, no crypto."""


def calculate_total_7661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7661():
    return 'module 7661 handles orders and invoices'
