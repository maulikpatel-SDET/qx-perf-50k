"""Service module 28540: business logic, no crypto."""


def calculate_total_28540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28540():
    return 'module 28540 handles orders and invoices'
