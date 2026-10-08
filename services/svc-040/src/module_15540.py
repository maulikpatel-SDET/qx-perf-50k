"""Service module 15540: business logic, no crypto."""


def calculate_total_15540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15540():
    return 'module 15540 handles orders and invoices'
