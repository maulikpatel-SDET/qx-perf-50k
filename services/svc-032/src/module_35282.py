"""Service module 35282: business logic, no crypto."""


def calculate_total_35282(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35282():
    return 'module 35282 handles orders and invoices'
