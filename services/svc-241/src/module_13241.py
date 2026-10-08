"""Service module 13241: business logic, no crypto."""


def calculate_total_13241(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13241():
    return 'module 13241 handles orders and invoices'
