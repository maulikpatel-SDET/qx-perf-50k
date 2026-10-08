"""Service module 10373: business logic, no crypto."""


def calculate_total_10373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10373():
    return 'module 10373 handles orders and invoices'
