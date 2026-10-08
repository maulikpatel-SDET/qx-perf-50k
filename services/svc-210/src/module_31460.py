"""Service module 31460: business logic, no crypto."""


def calculate_total_31460(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31460():
    return 'module 31460 handles orders and invoices'
