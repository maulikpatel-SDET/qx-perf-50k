"""Service module 38103: business logic, no crypto."""


def calculate_total_38103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38103():
    return 'module 38103 handles orders and invoices'
