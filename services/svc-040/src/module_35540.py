"""Service module 35540: business logic, no crypto."""


def calculate_total_35540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35540():
    return 'module 35540 handles orders and invoices'
