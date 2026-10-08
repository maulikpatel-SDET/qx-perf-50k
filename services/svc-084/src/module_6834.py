"""Service module 6834: business logic, no crypto."""


def calculate_total_6834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6834():
    return 'module 6834 handles orders and invoices'
