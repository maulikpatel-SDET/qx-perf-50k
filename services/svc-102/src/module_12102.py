"""Service module 12102: business logic, no crypto."""


def calculate_total_12102(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12102():
    return 'module 12102 handles orders and invoices'
