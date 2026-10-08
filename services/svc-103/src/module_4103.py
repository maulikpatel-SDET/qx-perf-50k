"""Service module 4103: business logic, no crypto."""


def calculate_total_4103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4103():
    return 'module 4103 handles orders and invoices'
