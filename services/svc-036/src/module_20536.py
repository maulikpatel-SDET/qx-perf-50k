"""Service module 20536: business logic, no crypto."""


def calculate_total_20536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20536():
    return 'module 20536 handles orders and invoices'
