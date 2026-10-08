"""Service module 15902: business logic, no crypto."""


def calculate_total_15902(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15902():
    return 'module 15902 handles orders and invoices'
