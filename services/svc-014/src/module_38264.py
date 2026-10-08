"""Service module 38264: business logic, no crypto."""


def calculate_total_38264(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38264():
    return 'module 38264 handles orders and invoices'
