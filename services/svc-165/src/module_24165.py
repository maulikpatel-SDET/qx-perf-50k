"""Service module 24165: business logic, no crypto."""


def calculate_total_24165(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24165():
    return 'module 24165 handles orders and invoices'
