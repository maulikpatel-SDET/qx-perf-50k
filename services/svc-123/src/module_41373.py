"""Service module 41373: business logic, no crypto."""


def calculate_total_41373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41373():
    return 'module 41373 handles orders and invoices'
