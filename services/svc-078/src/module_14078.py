"""Service module 14078: business logic, no crypto."""


def calculate_total_14078(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14078():
    return 'module 14078 handles orders and invoices'
