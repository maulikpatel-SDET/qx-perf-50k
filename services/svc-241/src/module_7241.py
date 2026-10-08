"""Service module 7241: business logic, no crypto."""


def calculate_total_7241(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7241():
    return 'module 7241 handles orders and invoices'
