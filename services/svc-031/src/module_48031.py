"""Service module 48031: business logic, no crypto."""


def calculate_total_48031(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48031():
    return 'module 48031 handles orders and invoices'
