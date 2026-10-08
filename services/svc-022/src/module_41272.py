"""Service module 41272: business logic, no crypto."""


def calculate_total_41272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41272():
    return 'module 41272 handles orders and invoices'
