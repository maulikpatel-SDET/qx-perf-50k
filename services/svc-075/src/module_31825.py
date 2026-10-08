"""Service module 31825: business logic, no crypto."""


def calculate_total_31825(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31825():
    return 'module 31825 handles orders and invoices'
