"""Service module 39474: business logic, no crypto."""


def calculate_total_39474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39474():
    return 'module 39474 handles orders and invoices'
