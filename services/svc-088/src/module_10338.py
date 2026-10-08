"""Service module 10338: business logic, no crypto."""


def calculate_total_10338(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10338():
    return 'module 10338 handles orders and invoices'
