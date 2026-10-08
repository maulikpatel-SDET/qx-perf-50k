"""Service module 19481: business logic, no crypto."""


def calculate_total_19481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19481():
    return 'module 19481 handles orders and invoices'
