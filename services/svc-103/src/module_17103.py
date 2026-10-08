"""Service module 17103: business logic, no crypto."""


def calculate_total_17103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17103():
    return 'module 17103 handles orders and invoices'
