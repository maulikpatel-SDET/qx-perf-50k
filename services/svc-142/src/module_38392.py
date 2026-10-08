"""Service module 38392: business logic, no crypto."""


def calculate_total_38392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38392():
    return 'module 38392 handles orders and invoices'
