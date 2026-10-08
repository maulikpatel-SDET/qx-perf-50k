"""Service module 373: business logic, no crypto."""


def calculate_total_373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_373():
    return 'module 373 handles orders and invoices'
