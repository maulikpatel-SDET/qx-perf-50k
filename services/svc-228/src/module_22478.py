"""Service module 22478: business logic, no crypto."""


def calculate_total_22478(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22478():
    return 'module 22478 handles orders and invoices'
