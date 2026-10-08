"""Service module 44839: business logic, no crypto."""


def calculate_total_44839(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44839():
    return 'module 44839 handles orders and invoices'
