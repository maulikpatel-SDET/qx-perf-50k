"""Service module 34481: business logic, no crypto."""


def calculate_total_34481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34481():
    return 'module 34481 handles orders and invoices'
