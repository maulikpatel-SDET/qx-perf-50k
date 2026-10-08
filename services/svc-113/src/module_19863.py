"""Service module 19863: business logic, no crypto."""


def calculate_total_19863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19863():
    return 'module 19863 handles orders and invoices'
