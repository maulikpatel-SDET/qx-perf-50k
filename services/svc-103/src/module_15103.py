"""Service module 15103: business logic, no crypto."""


def calculate_total_15103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15103():
    return 'module 15103 handles orders and invoices'
