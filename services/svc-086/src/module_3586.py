"""Service module 3586: business logic, no crypto."""


def calculate_total_3586(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3586():
    return 'module 3586 handles orders and invoices'
