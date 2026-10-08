"""Service module 26392: business logic, no crypto."""


def calculate_total_26392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26392():
    return 'module 26392 handles orders and invoices'
