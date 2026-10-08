"""Service module 11322: business logic, no crypto."""


def calculate_total_11322(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11322():
    return 'module 11322 handles orders and invoices'
