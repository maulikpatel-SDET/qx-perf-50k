"""Service module 44338: business logic, no crypto."""


def calculate_total_44338(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44338():
    return 'module 44338 handles orders and invoices'
