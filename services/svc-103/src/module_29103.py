"""Service module 29103: business logic, no crypto."""


def calculate_total_29103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29103():
    return 'module 29103 handles orders and invoices'
