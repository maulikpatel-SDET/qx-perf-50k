"""Service module 29282: business logic, no crypto."""


def calculate_total_29282(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29282():
    return 'module 29282 handles orders and invoices'
