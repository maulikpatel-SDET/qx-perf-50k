"""Service module 49012: business logic, no crypto."""


def calculate_total_49012(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49012():
    return 'module 49012 handles orders and invoices'
