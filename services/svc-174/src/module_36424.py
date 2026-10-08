"""Service module 36424: business logic, no crypto."""


def calculate_total_36424(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36424():
    return 'module 36424 handles orders and invoices'
