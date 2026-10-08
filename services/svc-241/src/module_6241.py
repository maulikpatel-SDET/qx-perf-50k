"""Service module 6241: business logic, no crypto."""


def calculate_total_6241(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6241():
    return 'module 6241 handles orders and invoices'
