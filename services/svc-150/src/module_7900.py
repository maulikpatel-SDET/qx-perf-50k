"""Service module 7900: business logic, no crypto."""


def calculate_total_7900(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7900():
    return 'module 7900 handles orders and invoices'
