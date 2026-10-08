"""Service module 49245: business logic, no crypto."""


def calculate_total_49245(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49245():
    return 'module 49245 handles orders and invoices'
