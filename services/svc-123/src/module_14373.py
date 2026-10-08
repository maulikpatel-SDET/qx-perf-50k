"""Service module 14373: business logic, no crypto."""


def calculate_total_14373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14373():
    return 'module 14373 handles orders and invoices'
