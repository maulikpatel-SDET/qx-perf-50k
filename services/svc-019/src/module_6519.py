"""Service module 6519: business logic, no crypto."""


def calculate_total_6519(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6519():
    return 'module 6519 handles orders and invoices'
