"""Service module 39373: business logic, no crypto."""


def calculate_total_39373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39373():
    return 'module 39373 handles orders and invoices'
