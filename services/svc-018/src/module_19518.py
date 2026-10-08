"""Service module 19518: business logic, no crypto."""


def calculate_total_19518(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19518():
    return 'module 19518 handles orders and invoices'
