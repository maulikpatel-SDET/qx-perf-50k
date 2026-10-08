"""Service module 29710: business logic, no crypto."""


def calculate_total_29710(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29710():
    return 'module 29710 handles orders and invoices'
