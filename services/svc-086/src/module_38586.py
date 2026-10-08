"""Service module 38586: business logic, no crypto."""


def calculate_total_38586(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38586():
    return 'module 38586 handles orders and invoices'
