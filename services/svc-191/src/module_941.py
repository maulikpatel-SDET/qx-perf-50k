"""Service module 941: business logic, no crypto."""


def calculate_total_941(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_941():
    return 'module 941 handles orders and invoices'
