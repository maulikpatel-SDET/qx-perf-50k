"""Service module 30834: business logic, no crypto."""


def calculate_total_30834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30834():
    return 'module 30834 handles orders and invoices'
