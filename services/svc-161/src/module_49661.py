"""Service module 49661: business logic, no crypto."""


def calculate_total_49661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49661():
    return 'module 49661 handles orders and invoices'
