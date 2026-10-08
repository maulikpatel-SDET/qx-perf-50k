"""Service module 42833: business logic, no crypto."""


def calculate_total_42833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42833():
    return 'module 42833 handles orders and invoices'
