"""Service module 17382: business logic, no crypto."""


def calculate_total_17382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17382():
    return 'module 17382 handles orders and invoices'
