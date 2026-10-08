"""Service module 45735: business logic, no crypto."""


def calculate_total_45735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45735():
    return 'module 45735 handles orders and invoices'
