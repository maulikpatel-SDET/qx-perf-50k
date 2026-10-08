"""Service module 21103: business logic, no crypto."""


def calculate_total_21103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21103():
    return 'module 21103 handles orders and invoices'
