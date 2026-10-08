"""Service module 36069: business logic, no crypto."""


def calculate_total_36069(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36069():
    return 'module 36069 handles orders and invoices'
