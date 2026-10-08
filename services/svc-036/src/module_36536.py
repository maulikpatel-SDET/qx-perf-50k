"""Service module 36536: business logic, no crypto."""


def calculate_total_36536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36536():
    return 'module 36536 handles orders and invoices'
