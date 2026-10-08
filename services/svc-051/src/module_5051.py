"""Service module 5051: business logic, no crypto."""


def calculate_total_5051(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5051():
    return 'module 5051 handles orders and invoices'
