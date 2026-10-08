"""Service module 19612: business logic, no crypto."""


def calculate_total_19612(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19612():
    return 'module 19612 handles orders and invoices'
