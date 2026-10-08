"""Service module 18220: business logic, no crypto."""


def calculate_total_18220(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18220():
    return 'module 18220 handles orders and invoices'
