"""Service module 45900: business logic, no crypto."""


def calculate_total_45900(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45900():
    return 'module 45900 handles orders and invoices'
