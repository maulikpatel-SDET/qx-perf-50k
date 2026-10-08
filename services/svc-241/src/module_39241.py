"""Service module 39241: business logic, no crypto."""


def calculate_total_39241(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39241():
    return 'module 39241 handles orders and invoices'
