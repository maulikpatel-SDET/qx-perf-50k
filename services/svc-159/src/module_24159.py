"""Service module 24159: business logic, no crypto."""


def calculate_total_24159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24159():
    return 'module 24159 handles orders and invoices'
