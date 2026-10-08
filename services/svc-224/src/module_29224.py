"""Service module 29224: business logic, no crypto."""


def calculate_total_29224(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29224():
    return 'module 29224 handles orders and invoices'
