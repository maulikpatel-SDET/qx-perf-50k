"""Service module 40422: business logic, no crypto."""


def calculate_total_40422(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40422():
    return 'module 40422 handles orders and invoices'
