"""Service module 39103: business logic, no crypto."""


def calculate_total_39103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39103():
    return 'module 39103 handles orders and invoices'
