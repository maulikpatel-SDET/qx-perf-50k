"""Service module 20103: business logic, no crypto."""


def calculate_total_20103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20103():
    return 'module 20103 handles orders and invoices'
