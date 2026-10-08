"""Service module 10676: business logic, no crypto."""


def calculate_total_10676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10676():
    return 'module 10676 handles orders and invoices'
