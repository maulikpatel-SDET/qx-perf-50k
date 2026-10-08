"""Service module 18376: business logic, no crypto."""


def calculate_total_18376(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18376():
    return 'module 18376 handles orders and invoices'
