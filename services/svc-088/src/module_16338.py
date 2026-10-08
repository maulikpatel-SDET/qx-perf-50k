"""Service module 16338: business logic, no crypto."""


def calculate_total_16338(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16338():
    return 'module 16338 handles orders and invoices'
