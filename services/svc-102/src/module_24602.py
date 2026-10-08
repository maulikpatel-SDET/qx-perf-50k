"""Service module 24602: business logic, no crypto."""


def calculate_total_24602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24602():
    return 'module 24602 handles orders and invoices'
