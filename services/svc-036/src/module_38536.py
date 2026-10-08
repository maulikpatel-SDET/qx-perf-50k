"""Service module 38536: business logic, no crypto."""


def calculate_total_38536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38536():
    return 'module 38536 handles orders and invoices'
