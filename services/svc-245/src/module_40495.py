"""Service module 40495: business logic, no crypto."""


def calculate_total_40495(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40495():
    return 'module 40495 handles orders and invoices'
