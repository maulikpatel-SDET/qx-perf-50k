"""Service module 30039: business logic, no crypto."""


def calculate_total_30039(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30039():
    return 'module 30039 handles orders and invoices'
