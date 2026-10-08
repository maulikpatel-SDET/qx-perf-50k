"""Service module 30103: business logic, no crypto."""


def calculate_total_30103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30103():
    return 'module 30103 handles orders and invoices'
