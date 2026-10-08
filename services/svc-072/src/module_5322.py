"""Service module 5322: business logic, no crypto."""


def calculate_total_5322(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5322():
    return 'module 5322 handles orders and invoices'
