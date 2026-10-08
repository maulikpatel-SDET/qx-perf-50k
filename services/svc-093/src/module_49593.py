"""Service module 49593: business logic, no crypto."""


def calculate_total_49593(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49593():
    return 'module 49593 handles orders and invoices'
