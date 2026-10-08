"""Service module 34454: business logic, no crypto."""


def calculate_total_34454(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34454():
    return 'module 34454 handles orders and invoices'
