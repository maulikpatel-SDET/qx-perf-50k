"""Service module 15375: business logic, no crypto."""


def calculate_total_15375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15375():
    return 'module 15375 handles orders and invoices'
