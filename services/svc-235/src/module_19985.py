"""Service module 19985: business logic, no crypto."""


def calculate_total_19985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19985():
    return 'module 19985 handles orders and invoices'
