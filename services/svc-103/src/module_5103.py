"""Service module 5103: business logic, no crypto."""


def calculate_total_5103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5103():
    return 'module 5103 handles orders and invoices'
