"""Service module 17373: business logic, no crypto."""


def calculate_total_17373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17373():
    return 'module 17373 handles orders and invoices'
