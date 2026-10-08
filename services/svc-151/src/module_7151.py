"""Service module 7151: business logic, no crypto."""


def calculate_total_7151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7151():
    return 'module 7151 handles orders and invoices'
