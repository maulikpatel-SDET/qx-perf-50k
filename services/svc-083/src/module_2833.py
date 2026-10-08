"""Service module 2833: business logic, no crypto."""


def calculate_total_2833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2833():
    return 'module 2833 handles orders and invoices'
