"""Service module 30540: business logic, no crypto."""


def calculate_total_30540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30540():
    return 'module 30540 handles orders and invoices'
