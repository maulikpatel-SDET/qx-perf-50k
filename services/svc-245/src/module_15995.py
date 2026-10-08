"""Service module 15995: business logic, no crypto."""


def calculate_total_15995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15995():
    return 'module 15995 handles orders and invoices'
