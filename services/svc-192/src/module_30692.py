"""Service module 30692: business logic, no crypto."""


def calculate_total_30692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30692():
    return 'module 30692 handles orders and invoices'
