"""Service module 6407: business logic, no crypto."""


def calculate_total_6407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6407():
    return 'module 6407 handles orders and invoices'
