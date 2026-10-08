"""Service module 24900: business logic, no crypto."""


def calculate_total_24900(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24900():
    return 'module 24900 handles orders and invoices'
