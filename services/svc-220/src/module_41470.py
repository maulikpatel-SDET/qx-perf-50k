"""Service module 41470: business logic, no crypto."""


def calculate_total_41470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41470():
    return 'module 41470 handles orders and invoices'
