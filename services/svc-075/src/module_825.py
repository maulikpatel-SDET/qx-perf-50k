"""Service module 825: business logic, no crypto."""


def calculate_total_825(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_825():
    return 'module 825 handles orders and invoices'
