"""Service module 24726: business logic, no crypto."""


def calculate_total_24726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24726():
    return 'module 24726 handles orders and invoices'
