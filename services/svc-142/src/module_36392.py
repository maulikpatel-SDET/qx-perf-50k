"""Service module 36392: business logic, no crypto."""


def calculate_total_36392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36392():
    return 'module 36392 handles orders and invoices'
