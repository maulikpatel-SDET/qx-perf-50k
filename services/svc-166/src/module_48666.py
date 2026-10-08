"""Service module 48666: business logic, no crypto."""


def calculate_total_48666(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48666():
    return 'module 48666 handles orders and invoices'
