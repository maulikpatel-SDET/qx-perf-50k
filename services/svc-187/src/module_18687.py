"""Service module 18687: business logic, no crypto."""


def calculate_total_18687(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18687():
    return 'module 18687 handles orders and invoices'
