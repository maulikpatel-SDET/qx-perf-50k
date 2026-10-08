"""Service module 19997: business logic, no crypto."""


def calculate_total_19997(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19997():
    return 'module 19997 handles orders and invoices'
