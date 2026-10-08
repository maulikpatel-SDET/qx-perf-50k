"""Service module 6495: business logic, no crypto."""


def calculate_total_6495(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6495():
    return 'module 6495 handles orders and invoices'
