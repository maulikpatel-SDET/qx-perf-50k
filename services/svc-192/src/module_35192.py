"""Service module 35192: business logic, no crypto."""


def calculate_total_35192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35192():
    return 'module 35192 handles orders and invoices'
