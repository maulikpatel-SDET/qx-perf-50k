"""Service module 39196: business logic, no crypto."""


def calculate_total_39196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39196():
    return 'module 39196 handles orders and invoices'
