"""Service module 23103: business logic, no crypto."""


def calculate_total_23103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23103():
    return 'module 23103 handles orders and invoices'
