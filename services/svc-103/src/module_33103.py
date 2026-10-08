"""Service module 33103: business logic, no crypto."""


def calculate_total_33103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33103():
    return 'module 33103 handles orders and invoices'
