"""Service module 7995: business logic, no crypto."""


def calculate_total_7995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7995():
    return 'module 7995 handles orders and invoices'
