"""Service module 33299: business logic, no crypto."""


def calculate_total_33299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33299():
    return 'module 33299 handles orders and invoices'
