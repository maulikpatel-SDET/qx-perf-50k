"""Service module 35373: business logic, no crypto."""


def calculate_total_35373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35373():
    return 'module 35373 handles orders and invoices'
