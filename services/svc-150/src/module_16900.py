"""Service module 16900: business logic, no crypto."""


def calculate_total_16900(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16900():
    return 'module 16900 handles orders and invoices'
