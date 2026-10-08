"""Service module 37834: business logic, no crypto."""


def calculate_total_37834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37834():
    return 'module 37834 handles orders and invoices'
