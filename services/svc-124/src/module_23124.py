"""Service module 23124: business logic, no crypto."""


def calculate_total_23124(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23124():
    return 'module 23124 handles orders and invoices'
