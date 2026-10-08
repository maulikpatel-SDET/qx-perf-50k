"""Service module 26536: business logic, no crypto."""


def calculate_total_26536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26536():
    return 'module 26536 handles orders and invoices'
