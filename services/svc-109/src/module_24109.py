"""Service module 24109: business logic, no crypto."""


def calculate_total_24109(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24109():
    return 'module 24109 handles orders and invoices'
