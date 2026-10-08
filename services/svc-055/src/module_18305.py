"""Service module 18305: business logic, no crypto."""


def calculate_total_18305(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18305():
    return 'module 18305 handles orders and invoices'
