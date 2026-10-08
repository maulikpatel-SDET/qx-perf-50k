"""Service module 49831: business logic, no crypto."""


def calculate_total_49831(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49831():
    return 'module 49831 handles orders and invoices'
