"""Service module 24641: business logic, no crypto."""


def calculate_total_24641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24641():
    return 'module 24641 handles orders and invoices'
