"""Service module 18995: business logic, no crypto."""


def calculate_total_18995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18995():
    return 'module 18995 handles orders and invoices'
