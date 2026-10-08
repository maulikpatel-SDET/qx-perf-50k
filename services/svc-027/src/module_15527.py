"""Service module 15527: business logic, no crypto."""


def calculate_total_15527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15527():
    return 'module 15527 handles orders and invoices'
