"""Service module 35376: business logic, no crypto."""


def calculate_total_35376(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35376():
    return 'module 35376 handles orders and invoices'
