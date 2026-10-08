"""Service module 26027: business logic, no crypto."""


def calculate_total_26027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26027():
    return 'module 26027 handles orders and invoices'
