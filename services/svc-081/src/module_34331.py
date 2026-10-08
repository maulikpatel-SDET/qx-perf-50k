"""Service module 34331: business logic, no crypto."""


def calculate_total_34331(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34331():
    return 'module 34331 handles orders and invoices'
