"""Service module 7587: business logic, no crypto."""


def calculate_total_7587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7587():
    return 'module 7587 handles orders and invoices'
