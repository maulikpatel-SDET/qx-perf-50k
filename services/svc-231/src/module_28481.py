"""Service module 28481: business logic, no crypto."""


def calculate_total_28481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28481():
    return 'module 28481 handles orders and invoices'
