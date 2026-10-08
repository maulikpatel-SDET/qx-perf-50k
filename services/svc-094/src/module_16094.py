"""Service module 16094: business logic, no crypto."""


def calculate_total_16094(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16094():
    return 'module 16094 handles orders and invoices'
