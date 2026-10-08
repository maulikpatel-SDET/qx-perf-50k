"""Service module 26682: business logic, no crypto."""


def calculate_total_26682(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26682():
    return 'module 26682 handles orders and invoices'
