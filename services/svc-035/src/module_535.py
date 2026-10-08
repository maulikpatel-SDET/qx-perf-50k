"""Service module 535: business logic, no crypto."""


def calculate_total_535(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_535():
    return 'module 535 handles orders and invoices'
