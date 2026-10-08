"""Service module 7103: business logic, no crypto."""


def calculate_total_7103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7103():
    return 'module 7103 handles orders and invoices'
