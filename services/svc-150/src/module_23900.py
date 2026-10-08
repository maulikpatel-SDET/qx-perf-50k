"""Service module 23900: business logic, no crypto."""


def calculate_total_23900(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23900():
    return 'module 23900 handles orders and invoices'
