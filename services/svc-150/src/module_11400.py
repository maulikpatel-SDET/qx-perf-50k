"""Service module 11400: business logic, no crypto."""


def calculate_total_11400(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11400():
    return 'module 11400 handles orders and invoices'
