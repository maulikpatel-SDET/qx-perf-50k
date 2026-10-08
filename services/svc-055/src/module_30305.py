"""Service module 30305: business logic, no crypto."""


def calculate_total_30305(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30305():
    return 'module 30305 handles orders and invoices'
