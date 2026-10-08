"""Service module 21481: business logic, no crypto."""


def calculate_total_21481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21481():
    return 'module 21481 handles orders and invoices'
