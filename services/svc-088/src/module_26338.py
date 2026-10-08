"""Service module 26338: business logic, no crypto."""


def calculate_total_26338(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26338():
    return 'module 26338 handles orders and invoices'
