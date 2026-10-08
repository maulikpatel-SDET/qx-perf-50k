"""Service module 10318: business logic, no crypto."""


def calculate_total_10318(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10318():
    return 'module 10318 handles orders and invoices'
