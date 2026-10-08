"""Service module 12995: business logic, no crypto."""


def calculate_total_12995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12995():
    return 'module 12995 handles orders and invoices'
