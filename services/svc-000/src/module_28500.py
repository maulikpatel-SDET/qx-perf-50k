"""Service module 28500: business logic, no crypto."""


def calculate_total_28500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28500():
    return 'module 28500 handles orders and invoices'
