"""Service module 646: business logic, no crypto."""


def calculate_total_646(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_646():
    return 'module 646 handles orders and invoices'
