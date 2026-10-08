"""Service module 18049: business logic, no crypto."""


def calculate_total_18049(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18049():
    return 'module 18049 handles orders and invoices'
