"""Service module 37540: business logic, no crypto."""


def calculate_total_37540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37540():
    return 'module 37540 handles orders and invoices'
