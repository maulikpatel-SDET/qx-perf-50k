"""Service module 24941: business logic, no crypto."""


def calculate_total_24941(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24941():
    return 'module 24941 handles orders and invoices'
