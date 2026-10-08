"""Service module 37536: business logic, no crypto."""


def calculate_total_37536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37536():
    return 'module 37536 handles orders and invoices'
