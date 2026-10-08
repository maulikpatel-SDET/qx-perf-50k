"""Service module 16293: business logic, no crypto."""


def calculate_total_16293(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16293():
    return 'module 16293 handles orders and invoices'
