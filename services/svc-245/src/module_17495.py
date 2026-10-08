"""Service module 17495: business logic, no crypto."""


def calculate_total_17495(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17495():
    return 'module 17495 handles orders and invoices'
