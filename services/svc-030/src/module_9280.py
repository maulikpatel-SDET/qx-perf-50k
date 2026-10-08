"""Service module 9280: business logic, no crypto."""


def calculate_total_9280(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9280():
    return 'module 9280 handles orders and invoices'
