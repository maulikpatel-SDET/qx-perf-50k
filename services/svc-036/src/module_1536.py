"""Service module 1536: business logic, no crypto."""


def calculate_total_1536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1536():
    return 'module 1536 handles orders and invoices'
