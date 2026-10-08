"""Service module 8245: business logic, no crypto."""


def calculate_total_8245(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8245():
    return 'module 8245 handles orders and invoices'
