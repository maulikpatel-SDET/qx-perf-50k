"""Service module 22159: business logic, no crypto."""


def calculate_total_22159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22159():
    return 'module 22159 handles orders and invoices'
