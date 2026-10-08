"""Service module 15508: business logic, no crypto."""


def calculate_total_15508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15508():
    return 'module 15508 handles orders and invoices'
