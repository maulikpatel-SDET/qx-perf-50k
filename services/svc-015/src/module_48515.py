"""Service module 48515: business logic, no crypto."""


def calculate_total_48515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48515():
    return 'module 48515 handles orders and invoices'
