"""Service module 4407: business logic, no crypto."""


def calculate_total_4407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4407():
    return 'module 4407 handles orders and invoices'
