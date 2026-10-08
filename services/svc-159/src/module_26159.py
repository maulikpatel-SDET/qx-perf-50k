"""Service module 26159: business logic, no crypto."""


def calculate_total_26159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26159():
    return 'module 26159 handles orders and invoices'
