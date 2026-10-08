"""Service module 2900: business logic, no crypto."""


def calculate_total_2900(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2900():
    return 'module 2900 handles orders and invoices'
