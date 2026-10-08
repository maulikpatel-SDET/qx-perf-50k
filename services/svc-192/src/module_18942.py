"""Service module 18942: business logic, no crypto."""


def calculate_total_18942(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18942():
    return 'module 18942 handles orders and invoices'
