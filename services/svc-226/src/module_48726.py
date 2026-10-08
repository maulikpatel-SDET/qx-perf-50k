"""Service module 48726: business logic, no crypto."""


def calculate_total_48726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48726():
    return 'module 48726 handles orders and invoices'
