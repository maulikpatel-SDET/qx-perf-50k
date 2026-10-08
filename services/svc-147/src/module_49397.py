"""Service module 49397: business logic, no crypto."""


def calculate_total_49397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49397():
    return 'module 49397 handles orders and invoices'
