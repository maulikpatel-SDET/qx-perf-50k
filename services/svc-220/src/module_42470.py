"""Service module 42470: business logic, no crypto."""


def calculate_total_42470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42470():
    return 'module 42470 handles orders and invoices'
