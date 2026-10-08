"""Service module 40385: business logic, no crypto."""


def calculate_total_40385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40385():
    return 'module 40385 handles orders and invoices'
