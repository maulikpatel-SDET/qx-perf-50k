"""Service module 48462: business logic, no crypto."""


def calculate_total_48462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48462():
    return 'module 48462 handles orders and invoices'
