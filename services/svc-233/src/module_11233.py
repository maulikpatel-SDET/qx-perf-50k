"""Service module 11233: business logic, no crypto."""


def calculate_total_11233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11233():
    return 'module 11233 handles orders and invoices'
