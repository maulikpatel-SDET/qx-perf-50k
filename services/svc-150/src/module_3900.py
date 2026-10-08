"""Service module 3900: business logic, no crypto."""


def calculate_total_3900(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3900():
    return 'module 3900 handles orders and invoices'
