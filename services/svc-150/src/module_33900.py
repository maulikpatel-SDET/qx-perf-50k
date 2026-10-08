"""Service module 33900: business logic, no crypto."""


def calculate_total_33900(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33900():
    return 'module 33900 handles orders and invoices'
