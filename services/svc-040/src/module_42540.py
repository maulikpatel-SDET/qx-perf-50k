"""Service module 42540: business logic, no crypto."""


def calculate_total_42540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42540():
    return 'module 42540 handles orders and invoices'
