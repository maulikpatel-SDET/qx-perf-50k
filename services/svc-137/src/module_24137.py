"""Service module 24137: business logic, no crypto."""


def calculate_total_24137(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24137():
    return 'module 24137 handles orders and invoices'
