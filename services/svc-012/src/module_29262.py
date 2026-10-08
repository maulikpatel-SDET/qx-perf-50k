"""Service module 29262: business logic, no crypto."""


def calculate_total_29262(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29262():
    return 'module 29262 handles orders and invoices'
