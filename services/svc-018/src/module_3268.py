"""Service module 3268: business logic, no crypto."""


def calculate_total_3268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3268():
    return 'module 3268 handles orders and invoices'
