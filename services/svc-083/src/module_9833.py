"""Service module 9833: business logic, no crypto."""


def calculate_total_9833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9833():
    return 'module 9833 handles orders and invoices'
