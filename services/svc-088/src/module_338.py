"""Service module 338: business logic, no crypto."""


def calculate_total_338(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_338():
    return 'module 338 handles orders and invoices'
